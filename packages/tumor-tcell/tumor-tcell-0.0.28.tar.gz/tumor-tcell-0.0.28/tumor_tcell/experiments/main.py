"""
========================
Tumor/T cell Experiments
========================

`tumor_tcell_abm` is the main function for generating and simulating tumor/T cell simulations in a
2D microenvironment. The T cells can interact with tumor cells in the following ways:
 * T cell receptor (TCR on T cells) and Major histocompatibility complex I receptor (MHCI on tumor cells) for activation of T cells, induction of IFNg and cytotoxic packet secretion, and slowing of T cell migration
 * PD1 receptor (on T cells) and PDL1 receptor (on tumor cells) that can inhibit cell activation and induce apoptosis
 * T cells secrete IFNg which tumor cells uptake and causes state switch to upregulate MHCI, PDL1, and decrease proliferation

Experiments can be triggered from the command line:

    $ python tumor_tcell/experiments/main.py -w [workflow id]

You can find information on the different workflows by reading the comments included for each entry in `workflow_library`,
at the bottom of this file.
"""

import random
import time as clock
from tqdm import tqdm
import math

# vivarium-core imports
from vivarium.core.engine import Engine, timestamp
from vivarium.library.units import units, remove_units
from vivarium.core.control import Control

# plots
from vivarium.plots.agents_multigen import plot_agents_multigen
from tumor_tcell.plots.video import make_video
from tumor_tcell.plots.snapshots import plot_snapshots, format_snapshot_data

# tumor-tcell imports
from tumor_tcell.composites.tumor_agent import TumorAgent
from tumor_tcell.composites.t_cell_agent import TCellAgent
from tumor_tcell.composites.tumor_microenvironment import TumorMicroEnvironment
from tumor_tcell.composites.death_logger import DeathLogger

# default parameters
PI = math.pi
TIMESTEP = 60
NBINS = [20, 20]
DEPTH = 15  # um
BOUNDS = [200 * units.um, 200 * units.um]

TUMOR_ID = 'tumor'
TCELL_ID = 'tcell'

# parameters for toy experiments
MEDIUM_BOUNDS = [90*units.um, 90*units.um]

# plotting
TAG_COLORS = {
    ('internal', 'cell_state', 'PDL1p'): 'skyblue',
    ('internal', 'cell_state', 'PDL1n'): 'indianred',
    ('internal', 'cell_state', 'PD1p'): 'limegreen',
    ('internal', 'cell_state', 'PD1n'): 'darkorange', }


def get_tcells(
        number=1,
        relative_pd1n=0.2,
        total_pd1n=None
):
    """
    make an initial state for any number of tcell instances,
    with either PD1 negative (`PD1n`) or PD1 positive (`PD1p`) states determined by the parameter
    `relative_pd1n` or `total_pd1n`.
    """
    if total_pd1n:
        assert isinstance(total_pd1n, int)
        return {
        '{}_{}'.format(TCELL_ID, n): {
            'type': 'tcell',
            'cell_state': 'PD1n' if n < total_pd1n else 'PD1p',
            'TCR_timer': random.uniform(0, 5400),
            'velocity_timer': 0,
            'velocity': 10.0 * units.um/units.min,
            'diameter': 7.5 * units.um,
        } for n in range(number)}
    else:
        assert relative_pd1n <= 1.0
        return {
        '{}_{}'.format(TCELL_ID, n): {
            'type': 'tcell',
            'cell_state': 'PD1n' if random.uniform(0, 1) < relative_pd1n else 'PD1p',
            'TCR_timer': random.uniform(0, 5400),
            'velocity_timer': 0,
            'velocity': 10.0 * units.um/units.min,
            'diameter': 7.5 * units.um,
        } for n in range(number)}


def get_tumors(number=1, relative_pdl1n=0.5):
    """
    make an initial state for any number of tumor instances,
    with either PD1 negative (`PDL1n`) or PD1 positive (`PDL1p`) states determined by the parameter
    `relative_pdl1n`
    """
    return {
        '{}_{}'.format(TUMOR_ID, n): {
            'type': 'tumor',
            'cell_state': 'PDL1n' if random.uniform(0, 1) < relative_pdl1n else 'PDL1p',
            'diameter': 15 * units.um,
        } for n in range(number)}


def random_location(
        bounds,
        center=None,
        distance_from_center=None,
        excluded_distance_from_center=None
):
    """
    generate a single random location within `bounds`, and within `distance_from_center`
    of a provided `center`. `excluded_distance_from_center` is an additional parameter
    that leaves an empty region around the center point.
    """
    if distance_from_center and excluded_distance_from_center:
        assert distance_from_center > excluded_distance_from_center, \
            'distance_from_center must be greater than excluded_distance_from_center'

    # get the center
    if center:
        center_x = center[0]
        center_y = center[1]
    else:
        center_x = bounds[0]/2
        center_y = bounds[1]/2

    if distance_from_center:
        if excluded_distance_from_center:
            ring_size = distance_from_center - excluded_distance_from_center
            distance = excluded_distance_from_center + ring_size * math.sqrt(random.random())
        else:
            distance = distance_from_center * math.sqrt(random.random())

        angle = random.uniform(0, 2 * PI)
        dy = math.sin(angle)*distance
        dx = math.cos(angle)*distance
        pos_x = center_x+dx
        pos_y = center_y+dy

    elif excluded_distance_from_center:
        in_center = True
        while in_center:
            pos_x = random.uniform(0, bounds[0])
            pos_y = random.uniform(0, bounds[1])
            distance = (pos_x**2 + pos_y**2)**0.5
            if distance > excluded_distance_from_center:
                in_center = False
    else:
        pos_x = random.uniform(0, bounds[0])
        pos_y = random.uniform(0, bounds[1])

    return [pos_x, pos_y]



def lymph_node_location(
        bounds,
        relative_position=[[0.95,1],[0.95,1]]
):
    """return random location within `relative_position` of the total environment `bounds`"""
    return [
        random.uniform(bounds[0]*relative_position[0][0], bounds[0]*relative_position[0][1]),
        random.uniform(bounds[0]*relative_position[1][0], bounds[0]*relative_position[1][1])]

def convert_to_hours(data):
    """Convert seconds to hours"""
    times = list(data.keys())
    for time in times:
        hour = time/3600
        data[hour] = data.pop(time)
    return data


# make defaults
N_TUMORS = 120
N_TCELLS = 9
DEFAULT_TUMORS = get_tumors(number=N_TUMORS)
DEFAULT_TCELLS = get_tcells(number=N_TCELLS)


# The main simulation function
def tumor_tcell_abm(
    bounds=BOUNDS,
    n_bins=NBINS,
    depth=DEPTH,
    field_molecules=['IFNg'],
    n_tumors=120,
    n_tcells=9,
    tumors=None,
    tcells=None,
    tumors_state_PDL1n=0.5,
    tcells_state_PD1n=0.8,
    tcells_total_PD1n=None,
    total_time=70000,
    sim_step=10*TIMESTEP,  # simulation increments at which halt_threshold is checked
    halt_threshold=300,  # stop simulation at this number
    time_step=TIMESTEP,
    emit_step=1,
    emitter='timeseries',
    parallel=False,
    tumors_distance=None,
    tcells_distance=None,
    tumors_excluded_distance=None,
    tcells_excluded_distance=None,
    tumors_center=None,
    tcell_center=None,
    lymph_nodes=False,
):
    """ Tumor-Tcell simulation

    This function simulates tumor t cell interactions in a spatial environment.

    Arguments:
    * bounds (list): x and y values for the size of the environment, in microns.
    * n_bins (list): number of bins in the x and y dimensions.
    * depth (float): the depth of the microenvironment, in microns.
    * field_molecules (list): the names of molecules in the external field.
    * n_tumors (int): initial number of tumors.
    * n_tcells (int): initial number of t cells.
    * tumors (dict): specifies precisely the initial tumor state.
        If not provided, the function `get_tumors` is used to generate an initial state
        based in n_tumors and tumors_state_PDL1n.
    * tcells (dict): specifies precisely the initial t cell state.
        If not provided, the function `get_tcells` is used to generate an initial state
        based in n_tcells and tcells_state_PD1n or tcells_total_PD1n.
    * tumors_state_PDL1n (float): probability that initial tumors that are PDL1n
    * tcells_state_PD1n (float): probability that initial tcells that are PD1n
    * total_time (float): total simulation time in seconds.
    * sim_step (float): length of simulation increments which check if halt_threshold has been reached.
    * halt_threshold (int): if the total number of cells reaches this value, the simulaiton is terminated.
    * time_step (float): the time step used for the tcell agents, tumor agents, and microenvironment.
    * emit_step (int): the number of time steps between saving simulation state.
    * emitter (str): the type of emitter, choose between "timeseries" and "database".
    * parallel (bool): whether simulations run with parallel processes.
    * tumors_distance (float): if this is set, is places tumors within this distance from tumors_excluded_distance.
    * tcells_distance: if this is set, is places tcells within this distance from tcells_excluded_distance.
    * tumors_excluded_distance (float): if this is set, it excludes tumors within this distance from the center,
        which together with tumors_distances supports ring-like structures.
    * tcells_excluded_distance (float): if this is set, it excludes tcells within this distance from the center,
        which together with tcells_distance supports ring-like structures.
    * tumors_center (list): [x, y] position for the center of the tumors.
    * tcell_center (list): [x, y] position for the center of the tcells.
    * lymph_nodes (bool): sets whether tcells have a lymph node location, and sets behavior of the mother cells
        to not migrate.

    Return:
        Simulation output data (dict)

    Note:
        * the `lymph_nodes` option has not been thoroughly tested.
    """

    ############################
    # Create the configuration #
    ############################

    # Make the composers - these are used to generate simulation modules that are wired
    # together to make the full multi-scale simulation.
    ## T cell composer
    t_cell_config = {
        'tcell': {'_parallel': parallel},
        'time_step': time_step}
    t_cell_composer = TCellAgent(t_cell_config)

    ## Tumor composer
    tumor_config = {
        'tumor': {'_parallel': parallel},
        'time_step': time_step}
    tumor_composer = TumorAgent(tumor_config)

    ## Environment composer
    environment_config = {
        'neighbors_multibody': {
            '_parallel': parallel,
            'time_step': time_step,
            'bounds': bounds},
        'diffusion_field': {
            '_parallel': parallel,
            'time_step': time_step,
            'molecules': field_molecules,
            'bounds': bounds,
            'n_bins': n_bins,
            'depth': depth}}
    environment_composer = TumorMicroEnvironment(environment_config)

    ## process for logging the final time and state of agents
    logger_config = {'time_step': time_step}
    logger_composer = DeathLogger(logger_config)


    #######################################
    # Initialize the composite simulation #
    #######################################

    # make individual composites and merge them
    composite_model = logger_composer.generate()
    environment = environment_composer.generate()
    composite_model.merge(composite=environment)

    # Make the cells
    if not tcells:
        tcells = get_tcells(
            number=n_tcells,
            relative_pd1n=tcells_state_PD1n,
            total_pd1n=tcells_total_PD1n)
    if not tumors:
        tumors = get_tumors(
            number=n_tumors,
            relative_pdl1n=tumors_state_PDL1n)

    # add T cells to the composite
    for agent_id in tcells.keys():
        t_cell = t_cell_composer.generate({'agent_id': agent_id})
        composite_model.merge(composite=t_cell, path=('agents', agent_id))

    # add tumors to the composite
    for agent_id in tumors.keys():
        tumor = tumor_composer.generate({'agent_id': agent_id})
        composite_model.merge(composite=tumor, path=('agents', agent_id))


    ###################################
    # Initialize the simulation state #
    ####################################

    # make the initial environment state
    initial_env_config = {
        'diffusion_field': {'uniform': 0.0}}
    initial_env = composite_model.initial_state(initial_env_config)

    # initialize cell states
    initial_t_cells = {
        agent_id: {
            'boundary': {
                'location': state.get('location', random_location(
                    bounds,
                    center=tcell_center,
                    distance_from_center=tcells_distance,
                    excluded_distance_from_center=tcells_excluded_distance,
                ) if not lymph_nodes else lymph_node_location(bounds)),
                'diameter': state.get('diameter', 7.5 * units.um),
                'velocity': state.get('velocity', 10.0 * units.um/units.min)},
            'globals': {
                'LN_no_migration': lymph_nodes,
            },
            'internal': {
                'cell_state': state.get('cell_state', None),
                'velocity_timer': state.get('velocity_timer', 0),
                'TCR_timer': state.get('TCR_timer', 0)},
            'neighbors': {
                'present': {
                    'PD1': state.get('PD1', None),
                    'TCR': state.get('TCR', 50000)}
            }} for agent_id, state in tcells.items()}

    initial_tumors = {
        agent_id: {
            'internal': {
                'cell_state': state.get('cell_state', None)},
            'boundary': {
                'location': state.get('location', random_location(
                    bounds,
                    center=tumors_center,
                    distance_from_center=tumors_distance,
                    excluded_distance_from_center=tumors_excluded_distance)),
                'diameter': state.get('diameter', 15 * units.um),
                'velocity': state.get('velocity', 0.0 * units.um/units.min)},
            'neighbors': {
                'present': {
                    'PDL1': state.get('PDL1', None),
                    'MHCI': state.get('MHCI', 1000)}
            }} for agent_id, state in tumors.items()}

    # combine all the initial states together
    initial_state = {
        **initial_env,
        'agents': {
            **initial_t_cells, **initial_tumors}}


    ######################
    # Run the simulation #
    ######################

    experiment_id = (f"tumor_tcell_{timestamp()}")
    experiment_config = {
        'description': f"n_tcells: {n_tcells} \n"
                       f"n_tumors: {n_tumors} \n"
                       f"tumors_state_PDL1n: {tumors_state_PDL1n} \n"
                       f"tcells_state_PD1n:{tcells_state_PD1n} \n"
                       f"tcells_total_PD1n:{tcells_total_PD1n} \n"
                       f"total_time:{total_time} \n"
                       f"time_step:{time_step} \n"
                       f"sim_step:{sim_step} \n"
                       f"bounds:{bounds} \n"
                       f"n_bins:{n_bins} \n"
                       f"halt_threshold:{halt_threshold} \n"
                       f"tumors_distance:{tumors_distance} \n"
                       f"tcells_distance: {tcells_distance} \n",
        'processes': composite_model.processes,
        'topology': composite_model.topology,
        'initial_state': initial_state,
        'display_info': False,
        'experiment_id': experiment_id,
        'emit_step': emit_step,
        'emitter': {'type': emitter}}
    print(f'Initializing experiment {experiment_id}')
    experiment = Engine(**experiment_config)

    # run simulation and terminate upon reaching total_time or halt_threshold
    clock_start = clock.time()
    for time in tqdm(range(0, total_time, sim_step)):
        n_agents = len(experiment.state.get_value()['agents'])
        if n_agents < halt_threshold:
            experiment.update(sim_step)
        else:
            print(f'halt threshold of {halt_threshold} reached at time = {time}')
            continue

    # print runtime and finalize
    clock_finish = clock.time() - clock_start
    print('Completed in {:.2f} seconds'.format(clock_finish))
    experiment.end()

    # return the data
    data = experiment.emitter.get_data_deserialized()
    data = convert_to_hours(data)
    return data


FULL_BOUNDS = [1200*units.um, 1200*units.um]
def large_experiment(
        n_tcells=12,
        n_tumors=1200,
        tcells_state_PD1n=None,
        tumors_state_PDL1n=0.5,
        tcells_total_PD1n=None,
        lymph_nodes=False,
        total_time=259200,
        tumors_distance=260 * units.um,  # sqrt(n_tumors)*15(diameter)/2
        tcells_distance=250 * units.um,  # in or out (None) of the tumor
        tcells_excluded_distance=240 * units.um,  # for creating a ring around tumor
):
    """
    Configurable large environment that has many tumors and t cells. Calls tumor_tcell_abm
    with a few key parameters.
    """
    return tumor_tcell_abm(
        n_tcells=n_tcells,
        n_tumors=n_tumors,
        tcells_state_PD1n=tcells_state_PD1n,
        tumors_state_PDL1n=tumors_state_PDL1n,
        tcells_total_PD1n=tcells_total_PD1n,
        total_time=total_time,
        time_step=TIMESTEP,
        sim_step=100*TIMESTEP,
        emit_step=10*TIMESTEP,
        bounds=FULL_BOUNDS,
        n_bins=[120, 120],  # 10 um bin size, usually 120 by 120
        halt_threshold=4000,  # 5000, #sqrt(halt_threshold)*15 <bounds, normally 5000
        emitter='database',
        tumors_distance=tumors_distance,  # sqrt(n_tumors)*15(diameter)/2
        tcells_distance=tcells_distance,  # in or out (None) of the tumor
        tcells_excluded_distance=tcells_excluded_distance,  # for creating a ring around tumor
        lymph_nodes=lymph_nodes,
    )

# Change experimental PD1 and PDL1 levels for full experiment
def tumor_microenvironment_experiment():
    """
    run a large_experiment with parameters based on in vivo measurements.
    This can be used to control the location of the initial cells.
    """
    return large_experiment(
        n_tcells=12,
        total_time=259200,
        tumors_state_PDL1n=0.5,
        tcells_total_PD1n=9,
        tumors_distance=260 * units.um,  # sqrt(n_tumors)*15(diameter)/2
        tcells_distance=220 * units.um,  # in or out (None) of the tumor
        tcells_excluded_distance=200 * units.um,  # for creating a ring around tumor
    )


def lymph_node_experiment():
    """
    WORK IN PROGRESS
    """
    return large_experiment(
        n_tcells=12,
        n_tumors=120,
        tcells_state_PD1n=0.8,
        tumors_state_PDL1n=0.5,
        tcells_total_PD1n=9,
        lymph_nodes=True,
        total_time=60000,
    )


def plots_suite(
        data,
        out_dir=None,
        bounds=BOUNDS,
        n_snapshots=8,
        final_time=None,
):
    """
    plotting function that generates and saves several figures.

    Returns:
        * fig1: t cell multi-generation timeseries plot
        * fig2: tumor multi-generation timeseries plot
        * fig3: snapshot plot
    """

    # separate out t cell and tumor data for the multi-generation plots
    tcell_data = {}
    tumor_data = {}
    for time, time_data in data.items():
        if 'agents' not in time_data:
            continue
        all_agents_data = time_data['agents']
        tcell_data[time] = {
            'agents': {
                agent_id: agent_data
                for agent_id, agent_data in all_agents_data.items()
                if TCELL_ID in agent_id}}
        tumor_data[time] = {
            'agents': {
                agent_id: agent_data
                for agent_id, agent_data in all_agents_data.items()
                if TUMOR_ID in agent_id}}

    # # get the final death log
    # times_vector = list(data.keys())
    # death_log = data[times_vector[-1]]['log']

    # make multi-gen plot for t cells and tumors
    plot_settings = {
        'time_display': '(hr)',
        'skip_paths': [
            ('boundary', 'diameter'),
            ('boundary', 'location')]}
    fig1 = plot_agents_multigen(tcell_data, plot_settings, out_dir, TCELL_ID)
    fig2 = plot_agents_multigen(tumor_data, plot_settings, out_dir, TUMOR_ID)

    # snapshots plot shows cells and chemical fields in space at different times
    # extract data
    agents, fields = format_snapshot_data(data)

    # make the plot
    fig3 = plot_snapshots(
        bounds=remove_units(bounds),
        agents=remove_units(agents),
        fields=fields,
        tag_colors=TAG_COLORS,
        n_snapshots=n_snapshots,
        final_time=final_time,
        out_dir=out_dir,
        filename='snapshots.pdf',
        default_font_size=48,
        field_label_size=48,
        time_display='hr')

    return fig1, fig2, fig3


def make_snapshot_video(
        data,
        bounds,
        n_steps=10,
        out_dir=None
):
    """
    Make a video of a simulation.
    """
    n_times = len(data.keys())
    step = math.ceil(n_times/n_steps)

    make_video(
        data=remove_units(data),
        bounds=remove_units(bounds),
        agent_shape='circle',
        tag_colors=TAG_COLORS,
        step=step,
        out_dir=out_dir,
        time_display='hr',
        filename='tumor_tcell_video'
    )


# tests
def test_medium_simulation():
    # run a test confirming workflow #2 is running
    Control(
        experiments=experiments_library,
        plots=plots_library,
        workflows=workflow_library,
        args=['-w', '2']
    )


######################################
# libraries of experiments and plots #
######################################

experiments_library = {
    # the main experimental function, which uses the default parameters
    '1': tumor_tcell_abm,
    # configurable large environment that has many tumors and t cells.
    '4': large_experiment,
    # a large_experiment with parameters based on in vivo measurements,
    # in which t cells are initialized in a ring around the tumor.
    '5': tumor_microenvironment_experiment,
    # a work-in-progress to place some t cells in a lymph node, at a
    # distance from the tumor.
    '6': lymph_node_experiment,
}
plots_library = {
    # plots a timeseries across multiple generations for the t cells and the tumors.
    # also saves a snapshot plot from multiple time points.
    '1': plots_suite,
    # save a video of the simulation.
    'video': make_snapshot_video,
}

# workflows are sets of configured experiments and plots, which run sequentially.
# these are the primary configurations used to develop and evaluate simulations.
workflow_library = {
    # Workflow "main" is a large simulation with parameters based on in vivo measurements.
    # Expected runtime is ~12 hours
    'main': {
        'name': 'tumor_microenvironment_experiment',
        'experiment': '5',
        'plots': [
            {
                'plot_id': '1',
                'bounds': FULL_BOUNDS
            },
        ],
    },
    # a large experiment for testing purposes
    '1': {
        'name': 'tumor_tcell_experiment',
        'experiment': {
            'experiment_id': '1',
            'total_time': 40000,
        },
        'plots': [
            {
                'plot_id': '1',
                'bounds': BOUNDS
            },
            {
                'plot_id': 'video',
                'bounds': BOUNDS,
                'n_steps': 100,
            },
        ],
    },
    # a good workflow for testing, in a medium-sized environment with a small number of cells
    '2': {
        'name': 'medium_experiment',
        'experiment': {
            'experiment_id': '1',
            'bounds': MEDIUM_BOUNDS,
            'n_tumors': 3,
            'n_tcells': 3,
            'total_time': 50000,
            'n_bins': [3, 3],
            # 'emitter': 'database',
            'tumors_distance': 25 * units.um,
            'tcells_distance': 10 * units.um,
            'parallel': False,
        },
        'plots': [
            {
                'plot_id': '1',
                'bounds': MEDIUM_BOUNDS
            },
            {
                'plot_id': 'video',
                'bounds': MEDIUM_BOUNDS,
                'n_steps': 100,
            },
        ],
    },
    # like the "main" workflow, but less configured.
    '3': {
        'name': 'large_experiment',
        'experiment': '4',
        'plots': [
            {
                'plot_id': '1',
                'bounds': FULL_BOUNDS
            },
        ],
    },
    # an experimental set up for simulating t cells in the lymph node
    'lymph_node': {
        'name': 'lymph_node_experiment',
        'experiment': '6',
        'plots': [
            {
                'plot_id': '1',
                'bounds': FULL_BOUNDS
            },
            {
                'plot_id': 'video',
                'bounds': FULL_BOUNDS,
                'n_steps': 100,
            },
        ],
    },
}

# run with python tumor_tcell/experiments/main.py [workflow id]
if __name__ == '__main__':
    Control(
        experiments=experiments_library,
        plots=plots_library,
        workflows=workflow_library,
    )

import numpy as np
from pyMetaheuristic.algorithm import simulated_annealing
from pyMetaheuristic.utils import graphs
import math


def rosen(xx):
    d = len(xx)
    xi = xx[0:(d-1)]
    xnext = xx[1:d]

    sum_val = sum(100*(xnext_i - xi_i**2)**2 + (xi_i - 1)
                  ** 2 for xi_i, xnext_i in zip(xi, xnext))

    y = sum_val
    return (y)


parameters = {
    'min_values': (-5, -5),
    'max_values': (5, 5),
    'alpha': 0.9,
    'mu': 0,
    'sigma': 1,
    'temperature_iterations': 1000,
    'initial_temperature': 1.0,
    'final_temperature': 0.0001,
    'verbose': True,
    'start_init': None,
    'target_value': None
}

plot_parameters = {
    'min_values': (-5, -5),
    'max_values': (5, 5),
    'step': (0.1, 0.1),
    'solution': [],
    'proj_view': '3D',
    'view': 'notebook'
}
# graphs.plot_single_function(target_function = rosen, **plot_parameters)

sa = simulated_annealing(target_function=rosen, **parameters)

# for x in range(10):
#     tempo_cpu_inicio = time.process_time()
#     tempo_inicio = timeit.default_timer()
#     inicio = time.time()
#     sa = particle_swarm_optimization(target_function = rosen, **parameters)
#     fim = time.time()
#     tempo_fim = timeit.default_timer()
#     tempo_cpu_fim = time.process_time()

#     result.append({
#     'Metodo': 'SA PYMETAHEURISTIC',
#     'valor final X': sa[ -1],
#     'valor final F': sa[:-1],
#     'Rodada': x+1,
#     'tempo de execução(s)': tempo_fim - tempo_inicio,
#     'tempo de execução - CPU(s)': tempo_cpu_fim - tempo_cpu_inicio,
#     })

# for x in result:
#   print(x)

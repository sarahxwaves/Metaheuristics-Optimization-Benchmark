import math
import time
import timeit
from pyMetaheuristic.algorithm import particle_swarm_optimization
from pyMetaheuristic.utils import graphs
import numpy as np

result = []


def rosen(xx):
    d = len(xx)
    xi = xx[0:(d-1)]
    xnext = xx[1:d]

    sum_val = sum(100*(xnext_i - xi_i**2)**2 + (xi_i - 1)
                  ** 2 for xi_i, xnext_i in zip(xi, xnext))

    y = sum_val
    return (y)


parameters = {
    'swarm_size': 250,
    'min_values': (-5, -5),
    'max_values': (5, 5),
    'iterations': 500,
    'decay': 0,
    'w': 0.9,
    'c1': 2,
    'c2': 2,
    'verbose': True,
    'start_init': None,
    'target_value': None
}

# plot_parameters = {
#     'min_values': (-5, -5),
#     'max_values': (5, 5),
#     'step': (0.1, 0.1),
#     'solution': [],
#     'proj_view': '3D',
#     'view': 'notebook'
# }
# graphs.plot_single_function(target_function = ackley, **plot_parameters)

# pso = particle_swarm_optimization(target_function=rosen, **parameters)

# print('Melhor solução: ', pso[-1])

for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    pso = particle_swarm_optimization(target_function=rosen, **parameters)
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    result.append({
        'Metodo': 'PSO PYMETAHEURISTIC',
        'valor final X': pso[-1],
        'valor final F': pso[:-1],
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

for x in result:
    print(x)

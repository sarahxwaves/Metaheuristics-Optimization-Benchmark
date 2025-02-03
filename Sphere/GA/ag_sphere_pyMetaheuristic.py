from pyMetaheuristic.algorithm import genetic_algorithm
import math
import numpy as np
from pyMetaheuristic.utils import graphs
import time
import timeit

result = []


def sphere(xx):
    sum_val = sum(x**2 for x in xx)
    y = sum_val
    return (y)


parameters = {
    'population_size': 300,
    'min_values': (-10, -10),
    'max_values': (10, 10),
    'generations': 500,
    'mutation_rate': 0.01,
    'elite': 0,
    'eta': 0,
    'mu': 1,
    'verbose': True,
    'start_init': None,
    'target_value': None
}

# ga = genetic_algorithm(target_function=sphere, **parameters)

# GRAFICO PLOTAGEM
# plot_parameters = {
#     'min_values': (-5, -5),
#     'max_values': (5, 5),
#     'step': (0.1, 0.1),
#     'solution': [],
#     'proj_view': '3D',
#     'view': 'notebook'
# }

# graphs.plot_single_function(target_function = sphere, **plot_parameters)

for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    ga = genetic_algorithm(target_function=sphere, **parameters)
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    print('Melhor solução: ', ga[-1])

    result.append({
        'Metodo': 'GA PYMETAHEURISTIC',
        'valor final X': ga[-1],
        'valor final F': ga[:-1],
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

for x in result:
    print(x)

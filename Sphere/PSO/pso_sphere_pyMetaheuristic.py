import math
import time
import timeit
from pyMetaheuristic.algorithm import particle_swarm_optimization
from pyMetaheuristic.utils import graphs
import numpy as np
import pandas as pd

result = []


def sphere(xx):
    sum_val = sum(x**2 for x in xx)
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
# graphs.plot_single_function(target_function = sphere, **plot_parameters)

# pso = particle_swarm_optimization(target_function=sphere, **parameters)

# print('Melhor solução: ', pso[-1])

for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    pso = particle_swarm_optimization(target_function=sphere, **parameters)
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    result.append({
        'Metodo': 'PSO PYMETAHEURISTIC',
        'Fitness': pso[-1],
        'valor final F': pso[:-1],
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

# Calculate the average fitness and execution times
average_fitness = np.mean([x['Fitness'] for x in result])
average_execution_time = np.mean([x['Tempo execução'] for x in result])
average_cpu_time = np.mean([x['Tempo execução - CPU'] for x in result])

# Append the averages to the result list
result.append({
    'Metodo': 'PSO PYMETAHEURISTIC',
    'Media Fitness': average_fitness,
    'Media Tempo execução': average_execution_time,
    'Media Tempo CPU': average_cpu_time,
})

for x in result:
    print(x)
try:
    existing_df = pd.read_excel('resultados_Sphere.xlsx')
    df = pd.concat([existing_df, pd.DataFrame(result)], ignore_index=True)
except FileNotFoundError:
    df = pd.DataFrame(result)

df[['Metodo', 'Rodada', 'Fitness',
    'Tempo execução', 'Tempo execução - CPU', 'Media Fitness', 'Media Tempo CPU', 'Media Tempo execução']].to_excel('resultados_Sphere.xlsx', index=False)

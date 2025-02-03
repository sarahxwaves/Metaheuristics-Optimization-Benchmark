import numpy as np
from pyMetaheuristic.algorithm import simulated_annealing
from pyMetaheuristic.utils import graphs
import math
import time
import timeit
import pandas as pd

result = []


def sphere(xx):
    sum_val = sum(x**2 for x in xx)
    y = sum_val
    return (y)


parameters = {
    'min_values': (-5, -5),
    'max_values': (5, 5),
    'alpha': 0.9,
    'mu': 0,
    'sigma': 1,
    'temperature_iterations': 500,
    'initial_temperature': 100,
    'final_temperature': 0.1,
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

sa = simulated_annealing(target_function=sphere, **parameters)

for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    sa = simulated_annealing(target_function=sphere, **parameters)
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    result.append({
        'Metodo': 'SA PYMETAHEURISTIC',
        'Fitness': sa[-1],
        'valor final F': sa[:-1],
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

average_fitness = np.mean([x['Fitness'] for x in result])
average_execution_time = np.mean([x['Tempo execução'] for x in result])
average_cpu_time = np.mean([x['Tempo execução - CPU'] for x in result])

result.append({
    'Metodo': 'SA PYMETAHEURISTIC',
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

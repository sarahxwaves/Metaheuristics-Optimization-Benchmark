import numpy as np
from mealpy import FloatVar, SA
import math
import time
import timeit
import pandas as pd


def sphere(xx):
    sum_val = sum(x**2 for x in xx)
    y = sum_val
    return (y)


problem_dict = {
    "bounds": FloatVar(lb=(-10.,) * 10, ub=(10.,) * 10, name="delta"),
    "minmax": "min",
    "obj_func": sphere
}


# model = SA.GaussianSA(epoch=1000, pop_size=2,
#                       temp_init=100, cooling_rate=0.99, scale=0.1)
# g_best = model.solve(problem_dict)
# print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

result = []
for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    model = SA.GaussianSA(epoch=800, pop_size=200,
                          temp_init=100, cooling_rate=0.99, scale=0.1)
    g_best = model.solve(problem_dict)
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    result.append({
        'Metodo': 'SA MEALPY',
        'valor final X': g_best.solution,
        'Fitness': g_best.target.fitness,
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
    'Metodo': 'SA MEALPY',
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

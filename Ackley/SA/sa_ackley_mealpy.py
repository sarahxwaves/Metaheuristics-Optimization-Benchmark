import numpy as np
from mealpy import FloatVar, SA
import math
import time
import timeit
import pandas as pd


def ackley(xx):
    a = 10
    b = 0.2
    c = 2*math.pi
    d = len(xx)
    sum1 = np.sum(np.square(xx))
    sum2 = np.sum(np.cos(c*xx))
    term1 = -a * math.exp(-b*math.sqrt(sum1/d))
    term2 = -math.exp(sum2/d)
    y = term1 + term2 + a + math.exp(1)
    return (y)


problem_dict = {
    "bounds": FloatVar(lb=(-10.,) * 10, ub=(10.,) * 10, name="delta"),
    "minmax": "min",
    "obj_func": ackley
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
    model = SA.GaussianSA(epoch=500, pop_size=200,
                          temp_init=80, cooling_rate=0.8, scale=0.1)
    g_best = model.solve(problem_dict)
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    result.append({
        'Metodo': 'SIMULATED ANNEALING MEALPY',
        'valor final X': g_best.solution,
        'Fitness': g_best.target.fitness,
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

average_fitness = np.mean([x['Fitness'] for x in result])
average_execution_time = np.mean([x['Tempo execução'] for x in result])
average_cpu_time = np.mean([x['Tempo execução - CPU'] for x in result])

# result.append({
#     'Metodo': 'SIMULATED ANNEALING MEALPY',
#     'Media Fitness': average_fitness,
#     'Media Tempo execução': average_execution_time,
#     'Media Tempo CPU': average_cpu_time,
# })

for x in result:
    print(x)
# try:
#     existing_df = pd.read_excel('resultados_Ackley.xlsx')
#     df = pd.concat([existing_df, pd.DataFrame(result)], ignore_index=True)
# except FileNotFoundError:
#     df = pd.DataFrame(result)

# df[['Metodo', 'Rodada', 'Fitness',
#     'Tempo execução', 'Tempo execução - CPU', 'Media Fitness', 'Media Tempo CPU', 'Media Tempo execução']].to_excel('resultados_Ackley.xlsx', index=False)

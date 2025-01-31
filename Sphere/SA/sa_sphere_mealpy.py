import numpy as np
from mealpy import FloatVar, SA
import math
import time
import timeit


def sphere(xx):
    sum_val = sum(x**2 for x in xx)
    y = sum_val
    return (y)


problem_dict = {
    "bounds": FloatVar(lb=(-10.,) * 30, ub=(10.,) * 30, name="delta"),
    "minmax": "min",
    "obj_func": sphere
}


model = SA.GaussianSA(epoch=1000, pop_size=2,
                      temp_init=100, cooling_rate=0.99, scale=0.1)
g_best = model.solve(problem_dict)
print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

# result = []
# for x in range(10):
#   tempo_cpu_inicio = time.process_time()
#   tempo_inicio = timeit.default_timer()
#   inicio = time.time()
#   model = SA.GaussianSA(epoch=1000, pop_size=2, temp_init = 100, cooling_rate = 0.99, scale = 0.1)
#   g_best = model.solve(problem_dict)
#   fim = time.time()
#   tempo_fim = timeit.default_timer()
#   tempo_cpu_fim = time.process_time()

#   result.append({
#     'Metodo': 'SIMULATED ANNEALING MEALPY',
#     'valor final X': g_best.solution,
#     'Rodada': x+1,
#     'tempo de execução(s)': tempo_fim - tempo_inicio,
#     'tempo de execução - CPU(s)': tempo_cpu_fim - tempo_cpu_inicio,
# })

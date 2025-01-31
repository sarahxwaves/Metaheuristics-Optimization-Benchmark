import numpy as np
from mealpy import FloatVar, GA
import math
import time
import timeit

result = []


def sphere(xx):
    sum_val = sum(x**2 for x in xx)
    y = sum_val
    return (y)


problem_dict = {
    "bounds": FloatVar(lb=(-10.,) * 10, ub=(10.,) * 10, name="delta"),
    "obj_func": sphere,
    "minmax": "min",
}

model = GA.BaseGA(epoch=1000, pop_size=400, pc=0.8, pm=0.05)
g_best = model.solve(problem_dict)
print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

# for x in range(10):
#     tempo_cpu_inicio = time.process_time()
#     tempo_inicio = timeit.default_timer()
#     inicio = time.time()
#     model = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05)
#     g_best = model.solve(problem_dict)
#     fim = time.time()
#     tempo_fim = timeit.default_timer()
#     tempo_cpu_fim = time.process_time()

#     result.append({
#         'Metodo': 'GA MEALPY',
#         'valor final X': g_best.solution,
#         'Rodada': x+1,
#         'tempo de execução(s)': tempo_fim - tempo_inicio,
#         'tempo de execução - CPU(s)': tempo_cpu_fim - tempo_cpu_inicio,
#     })

# for x in result:
#   print(x)

import numpy as np
from mealpy import FloatVar, PSO
import math
import time
import timeit

result = []


def rosen(xx):
    d = len(xx)
    xi = xx[0:(d-1)]
    xnext = xx[1:d]
    sum_val = sum(100*(xnext_i - xi_i**2)**2 + (xi_i - 1)
                  ** 2 for xi_i, xnext_i in zip(xi, xnext))
    y = sum_val
    return (y)


problem_dict = {
    "bounds": FloatVar(lb=(-10.,) * 10, ub=(10.,) * 10, name="delta"),
    "obj_func": rosen,
    "minmax": "min",
}

# model = PSO.AIW_PSO(epoch=500, pop_size=200, c1=1.05, c2=2.05, alpha=0.8)
# g_best = model.solve(problem_dict)
# print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    model = PSO.AIW_PSO(epoch=500, pop_size=50, c1=1.05, c2=1.00, alpha=0.7)
    g_best = model.solve(problem_dict)
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    result.append({
        'Metodo': 'PSO MEALPY',
        'valor final X': g_best.solution,
        'fitness': g_best.target.fitness,
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

for x in result:
    print(x)

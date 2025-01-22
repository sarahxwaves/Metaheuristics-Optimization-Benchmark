import numpy as np
from mealpy import FloatVar, GA
import math
import time
import timeit

result = []

def ackley(xx):
    a=20
    b=0.2
    c=2*math.pi
    d = len(xx)

    sum1 = np.sum(np.square(xx))
    sum2 = np.sum(np.cos(c*xx))

    term1 = -a * math.exp(-b*math.sqrt(sum1/d))
    term2 = -math.exp(sum2/d)

    y = term1 + term2 + a + math.exp(1)
    return(y)

problem_dict = {
    "bounds": FloatVar(lb=(-10.,) * 30, ub=(10.,) * 30, name="delta"),
    "obj_func": ackley,
    "minmax": "min",
}

model = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05)
g_best = model.solve(problem_dict)
print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

# model2 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, selection="tournament", k_way=0.4, crossover="multi_points")

# model3 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, crossover="one_point", mutation="scramble")

# model4 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, crossover="arithmetic", mutation_multipoints=True, mutation="swap")

# model5 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, selection="roulette", crossover="multi_points")

# model6 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, selection="random", mutation="inversion")

# model7 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, crossover="arithmetic", mutation="flip")

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
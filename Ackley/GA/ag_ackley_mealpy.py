import numpy as np
from mealpy import FloatVar, GA
import math
import time
import timeit

result = []


def ackley(xx):
    a = 20
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
    "obj_func": ackley,
    "minmax": "min",
}

# Increase the number of generations (epochs) and population size for better exploration
# model = GA.BaseGA(epoch=1000, pop_size=400, pc=0.8, pm=0.05)
# g_best = model.solve(problem_dict)
# print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

# You can also experiment with different selection, crossover, and mutation strategies
# model = GA.BaseGA(epoch=2000, pop_size=100, pc=0.9, pm=0.05, selection="tournament", crossover="multi_points", mutation="scramble")
# g_best = model.solve(problem_dict)
# print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")

# model2 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, selection="tournament", k_way=0.4, crossover="multi_points")

# model4 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, crossover="arithmetic", mutation_multipoints=True, mutation="swap")

# model5 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, selection="roulette", crossover="multi_points")

# model7 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, crossover="arithmetic", mutation="flip")

for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    model = GA.BaseGA(epoch=500, pop_size=200, pc=0.9, pm=0.05)
    g_best = model.solve(problem_dict)
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    result.append({
        'Metodo': 'GA MEALPY',
        'valor final X': g_best.solution,
        'fitness': g_best.target.fitness,
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

for x in result:
    print(x)

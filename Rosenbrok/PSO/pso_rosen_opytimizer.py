import math
import time
import timeit
import numpy as np
from opytimizer import Opytimizer
from opytimizer.core import Function
from opytimizer.optimizers.swarm import PSO
from opytimizer.spaces import SearchSpace

n_agents = 20
n_variables = 10
lower_bound = [-10] * n_variables
upper_bound = [10] * n_variables
result = []


def rosen(xx):
    d = len(xx)
    xi = xx[0:(d-1)]
    xnext = xx[1:d]

    sum_val = sum(100*(xnext_i - xi_i**2)**2 + (xi_i - 1)
                  ** 2 for xi_i, xnext_i in zip(xi, xnext))

    y = sum_val
    return float(y)


space = SearchSpace(n_agents, n_variables, lower_bound, upper_bound)
optimizer = PSO()
function = Function(rosen)

optimizer.w = 0.4
optimizer.c1 = 5.00
optimizer.c2 = 1.05

# opt = Opytimizer(space, optimizer, function)
# opt.start(n_iterations=1000)

# best_agent = opt.space.best_agent

# print(f"Melhor posição: {best_agent.position}")
# print(f"Melhor valor da função objetivo: {best_agent.fit}")

for x in range(10):

    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()

    opt = Opytimizer(space, optimizer, function)
    space = SearchSpace(n_agents, n_variables, lower_bound, upper_bound)
    opt.start(n_iterations=500)
    best_agent = opt.space.best_agent
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    result.append({
        'Metodo': 'PSO OPYTIMIZER',
        'valor final X': best_agent.position,
        'valor final F': best_agent.fit,
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

for x in result:
    print(x)

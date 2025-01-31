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


def sphere(xx):
    sum_val = sum(x**2 for x in xx)
    y = sum_val
    return float(y)


space = SearchSpace(n_agents, n_variables, lower_bound, upper_bound)
optimizer = PSO()
function = Function(sphere)

optimizer.w = 0.4
optimizer.c1 = 5.00
optimizer.c2 = 1.05

opt = Opytimizer(space, optimizer, function)
opt.start(n_iterations=1000)

# Obtém o melhor agente
best_agent = opt.space.best_agent

# Imprime a posição e o valor da função objetivo do melhor agente
print(f"Melhor posição: {best_agent.position}")
print(f"Melhor valor da função objetivo: {best_agent.fit}")

# for x in range(10):
#     optimizer = PSO()
#     function = Function(sphere)

#     tempo_cpu_inicio = time.process_time()
#     tempo_inicio = timeit.default_timer()
#     inicio = time.time()

#     opt = Opytimizer(space, optimizer, function)
#     space = SearchSpace(n_agents, n_variables, lower_bound, upper_bound)
#     opt.start(n_iterations=1000)

#     fim = time.time()
#     tempo_fim = timeit.default_timer()
#     tempo_cpu_fim = time.process_time()

#     result.append({
#   'Metodo': 'PSO OPYTIMIZER',
#   'valor final X': best_agent.position,
#   'valor final F': best_agent.fit,
#   'Rodada': x+1,
#   'tempo de execução(s)': tempo_fim - tempo_inicio,
#   'tempo de execução - CPU(s)': tempo_cpu_fim - tempo_cpu_inicio,
#    })

# for x in result:
#   print(x)

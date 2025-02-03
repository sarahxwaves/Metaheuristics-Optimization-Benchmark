import math
import numpy as np
import time
import timeit

from opytimizer import Opytimizer
from opytimizer.core import Function
from opytimizer.optimizers.science import SA
from opytimizer.spaces import SearchSpace

n_agents = 20
n_variables = 2
lower_bound = [-5, -5]
upper_bound = [5, 5]
result = []


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


space = SearchSpace(n_agents, n_variables, lower_bound, upper_bound)
optimizer = SA()
function = Function(ackley)

# opt = Opytimizer(space, optimizer, function)
# opt.start(n_iterations=500)

# best_agent = opt.space.best_agent

# # Imprime a posição e o valor da função objetivo do melhor agente
# print(f"Melhor posição: {best_agent.position}")
# print(f"Melhor valor da função objetivo: {best_agent.fit}")

for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    space = SearchSpace(n_agents, n_variables, lower_bound, upper_bound)
    optimizer = SA()
    function = Function(ackley)
    opt = Opytimizer(space, optimizer, function)
    opt.start(n_iterations=500)
    best_agent = opt.space.best_agent
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    result.append({
        'Metodo': 'SIMULATED ANNEALING OPYTIMIZER',
        'valor final X': best_agent.position,
        'valor final F': best_agent.fit,
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

for x in result:
    print(x)

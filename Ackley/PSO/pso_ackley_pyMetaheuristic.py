import math
import time
import timeit
from pyMetaheuristic.algorithm import particle_swarm_optimization
from pyMetaheuristic.utils import graphs
import numpy as np

result = []


def ackley(variables_values=[0.0]):
    xx = np.array(variables_values)
    a = 20
    b = 0.2
    c = 2*math.pi
    d = len(xx)
    sum1 = np.sum(np.square(xx))
    sum2 = np.sum(np.cos(c*xx))
    term1 = -a * math.exp(-b*math.sqrt(sum1/d))
    term2 = -math.exp(sum2/d)
    func_value = term1 + term2 + a + math.exp(1)
    return (func_value)


parameters = {
    'swarm_size': 250,
    'min_values': (-5, -5),
    'max_values': (5, 5),
    'iterations': 1000,
    'decay': 0,
    'w': 0.9,
    'c1': 2,
    'c2': 2,
    'verbose': True,
    'start_init': None,
    'target_value': None
}

# plot_parameters = {
#     'min_values': (-5, -5),
#     'max_values': (5, 5),
#     'step': (0.1, 0.1),
#     'solution': [],
#     'proj_view': '3D',
#     'view': 'notebook'
# }
# graphs.plot_single_function(target_function = ackley, **plot_parameters)

pso = particle_swarm_optimization(target_function=ackley, **parameters)

print('Melhor solução: ', pso[-1])

# for x in range(10):
#     tempo_cpu_inicio = time.process_time()
#     tempo_inicio = timeit.default_timer()
#     inicio = time.time()
#     pso = particle_swarm_optimization(target_function = ackley, **parameters)
#     fim = time.time()
#     tempo_fim = timeit.default_timer()
#     tempo_cpu_fim = time.process_time()

#     result.append({
#     'Metodo': 'PSO PYMETAHEURISTIC',
#     'valor final X': pso[ -1],
#     'valor final F': pso[:-1],
#     'Rodada': x+1,
#     'tempo de execução(s)': tempo_fim - tempo_inicio,
#     'tempo de execução - CPU(s)': tempo_cpu_fim - tempo_cpu_inicio,
#     })

# for x in result:
#   print(x)

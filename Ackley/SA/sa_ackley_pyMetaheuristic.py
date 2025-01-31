import numpy as np
from pyMetaheuristic.algorithm import simulated_annealing
from pyMetaheuristic.utils import graphs
import math


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
    'min_values': (-5, -5),
    'max_values': (5, 5),
    'alpha': 0.9,
    'mu': 0,
    'sigma': 1,
    'temperature_iterations': 1000,
    'initial_temperature': 1.0,
    'final_temperature': 0.0001,
    'verbose': True,
    'start_init': None,
    'target_value': None
}

plot_parameters = {
    'min_values': (-5, -5),
    'max_values': (5, 5),
    'step': (0.1, 0.1),
    'solution': [],
    'proj_view': '3D',
    'view': 'notebook'
}
# graphs.plot_single_function(target_function = ackley, **plot_parameters)

sa = simulated_annealing(target_function=ackley, **parameters)

# for x in range(10):
#     tempo_cpu_inicio = time.process_time()
#     tempo_inicio = timeit.default_timer()
#     inicio = time.time()
#     sa = particle_swarm_optimization(target_function = ackley, **parameters)
#     fim = time.time()
#     tempo_fim = timeit.default_timer()
#     tempo_cpu_fim = time.process_time()

#     result.append({
#     'Metodo': 'SA PYMETAHEURISTIC',
#     'valor final X': sa[ -1],
#     'valor final F': sa[:-1],
#     'Rodada': x+1,
#     'tempo de execução(s)': tempo_fim - tempo_inicio,
#     'tempo de execução - CPU(s)': tempo_cpu_fim - tempo_cpu_inicio,
#     })

# for x in result:
#   print(x)

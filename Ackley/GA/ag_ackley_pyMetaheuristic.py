from pyMetaheuristic.algorithm import genetic_algorithm
import math
import numpy as np
from pyMetaheuristic.utils import graphs
import time
import timeit

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
    'population_size': 200,
    'min_values': (-5, -5),
    'max_values': (5, 5),
    'generations': 500,
    'mutation_rate': 0.005,
    'elite': 0,
    'verbose': True,
    'start_init': None,
    'target_value': None
}

# ga = genetic_algorithm(target_function=ackley, **parameters)

# GRAFICO PLOTAGEM
# plot_parameters = {
#     'min_values': (-5, -5),
#     'max_values': (5, 5),
#     'step': (0.1, 0.1),
#     'solution': [],
#     'proj_view': '3D',
#     'view': 'notebook'
# }

# graphs.plot_single_function(target_function = ackley, **plot_parameters)

for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    ga = genetic_algorithm(target_function=ackley, **parameters)
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    # print('Melhor solução: ', ga[-1])

    result.append({
        'Metodo': 'GA PYMETAHEURISTIC',
        'valor final X': ga[-1],
        'fitness': ga[:-1],
        'Rodada': x+1,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })

for x in result:
    print(x)

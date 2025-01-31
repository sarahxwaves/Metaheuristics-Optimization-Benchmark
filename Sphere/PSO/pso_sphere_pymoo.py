from pymoo.algorithms.soo.nonconvex.pso import PSO
from pymoo.problems import get_problem
from pymoo.optimize import minimize
import numpy as np
import time
import timeit

problem = get_problem("ackley", n_var=10, a=20, b=1/5, c=2 * np.pi)
algorithm = PSO(pop_size=200)

res = minimize(problem,
    algorithm,
    ('n_gen', 500),
    seed=1,
    verbose=True)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))


#LOOP 10X E MÉTRICAS TEMPO
# result = []

# for x in range(10):
#   problem = get_problem("ackley", n_var=10, a=20, b=1/5, c=2 * np.pi)
#   algorithm = PSO(pop_size=200, eliminate_duplicates=True)
#   tempo_cpu_inicio = time.process_time()
#   tempo_inicio = timeit.default_timer()
#   inicio = time.time()
#   res = minimize(problem,
#     algorithm,
#     ('n_gen', 500),
#     seed=1,
#     verbose=True)
#   fim = time.time()
#   tempo_fim = timeit.default_timer()
#   tempo_cpu_fim = time.process_time()

#   result.append({
#   'Metodo': 'PSO PYMOO',
#   'valor final X': res.X,
#   'valor final F': res.F,
#   'Rodada': x+1,
#   'success': res.success,
#   'tempo de execução(s)': tempo_fim - tempo_inicio,
#   'tempo de execução - CPU(s)': tempo_cpu_fim - tempo_cpu_inicio,
# })
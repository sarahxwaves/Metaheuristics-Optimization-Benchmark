from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.problems import get_problem
from pymoo.optimize import minimize
import numpy as np

problem = get_problem("rosenbrock", n_var=10)
algorithm = GA(pop_size=200, eliminate_duplicates=True)

res = minimize(problem,
               algorithm,
               ('n_gen', 500),
               seed=1,
               verbose=True)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))

result = []

# for x in range(10):
#   problem = get_problem("ackley", n_var=10, a=20, b=1/5, c=2 * np.pi)
#   algorithm = GA(pop_size=200, eliminate_duplicates=True,
#                   # save_history=True
#                   )
#   tempo_cpu_inicio = time.process_time()
#   tempo_inicio = timeit.default_timer()
#   inicio = time.time()
#   res = minimize(problem,
#     algorithm,
#     ('n_gen', 500),
#     seed=1,
#     verbose=True)
#   tempo_fim = timeit.default_timer()
#   tempo_cpu_fim = time.process_time()
#   fim = time.time()

#   n_evals = np.array([e.evaluator.n_eval for e in res.history])

#   opt = np.array([e.opt[0].F for e in res.history])

#   result.append({
#     # 'evals': opt,
#     'Metodo': 'GA PYMOO',
#     'valor final X': res.X,
#     'valor final F': res.F,
#     'Rodada': x+1,
#     'success': res.success,
#     'tempo de execução(s)': tempo_fim - tempo_inicio,
#     'tempo de execução - CPU(s)': tempo_cpu_fim - tempo_cpu_inicio
#   })

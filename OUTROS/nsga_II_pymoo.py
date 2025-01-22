from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.optimize import minimize
import numpy as np
import time

problem = get_problem("ackley", n_var=10, a=20, b=1/5, c=2 * np.pi)
algorithm = NSGA2(pop_size=200)
result = []


for x in range(10):
  inicio = time.time()
  res = minimize(problem,
    algorithm,
    ('n_gen', 500),
    seed=1,
    verbose=True)
  fim = time.time()

for x in result:
  print(x)
  print("\n")
  result.append({
    'valor final X': res.X,
    'valor final F': res.F,
    'tempo de execução': (fim - inicio)

  })


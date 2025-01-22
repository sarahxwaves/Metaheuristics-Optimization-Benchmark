from pymoo.algorithms.soo.nonconvex.es import ES
from pymoo.problems import get_problem
from pymoo.optimize import minimize
import numpy as np

problem = get_problem("ackley", n_var=10, a=20, b=1/5, c=2 * np.pi)
algorithm = ES(n_offsprings=200, rule=1.0 / 7.0)

res = minimize(problem,
    algorithm,
    ('n_gen', 500),
    seed=1,
    verbose=True)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))
from pymoo.algorithms.soo.nonconvex.de import DE
from pymoo.operators.sampling.lhs import LHS
from pymoo.problems import get_problem
from pymoo.optimize import minimize
import numpy as np

problem = get_problem("ackley", n_var=10, a=20, b=1/5, c=2 * np.pi)
algorithm = DE(pop_size=200, sampling=LHS(), variant="DE/rand/1/bin", CR=0.3, dither="vector", jitter=False)

res = minimize(problem,
    algorithm,
    ('n_gen', 500),
    seed=1,
    verbose=True)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))
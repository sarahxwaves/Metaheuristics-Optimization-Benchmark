from pymoo.problems import get_problem
import time
import timeit
from simanneal import Annealer
import math
import numpy as np

result = []
for x in range(10):
    problem = get_problem("ackley", n_var=10, a=20, b=1/5, c=2 * np.pi)
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()

    class AckleyOptimization(Annealer):

        def move(self):
            """This function defines how the state should be altered."""
            # Vary each parameter by up to +/- 10% of its current value.
            self.state = [x + (np.random.rand() - 0.5) * 0.2 * x for x in self.state]

        def energy(self):
            """This function calculates the energy of the current state."""
            xx = np.array(self.state)
            a = 20
            b = 0.2
            c = 2*math.pi
            d = len(xx)

            sum1 = np.sum(np.square(xx))
            sum2 = np.sum(np.cos(c*xx))

            term1 = -a * math.exp(-b*math.sqrt(sum1/d))
            term2 = -math.exp(sum2/d)

            func_value = term1 + term2 + a + math.exp(1)
            return(func_value)

    # Initial guess
    init_state = [5, 5]

    # Create annealer object
    ackley_problem = AckleyOptimization(init_state)

    ackley_problem.steps = 50000
    ackley_problem.updates = 5000 
    ackley_problem.Tmax = 20.0
    ackley_problem.Tmin = 1.0  # Reduz a temperatura final

    # Perform simulated annealing
    best_state, best_energy = ackley_problem.anneal()
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()

    print("Best solution found: \nX = %s\nF = %s" % (best_state, best_energy))
#     result.append({
#         'Metodo': 'SA SIMANNEAL',
#         'Rodada': x+1,
#         'tempo de execução(s)': tempo_fim - tempo_inicio,
#         'tempo de execução - CPU(s)': tempo_cpu_fim - tempo_cpu_inicio,
#     })

# for x in result:
#     print(x)

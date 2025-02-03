from pyswarms.single.global_best import GlobalBestPSO
import time
import timeit
import numpy as np

result = []
for x in range(10):
    tempo_cpu_inicio = time.process_time()
    tempo_inicio = timeit.default_timer()
    inicio = time.time()
    x_max = 10 * np.ones(2)
    x_min = -1 * x_max
    bounds = (x_min, x_max)
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    optimizer = GlobalBestPSO(n_particles=10, dimensions=10, options=options)

    def ackley(xx, a=20, b=0.2, c=2*np.pi):
        d = len(xx)
        sum1 = np.sum(np.square(xx))
        sum2 = np.sum(np.cos(c*xx))
        term1 = -a * np.exp(-b*np.sqrt(sum1/d))
        term2 = -np.exp(sum2/d)
        y = term1 + term2 + a + np.exp(1)
        return y

    def print_iteration(iteration, cost, pos):
        print(f"Iteration: {iteration}, Cost: {cost}, Position: {pos}")

    # now run the optimization, pass a=1 and b=100 as a tuple assigned to args
    cost, pos = optimizer.optimize(
        ackley, 5000, a=20, b=1/5, c=2 * np.pi, verbose=True)
 # Imprime a melhor solução encontrada
    fim = time.time()
    tempo_fim = timeit.default_timer()
    tempo_cpu_fim = time.process_time()
    result.append({
        'Metodo': 'PSO PYSWARM',
        # 'valor final X': res.X,
        # 'valor final F': res.F,
        'Rodada': x+1,
        # 'success': res.success,
        'Tempo execução': tempo_fim - tempo_inicio,
        'Tempo execução - CPU': tempo_cpu_fim - tempo_cpu_inicio,
    })


for x in result:
    print(x)

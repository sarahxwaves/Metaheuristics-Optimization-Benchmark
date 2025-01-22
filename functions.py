import numpy as np
import math

def ackleyForpyMetaheuristic(variables_values = [0.0]):
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
    return(func_value)

def ackley(xx, a=20, b=0.2, c=2*math.pi):
    d = len(xx)

    sum1 = np.sum(np.square(xx))
    sum2 = np.sum(np.cos(c*xx))

    term1 = -a * math.exp(-b*math.sqrt(sum1/d))
    term2 = -math.exp(sum2/d)

    y = term1 + term2 + a + math.exp(1)
    return(y)
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from collections.abc import Callable


def solve_ode(t, y):
    yder = np.zeros(1)
    yder[0] = math.pow(math.e, t*math.sin(y[0]) )
    return yder

t_span = [0, 3]
y0 = [0]
sol = solve_ivp(solve_ode, t_span, y0)
plt.plot(sol.t, sol.y[0], "o-r")
plt.show()

"""
Calculates y(t) given y(0), step-size, terminating t-value, and y'
fun = y'(t)
"""
def heuns(fun: Callable[float, float], h: float, t_end: float, y0: float):
    # Init conditions
    t = 0.0
    y_prev = y0
    solution = [(t, y_prev)]
    while(t <= t_end):
        k1: float = fun(t, y_prev)
        k2: float = fun(t + h, y_prev + h * k1)
        t = t + h
        y_next: float = y_prev + (h / 2) * (k1 + k2)
        solution.append((t, y_next))
        y_prev = y_next
    return solution

def funny(t: float, y: float):
    return t - y

print(heuns(funny, 0.1, 0.2, 1))

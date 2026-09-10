import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def solve_ode(t, y):
    yder = np.zeros(2)
    yder[0] = math.e ** t*math.sin(y[t])
    return yder

t_span = [0, 3]
y0 = [0, 0]
sol = solve_ivp(solve_ode, t_span, y0)
plt.plot(sol.t, sol.y, "o-r")
plt.show()

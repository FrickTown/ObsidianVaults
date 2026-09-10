import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def solve_ode(t, y):
    yder = np.zeros(1)
    yder[0] = math.pow(math.e, t*math.sin(y[0]) )
    return yder

t_span = [0, 3]
y0 = [0]
sol = solve_ivp(solve_ode, t_span, y0)
plt.plot(sol.t, sol.y[0], "o-r")
plt.show()

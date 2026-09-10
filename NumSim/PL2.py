import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from collections.abc import Callable

def question_1():
    def solve_ode(t, y):
        yder = np.zeros(1)
        yder[0] = math.pow(math.e, t * math.sin(y[0]) )
        return yder
    t_span = [0, 3]
    y0 = [0]
    sol = solve_ivp(solve_ode, t_span, y0)
    plt.plot(sol.t, sol.y[0], "o-r")
    plt.show()

"""
Calculates y(t) given y(0), step-size, terminating t-value, and y'
fun = y'(t) = f(t, y)
"""
def heuns(fun: Callable[float, float], h: float, t_end: float, y0: float):
    # Init conditions
    t = 0.0
    y_prev = y0
    solution = [(t, y_prev)] # Include t0 position
    while(t <= t_end):
        k1: float = fun(t, y_prev)
        k2: float = fun(t + h, y_prev + h * k1)
        t = t + h
        # Calculate and store t[i+h]
        y_next: float = y_prev + (h / 2) * (k1 + k2)
        solution.append((t, y_next))
        y_prev = y_next
    return solution

def question_2():
    def given_func(t: float, y: float):
        return math.pow(math.e, t * math.sin(y))

    h = 0.5
    end = 3
    y0 = 0
    print(heuns(given_func, h, end, y0))

def question_3():
    # y'''(t) + sin(t) * y(t) * y''(t) + y(t) - t = 0
    # y'''(t) = -sin(t) * y(t) * y''(t) - y(t) + t
    # y(0) = 0, y'(0) = 0, y''(0) = 5
    def solve_ode(t: float, y: list[float]):
        yder = np.zeros(3)
        yder[0] = y[1]
        yder[1] = y[2]
        yder[2] = (-math.sin(t) * y[0] * y[2]) - (y[0] + t)
        return yder

    y0 = [0, 0, 5]
    t_span = [0, 4]
    sol = solve_ivp(solve_ode, t_span, y0)
    plt.plot(sol.t, sol.y[0], "o-r", color="red", label="y(t)")
    plt.plot(sol.t, sol.y[1], "*-r", color="purple", label="y'(t)")
    plt.plot(sol.t, sol.y[2], "X-r", color="blue", label="y''(t)")
    plt.legend()
    plt.show()

def question_4():
    class ode_solution:
        t: list[float]
        y: list[list[float]]
        def __init__(self):
            self.t = []
            self.y = []

    def custom_ode_solver(fun: Callable[[float, list[float]], float], h: float, t_span: list[float], y0: list[float]):
        yi = y0[]
        ti = t_span[0]
        solution = ode_solution()
        while(ti <= t_span[1]):
            k1 = fun(ti, yi)
            k2 = fun(ti + (h / 2), yi + (h / 2) * k1)
            k3 = fun(ti + h, yi - (h * k1) + (2 * h * k2))
            k  = (k1 + (4 * k2) + k3) / 6
            yi_1 = yi + (h * k)

def main():
    #question_1()
    #question_2()
    #question_3()
    question_4()

if __name__ == "__main__":
    main()

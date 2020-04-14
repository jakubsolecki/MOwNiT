import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import scipy.integrate as integrate
from lab6.zad_1 import rectangle_rule, trapezoidal_rule, simpson_rule


def to_chart(fun, a, b, n, func_name):
    x_axis = np.linspace(a, b, n)
    plt.plot(x_axis, np.vectorize(fun)(x_axis), label=func_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(func_name)
    plt.show()


def calc_integral(fun, a, b, n, func_name):
    to_chart(fun, a, b, n, func_name)
    rect = rectangle_rule(fun, a, b, n)
    trap = trapezoidal_rule(fun, a, b, n)
    simp = simpson_rule(fun, a, b, n)
    base_val = integrate.quad(fun, a, b)[0]  # used as a reference value of an integral
    if base_val == 0:
        rect_rel_err = "Undefined"
        trap_rel_err = "Undefined"
        simp_rel_err = "Undefined"
    else:
        rect_rel_err = (abs(rect - base_val) / base_val)*100
        trap_rel_err = (abs(trap - base_val) / base_val)*100
        simp_rel_err = (abs(simp - base_val) / base_val)*100

    table = [["Quad integral (SciPy)", base_val, 0, 0],
             ["Rectangular rule", rect, rect_rel_err, abs(rect - base_val)],
             ["Trapezoidal rule", trap, trap_rel_err, abs(trap - base_val)],
             ["Simpson's rule", simp, simp_rel_err, abs(simp - base_val)]]
    print(tabulate(table, headers=["Integration method", "Value of the definite integral", "Relative error [%]",
                                   "Absolute error"], tablefmt="grid", floatfmt=".10f"))


def integral_comparison(a, b, n):
    calc_integral(lambda x: x, a, b, n, "x")
    calc_integral(lambda x: 2*x**2, a, b, n, "2*x^2")
    calc_integral(lambda x: 4*np.sin(x), a, b, n, "4*sin(x)")
    calc_integral(lambda x: np.exp(x), a, b, n, "e^x")
    calc_integral(lambda x: x*np.sin(x) ** 2 + 2*np.cos(x), a, b, n, "x*sin^2(x) + 2*cos(x)")
    calc_integral(lambda x: np.cos((x + 1) / (x**2 + 0.04)) * np.exp(x), a, b, n, "cos((x+1)/(x^2 + 0.04))*e^x")


integral_comparison(-2, 3, 5)
integral_comparison(-2, 3, 10)
integral_comparison(-2, 3, 50)
integral_comparison(-2, 3, 1000)
integral_comparison(0, 10, 5)
integral_comparison(0, 10, 10)
integral_comparison(0, 10, 50)
integral_comparison(0, 10, 1000)
integral_comparison(-10, 15, 5)
integral_comparison(-10, 15, 10)
integral_comparison(-10, 15, 50)
integral_comparison(-10, 15, 1000)
integral_comparison(0, 50, 5)
integral_comparison(0, 50, 10)
integral_comparison(0, 50, 50)
integral_comparison(0, 50, 1000)

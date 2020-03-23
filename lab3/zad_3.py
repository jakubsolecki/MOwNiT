import sympy as sp
import numpy as np
from tabulate import tabulate
import math
from zad_1 import to_table
import matplotlib.pyplot as plt


def lagrange_interpolation(x_values, y_values, x):
    if len(x_values) != len(y_values):
        exit("There must be exact same number of x and y values")
        return -1
    y = 0
    for k in range(len(x_values)):
        i = 1
        for j in range(len(x_values)):
            if j != k:
                i = i * ((x - x_values[j]) / (x_values[k] - x_values[j]))
        y += i * y_values[k]
    return sp.simplify(y)


def to_chart(min, max, number_of_points, fun1, fun2, fun_name):
    x_axis = []
    f1_values = []
    f2_values = []
    step = (max - min) / number_of_points
    for x in np.arange(min, max+step, step):
        x_axis.append(x)
        f1_values.append(fun1(x))
        f2_values.append(fun2(x))

    plt.plot(x_axis, f1_values, label=fun_name)
    plt.plot(x_axis, f2_values, label="Interpolated "+fun_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Comparison of "+fun_name+" and its Lagrange interpolation")
    plt.legend()
    plt.show()


def cmp_inbetween_points(min, max, number_of_points, fun1, fun2, fun_name):
    table = []
    step = (max - min) / number_of_points
    for x in np.arange(min+(step/2), max+(step/2), step):
        table.append([x, fun1(x), fun2(x), abs(fun1(x) - fun2(x)) / fun1(x),
                      abs(fun1(x) - fun2(x))])
    print(tabulate(table, headers=["x", fun_name, "Interpolation of "+fun_name,
                                   "Relative error", "Absolute error"],
                   tablefmt="grid", floatfmt=".10f"))


# x_sqrt, y_sqrt, sqrt_tab = to_table(0, 10, 3, math.sqrt, "sqrt(x)")
# x_sin, y_sin, sin_tab = to_table(0, 10, 3, math.sin, "sin(x)")
# f = lambda x: x**3 + 2*x
# x_f, y_f, f_tab = to_table(0, 10, 3, f, "x^3 + 2x")
#
# sqrt_approx = lambda x: lagrange_interpolation(x_sqrt, y_sqrt, x)
# sin_approx = lambda x: lagrange_interpolation(x_sin, y_sin, x)
# f_approx = lambda x: lagrange_interpolation(x_f, y_f, x)
#
# print(sqrt_tab)
# cmp_inbetween_points(0, 10, 3, math.sqrt, sqrt_approx, "sqrt(x)")
# to_chart(0, 10, 100, math.sqrt, sqrt_approx, "sqrt(x)")
#
# print(sin_tab)
# cmp_inbetween_points(0, 10, 3, math.sin, sin_approx, "sin(x)")
# to_chart(0, 10, 100, math.sin, sin_approx, "sin(x)")
#
# print(f_tab)
# cmp_inbetween_points(0, 10, 3, f, f_approx, "x^3 + 2x")
# to_chart(0, 10, 100, f, f_approx, "x^3 + 2x")

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate
from tabulate import tabulate
import math
from lab4.zad_2 import to_table


def to_chart_2(min, max, number_of_points, fun1, fun2, fun_name):
    x_axis = np.linspace(min, max, number_of_points)
    f1_values = fun1(x_axis)
    f2_values = fun2(x_axis)

    plt.plot(x_axis, f1_values, label="Interpolation B-spline " + fun_name)
    plt.plot(x_axis, f2_values, label=fun_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(fun_name)
    plt.legend()
    plt.show()


def cmp_inbetween_points_2(min, max, number_of_points, fun1, fun2, fun_name):
    table = []
    step = (max - min) / number_of_points
    for x in np.arange(min + (step / 2), max + (step / 2), step):
        table.append([x, fun1(x), fun2(x),
                      abs(fun2(x) - fun1(x)) / fun1(x),
                      abs(fun2(x) - fun1(x))])
    print(tabulate(table, headers=["x", fun_name, "B-spline", "Relative error", "Absolute error"],
                   tablefmt="grid", floatfmt=".10f"))


def b_spline_calc(x_array, y_array):
    t, c, k = interpolate.splrep(x_array, y_array, s=0, k=2)
    return interpolate.BSpline(t, c, k, extrapolate=False)


def comparison_3(min, max, n):
    sqrt_x_arr, sqrt_y_arr, sqrt_x_y = to_table(min, max, n, math.sqrt, "sqrt(x)")
    sqrt_approx = b_spline_calc(sqrt_x_arr, sqrt_y_arr)
    print(sqrt_x_y)
    cmp_inbetween_points_2(min, max, n, np.sqrt, sqrt_approx, "sqrt(x)")
    to_chart_2(min, max, 1000, np.sqrt, sqrt_approx, "sqrt(x)")

    sin_x_arr, sin_y_arr, sin_x_y = to_table(min, max, n, math.sin, "sin(x)")
    sin_approx = b_spline_calc(sin_x_arr, sin_y_arr)
    print(sin_x_y)
    cmp_inbetween_points_2(min, max, n, np.sin, sin_approx, "sin(x)")
    to_chart_2(min, max, 1000, np.sin, sin_approx, "sin(x)")

    f = lambda x: x**3 + 2*x
    f_x_arr, f_y_arr, f_x_y = to_table(min, max, n, f, "x^3 + 2x")
    f_approx = b_spline_calc(f_x_arr, f_y_arr)
    print(f_x_y)
    cmp_inbetween_points_2(min, max, n, f, f_approx, "x^3 + 2x")
    to_chart_2(min, max, 1000, f, f_approx, "x^3 + 2x")


# comparison_3(0, 10, 4)
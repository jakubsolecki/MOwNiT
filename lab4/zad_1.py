import numpy as np
from tabulate import tabulate
import sympy as sp
import matplotlib.pyplot as plt
import math


def to_table(min, max, number_of_points, func, func_name):
    step = (max - min) / number_of_points
    table = []
    x_values = []
    y_values = []
    for i in np.arange(min, max + step, step):
        table.append([i, func(i)])
        x_values.append(i)
        y_values.append(func(i))
    return x_values, y_values, tabulate(table, headers=["x", func_name],
                                        tablefmt="grid", floatfmt=".10f")


def to_chart(min, max, number_of_points, fun1, poly_calc, polynomial, fun_name):
    x_axis = []
    f1_values = []
    f2_values = []
    step = (max - min) / number_of_points

    for x in np.arange(min, max+step, step):
        x_axis.append(x)
        f1_values.append(fun1(x))
        f2_values.append(poly_calc(polynomial, x))

    plt.plot(x_axis, f1_values, label=fun_name)
    plt.plot(x_axis, f2_values, label="Interpolated " + fun_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Comparison of " + fun_name + " and its interpolation")
    plt.legend()
    plt.show()


def cmp_inbetween_points(min, max, number_of_points, fun1, poly_calc, polynomial, fun_name):
    table = []
    step = (max - min) / number_of_points
    for x in np.arange(min + (step/2), max + (step/2), step):
        table.append([x, fun1(x), poly_calc(polynomial, x),
                      abs(poly_calc(polynomial, x) - fun1(x)) / fun1(x),
                      abs(poly_calc(polynomial, x) - fun1(x))])
    print(tabulate(table, headers=["x", fun_name, "Interpolation of " + fun_name, "Relative error", "Absolute error"],
                   tablefmt="grid", floatfmt=".10f"))


def calculate(f, x):
    X = sp.symbols("x")
    return f.evalf(subs={X: x})


def coefficients(x_array, y_array):
    n = len(x_array)
    res_tab = np.copy(y_array)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            res_tab[i] = float(res_tab[i] - res_tab[i-1])/float(x_array[i] - x_array[i-j])
    return np.array(res_tab)


def newton_polynomial(coeffs_array, x_array):
    X = sp.symbols("x")
    n = len(coeffs_array)
    res = 0
    for i in range(n):
        part = 1
        for j in range(i):
            part *= (X - x_array[j])
        res += part * coeffs_array[i]
    return sp.simplify(res)


def comparison(min, max, n):
    sqrt_x_arr, sqrt_y_arr, sqrt_x_y = to_table(min, max, n, math.sqrt, "sqrt(x)")
    sqrt_coeffs = coefficients(sqrt_x_arr, sqrt_y_arr)
    sqrt_approx = newton_polynomial(sqrt_coeffs, sqrt_x_arr)
    print(sqrt_x_y)
    cmp_inbetween_points(min, max, n, math.sqrt, calculate, sqrt_approx, "sqrt(x)")
    to_chart(min, max, 1000, math.sqrt, calculate, sqrt_approx, "sqrt(x)")

    sin_x_arr, sin_y_arr, sin_x_y = to_table(min, max, n, math.sin, "sin(x)")
    sin_coefs = coefficients(sin_x_arr, sin_y_arr)
    sin_approx = newton_polynomial(sin_coefs, sin_x_arr)
    print(sin_x_y)
    cmp_inbetween_points(min, max, n, math.sin, calculate, sin_approx, "sin(x)")
    to_chart(min, max, 1000, math.sin, calculate, sin_approx, "sin(x)")

    f = lambda x: x**3 + 2*x
    f_x_arr, f_y_arr, f_x_y = to_table(min, max, n, f, "x^3 + 2x")
    f_coefs = coefficients(f_x_arr, f_y_arr)
    f_approx = newton_polynomial(f_coefs, f_x_arr)
    print(f_x_y)
    cmp_inbetween_points(min, max, n, f, calculate, f_approx, "x^3 + 2x")
    to_chart(min, max, 1000, f, calculate, f_approx, "x^3 + 2x")


# comparison(0, 10, 3)

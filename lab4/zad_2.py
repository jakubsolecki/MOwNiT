import sympy as sp
from lab4.zad_1 import calculate, to_chart, to_table, cmp_inbetween_points
import math


def hermite_polynomial(x_array, y_array):
    n = len(x_array)
    derivatives = [0] * n

    for i in range(1, n):
        if x_array[i] == x_array[i-1]:
            derivatives[i] = derivatives[i-1] + 1
        else:
            derivatives[i] = 0

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            if derivatives[j] == 0:
                y_array[j] = \
                    (y_array[j] - y_array[int(j-1 - derivatives[j-1])]) / (x_array[j] - x_array[j - i])
            else:
                y_array[j] /= float(i)
                derivatives[j] -= 1

    for j in range(n - 1, -1, -1):
        for i in range(j, n - 1, 1):
            y_array[i] = y_array[i] - y_array[i+1] * x_array[j]

    polynomial = 0
    X = sp.symbols('x')
    for i in range(n):
        polynomial += y_array[i]*pow(X, i)

    return polynomial


def comparison_2(min, max, n):
    sqrt_x_arr, sqrt_y_arr, sqrt_x_y = to_table(min, max, n, math.sqrt, "sqrt(x)")
    sqrt_approx = hermite_polynomial(sqrt_x_arr, sqrt_y_arr)
    print(sqrt_x_y)
    cmp_inbetween_points(min, max, n, math.sqrt, calculate, sqrt_approx, "sqrt(x)")
    to_chart(min, max, 1000, math.sqrt, calculate, sqrt_approx, "sqrt(x)")

    sin_x_arr, sin_y_arr, sin_x_y = to_table(min, max, n, math.sin, "sin(x)")
    sin_approx = hermite_polynomial(sin_x_arr, sin_y_arr)
    print(sin_x_y)
    cmp_inbetween_points(min, max, n, math.sin, calculate, sin_approx, "sin(x)")
    to_chart(min, max, 1000, math.sin, calculate, sin_approx, "sin(x)")

    f = lambda x: x**3 + 2*x
    f_x_arr, f_y_arr, f_x_y = to_table(min, max, n, f, "x^3 + 2x")
    f_approx = hermite_polynomial(f_x_arr, f_y_arr)
    print(f_x_y)
    cmp_inbetween_points(min, max, n, f, calculate, f_approx, "x^3 + 2x")
    to_chart(min, max, 1000, f, calculate, f_approx, "x^3 + 2x")

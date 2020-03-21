import sympy as sp
import math
from zad_1 import to_table


def lagrange_polynomial(x_values, y_values):
    if len(x_values) != len(y_values):
        exit("There must be exact same number of x and y values")
        return -1
    x = sp.symbols('x')
    y = 0
    for k in range(len(x_values)):
        i = 1
        for j in range(len(x_values)):
            if j != k:
                i = i*((x - x_values[j]) / (x_values[k] - x_values[j]))
        y += i*y_values[k]
    return sp.simplify(y)


x_arr, y_arr = to_table(0, 10, 3, math.sqrt, "sqrt(x)")
print("Lagrange polynomial for sqrt(x):", lagrange_polynomial(x_arr, y_arr), "\n")

x_arr, y_arr = to_table(0, 10, 3, math.sin, "sin(x)")
print("Lagrange polynomial for sqrt(x):", lagrange_polynomial(x_arr, y_arr), "\n")

f = lambda x: x**3 + 2*x
x_arr, y_arr = to_table(0, 10, 3, f, "x^3 + 2x")
print("Lagrange polynomial for sqrt(x):", lagrange_polynomial(x_arr, y_arr), "\n")

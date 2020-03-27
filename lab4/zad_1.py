import numpy as np
from lab3 import zad_1 as l3z1, zad_2 as l3z2, zad_3 as l3z3, zad_4 as l3z4
import math


def div_diff_coeffs(x_array, y_array):
    length = len(x_array)
    x = np.copy(x_array)
    coef = np.copy(y_array)
    for j in range(1, length):
        coef[j:length] = (coef[j:length] - coef[j-1])/(x[j:length] - x[j-1])
    return coef


def interpolate(coeff_array, x_array, x):
    n = len(x_array) - 1
    res = coeff_array[n]
    for k in range(1, n + 1):
        res = coeff_array[n - k] + (x - x_array[n - k]) * res
    return res

# TODO: calculate interpolation error


sqrt_x_arr, sqrt_y_arr, _ = l3z1.to_table(0, 10, 3, math.sqrt, "sqrt(x)")
sqrt_coefs = div_diff_coeffs(sqrt_x_arr, sqrt_y_arr)
sqrt_approx = lambda x: interpolate(sqrt_coefs, sqrt_x_arr, x)
l3z3.to_chart(0, 10, 100, math.sqrt, sqrt_approx, "sqrt(x)")

sin_x_arr, sin_y_arr, _ = l3z1.to_table(0, 10, 3, math.sin, "sin(x)")
sin_coefs = div_diff_coeffs(sin_x_arr, sin_y_arr)
sin_approx = lambda x: interpolate(sin_coefs, sin_x_arr, x)
l3z3.to_chart(0, 10, 100, math.sin, sin_approx, "sin(x)")

f = lambda x: x**3 + 2*x
f_x_arr, f_y_arr, _ = l3z1.to_table(0, 10, 3, f, "x^3 + 2x")
f_coefs = div_diff_coeffs(f_x_arr, f_y_arr)
f_approx = lambda x: interpolate(f_coefs, f_x_arr, x)
l3z3.to_chart(0, 10, 100, f, f_approx, "x^3 + 2x")

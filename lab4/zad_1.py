import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def div_diff_coeffs(x_array, y_array):
    x_array.astype(float)
    y_array.astype(float)
    length = len(x_array)
    table = []
    for i in range(length):
        table.append(y_array[i])
    for j in range(1, length):
        for i in range(length-1, j-1, -1):
            table[i] = float(table[i] - table[i-1])/float(x_array[i] - x_array[i-j])
    return np.array(table)


def newton_polynomial(coeff_array, x_array):
    x = sp.symbols("x")
    x_array.astype(float)
    # n = len(x_array) - 1
    # div_diff = coeff_array[n] + (x - x_array[n])
    # for i in range(n-1, -1, -1):
    #     div_diff = div_diff*(x - x_array[i]) + coeff_array[i]
    # return sp.simplify(div_diff)
    polynomial_table = coeff_array
    res = polynomial_table[0]
    length = len(coeff_array)
    for i in range(length):
        for j in range(i, length):
            polynomial_table[j] = polynomial_table[j]*(x - x[i])
        res += polynomial_table[i]
    return sp.simplify(res)

import math
import numpy as np
from tabulate import tabulate


def to_table(min, max, number_of_points, func, func_name):
    step = (max - min) / number_of_points
    table = []
    x_values = []
    y_values = []
    for i in np.arange(min, max+step, step):
        table.append([i, func(i)])
        x_values.append(i)
        y_values.append(func(i))
    print(tabulate(table, headers=["x", func_name], tablefmt="grid", floatfmt=".10f"))
    return x_values, y_values


# to_table(0, 10, 3, math.sqrt, "sqrt(x)")
# # to_table(0, 10, 3, math.sin, "sin(x)")
# # f = lambda x: x**3 + 2*x
# # to_table(0, 10, 3, f, "x^3 + 2x")

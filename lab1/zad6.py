import numpy as np
from tabulate import tabulate


def kahan_algorithm(x, n):
    sum = 0.0
    eps = 0.0
    for i in range(0, n):
        x_without_eps = x - eps
        tmp_sum = sum + x_without_eps
        eps = (tmp_sum - sum) - x_without_eps
        sum = tmp_sum
    return sum


def add_n_times(x, n, sum):
    for i in range(0, n):
        sum += x
    return sum


table = [["float16", add_n_times(np.float16(0.09531258654533566), 100000000, np.float16(0))],
        ["float32", add_n_times(np.float32(0.09531258654533566), 100000000, np.float32(0))],
        ["float64", add_n_times(np.float64(0.09531258654533566), 100000000, np.float64(0))],
        ["kahan algorithm", kahan_algorithm(0.09531258654533566, 100000000)]]

print(tabulate(table, headers=['Type', 'Value'], floatfmt=".10f"))

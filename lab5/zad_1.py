import math
import numpy as np
import sympy as sp
from tabulate import tabulate
import matplotlib.pyplot as plt


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


def to_chart(min, max, number_of_points, fun1, fun2, fun_name, rel_errors, abs_errors, degree):
    x_axis = []
    f1_values = []
    f2_values = []
    step = (max - min) / number_of_points
    for x in np.arange(min, max+step, step):
        x_axis.append(x)
        f1_values.append(fun1(x))
        f2_values.append(fun2(x))
        if fun1(x) == 0:
            rel_errors.append(abs(fun2(x) - fun1(x)))
        else:
            rel_errors.append(abs(fun2(x) - fun1(x)) / fun1(x))
        abs_errors.append(abs(fun2(x) - fun1(x)))

    plt.plot(x_axis, f1_values, label=fun_name)
    plt.plot(x_axis, f2_values, label="Approximation of " + fun_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Least squares polynomial approximation of " + fun_name + ", degree: " + str(degree))
    plt.legend()
    plt.show()


# Least-squares polynomial approximation
def lspa(x_array, y_array, m):
    n = len(x_array)
    g_array = [0] * (2 * m + 1)

    for i in range(2 * m + 1):
        sum = 0
        for j in range(n):
            sum += pow(x_array[j], i)
        g_array[i] = sum

    b_array = np.zeros(m + 1)

    for i in range(m + 1):
        sum = 0
        for j in range(n):
            sum += (pow(x_array[j], i) * y_array[j])
        b_array[i] = sum

    g_matrix = np.zeros((m + 1, m + 1))

    for i in range(m + 1):
        for j in range(m + 1):
            g_matrix[i][j] = g_array[i + j]

    a_array = np.linalg.solve(g_matrix, b_array)

    polynomial = 0
    X = sp.symbols('x')
    for i in range(m + 1):
        polynomial += pow(X, i) * a_array[i]

    return sp.simplify(polynomial)


def calculate(p, x):
    s = sp.symbols("x")
    return p.evalf(subs={s: x})


def cmp_err(rel_errors, abs_errors):
    tab = [["Mean of relative errors [%]", float(sum(rel_errors) / len(rel_errors)) * 100],
               ["Mean of absolute errors", float(sum(abs_errors) / len(abs_errors))]]
    print(tabulate(tab, headers=["Type", "General error"], tablefmt="grid", floatfmt=".10f"), "\n")


def show_lspan(min, max, number_of_points, n):
    sqrt_x_arr, sqrt_y_arr, sqrt_x_y = to_table(min, max, number_of_points, math.sqrt, "sqrt(x)")
    sin_x_arr, sin_y_arr, sin_x_y = to_table(min, max, number_of_points, math.sin, "sin(x)")
    f = lambda x: x ** 3 + 2 * x
    f_x_arr, f_y_arr, f_x_y = to_table(min, max, number_of_points, f, "x^3 + 2x")

    for i in range(1, n + 1):
        sqrt_lspa = lspa(sqrt_x_arr, sqrt_y_arr, i)
        sin_lspa = lspa(sin_x_arr, sin_y_arr, i)
        f_lspa = lspa(f_x_arr, f_y_arr, i)

        sqrt_approx = lambda x: calculate(sqrt_lspa, x)
        sin_approx = lambda x: calculate(sin_lspa, x)
        f_approx = lambda x: calculate(f_lspa, x)

        rel_errors = []
        abs_errors = []
        to_chart(min, max, 100, math.sqrt, sqrt_approx, "sqrt(x)", rel_errors, abs_errors, i)
        cmp_err(rel_errors, abs_errors)

        rel_errors = []
        abs_errors = []
        to_chart(min, max, 100, math.sin, sin_approx, "sin(x)", rel_errors, abs_errors, i)
        cmp_err(rel_errors, abs_errors)

        rel_errors = []
        abs_errors = []
        to_chart(min, max, 100, f, f_approx, "x^3 + 2x", rel_errors, abs_errors, i)
        cmp_err(rel_errors, abs_errors)


# show_lspan(0, 10, 3, 2)
# show_lspan(0, 10, 4, 3)
# show_lspan(0, 10, 5, 4)
# show_lspan(0, 10, 8, 7)


timeline = ['1/21/2020','1/22/2020','1/23/2020','1/24/2020','1/25/2020','1/26/2020','1/27/2020','1/28/2020','1/29/2020',
            '1/30/2020','1/31/2020','2/1/2020','2/2/2020','2/3/2020','2/4/2020','2/5/2020','2/6/2020','2/7/2020',
            '2/8/2020','2/9/2020','2/10/2020','2/11/2020','2/12/2020','2/13/2020','2/14/2020','2/15/2020','2/16/2020',
            '2/17/2020','2/18/2020','2/19/2020','2/20/2020','2/21/2020','2/22/2020','2/23/2020','2/24/2020','2/25/2020',
            '2/26/2020','2/27/2020','2/28/2020','2/29/2020','3/1/2020','3/2/2020','3/3/2020','3/4/2020','3/5/2020',
            '3/6/2020','3/7/2020','3/8/2020','3/9/2020','3/10/2020','3/11/2020','3/12/2020','3/13/2020','3/14/2020'
            ,'3/15/2020','3/16/2020','3/17/2020','3/18/2020','3/19/2020','3/20/2020','3/21/2020','3/22/2020',
            '3/23/2020','3/24/2020','3/25/2020','3/26/2020','3/27/2020','3/28/2020','3/29/2020','3/30/2020','3/31/2020',
            '4/1/2020','4/2/2020','4/3/2020']

cases = [1,1,1,1,3,3,4,6,7,11,14,17,20,20,20,33,25,25,25,26,26,26,28,29,33,41,53,59,65,73,85,93,105,132,144,157,164,
         186,210,230,239,254,268,284,317,349,408,455,488,514,568,620,675,716,780,814,829,829,873,950,996,1046,1089,
         1128,1193,1291,1387,1499,1693,1866,1953,2178,2384,2617]


def calculate2(p, n):
  values = []
  for i in n:
    values.append(calculate(p, i))
  return values


def covid_approx(timeline, cases, n):
    for i in range(1, n + 1):
        cases_polynomial = lspa(np.linspace(1, len(cases), len(cases)), cases, i)
        cases_values = calculate2(cases_polynomial, np.linspace(1, len(cases), len(cases)))

        params = {'legend.fontsize': 'x-large',
                  'figure.figsize': (20, 12),
                  'axes.labelsize': 'x-large',
                  'axes.titlesize': 'x-large',
                  'xtick.labelsize': 'x-large',
                  'ytick.labelsize': 'x-large'}
        plt.rcParams.update(params)
        plt.title(f'Approximation of degree {i}')
        plt.plot(timeline, cases_values, label="Approximation")
        plt.plot(timeline, cases, 'ro', label="Data")
        plt.grid(True, which='both')
        plt.xlabel('Timeline')
        plt.ylabel('Cases')
        plt.xticks(rotation=90)
        plt.legend()
        plt.show()


# covid_approx(timeline, cases, 10)

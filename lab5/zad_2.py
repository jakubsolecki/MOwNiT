import math
import numpy as np
import matplotlib.pyplot as plt
from lab5.zad_1 import to_table, timeline, cases


def to_chart2(min, max, number_of_points, fun1, fun2, fun_name, degree):
    x_axis = []
    f1_values = []
    step = (max - min) / number_of_points

    for x in np.arange(min, max+step, step):
        x_axis.append(x)
        f1_values.append(fun1(x))

    f2_values = np.polyval(fun2[0], x_axis)

    plt.plot(x_axis, f1_values, label=fun_name)
    plt.plot(x_axis, f2_values, label="Approximation of " + fun_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Least squares polynomial approximation of " + fun_name + ", degree: " + str(degree))
    plt.legend()
    plt.show()


def python_approx(min, max, number_of_points, n):
    sqrt_x_arr, sqrt_y_arr, _ = to_table(min, max, number_of_points, math.sqrt, "sqrt(x)")
    sin_x_arr, sin_y_arr, _ = to_table(min, max, number_of_points, math.sin, "sin(x)")
    f = lambda x: x ** 3 + 2 * x
    f_x_arr, f_y_arr, _ = to_table(min, max, number_of_points, f, "x^3 + 2x")

    for i in range(1, n + 1):

        sqrt_approx = np.polyfit(sqrt_x_arr, sqrt_y_arr, deg=i, full=True)
        to_chart2(0, 10, 100, math.sqrt, sqrt_approx, "sqrt(x)", i)

        sin_approx = np.polyfit(sin_x_arr, sin_y_arr, deg=i, full=True)
        to_chart2(0, 10, 100, math.sin, sin_approx, "sin(x)", i)

        f_approx = np.polyfit(f_x_arr, f_y_arr, deg=i, full=True)
        to_chart2(0, 10, 100, f, f_approx, "x^3 + 2x", i)


def python_covid_approx(timeline, cases, n):
    for i in range(1, n + 1):
        cases_polynomial = np.polyfit(np.linspace(1, len(timeline), len(timeline)), cases, i)
        cases_values = np.polyval(cases_polynomial, np.linspace(1, len(timeline), len(timeline)))

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
    

python_approx(0, 10, 3, 2)
python_approx(0, 10, 4, 3)
python_approx(0, 10, 5, 4)
python_approx(0, 10, 8, 7)
python_covid_approx(timeline, cases, 10)

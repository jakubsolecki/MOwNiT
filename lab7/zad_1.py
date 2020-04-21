from pylab import *
from scipy.special.orthogonal import roots_legendre
import scipy.integrate as integrate
from tabulate import tabulate
from lab6.zad_1 import *
import math


def gauss_legendre_rule(fun, a, b, n):
    [x, w] = roots_legendre(n+1)
    g = 0.5 * (b - a)
    h = 0.5 * (b - a) * x + 0.5 * (b + a)
    integral = g * sum(w * np.vectorize(fun)(h))
    return integral


def comparison(a, b, n):
    f1 = lambda x: 3*x**3 - 1
    f1_str = "3*x**3 - 1"
    f2 = lambda x: 2*x**2
    f2_str = " 2*x**2"
    f3 = lambda x: 4*math.sin(x)
    f3_str = "4*sin(x)"

    for f in [(f1, f1_str), (f2, f2_str), (f3, f3_str)]:
        ref_val = integrate.quad(f[0], a, b)[0]  # used as a reference value an integral
        rect = rectangle_rule(f[0], a, b, n)
        trap = trapezoidal_rule(f[0], a, b, n)
        simp = simpson_rule(f[0], a, b, n)
        gauss_leg_deg_2 = gauss_legendre_rule(f[0], a, b, 2)
        gauss_leg_deg_3 = gauss_legendre_rule(f[0], a, b, 3)
        gauss_leg_deg_4 = gauss_legendre_rule(f[0], a, b, 4)
        gauss_leg_deg_5 = gauss_legendre_rule(f[0], a, b, 5)

        if ref_val == 0:
            rect_rel_err = "Undefined"
            trap_rel_err = "Undefined"
            simp_rel_err = "Undefined"
            gauss_2_rel_err = "Undefined"
            gauss_3_rel_err = "Undefined"
            gauss_4_rel_err = "Undefined"
            gauss_5_rel_err = "Undefined"
        else:
            rect_rel_err = (abs(rect - ref_val) / ref_val) * 100
            trap_rel_err = (abs(trap - ref_val) / ref_val) * 100
            simp_rel_err = (abs(simp - ref_val) / ref_val) * 100
            gauss_2_rel_err = (abs(gauss_leg_deg_2 - ref_val) / ref_val) * 100
            gauss_3_rel_err = (abs(gauss_leg_deg_3 - ref_val) / ref_val) * 100
            gauss_4_rel_err = (abs(gauss_leg_deg_4 - ref_val) / ref_val) * 100
            gauss_5_rel_err = (abs(gauss_leg_deg_5 - ref_val) / ref_val) * 100

        table = [["Quad integral (SciPy)", ref_val, 0, 0],
                 ["Rectangular rule", rect, rect_rel_err, abs(rect - ref_val)],
                 ["Trapezoidal rule", trap, trap_rel_err, abs(trap - ref_val)],
                 ["Simpson's rule", simp, simp_rel_err, abs(simp - ref_val)],
                 ["Gauss-Legendre, 2nd degree", gauss_leg_deg_2, gauss_2_rel_err, abs(gauss_leg_deg_2 - ref_val)],
                 ["Gauss-Legendre, 3rd degree", gauss_leg_deg_3, gauss_3_rel_err, abs(gauss_leg_deg_3 - ref_val)],
                 ["Gauss-Legendre, 4th degree", gauss_leg_deg_4, gauss_4_rel_err, abs(gauss_leg_deg_4 - ref_val)],
                 ["Gauss-Legendre, 5th degree", gauss_leg_deg_5, gauss_5_rel_err, abs(gauss_leg_deg_5 - ref_val)]]

        print(tabulate(table, headers=[f"Integration method for {f[1]}", "Value of the definite integral",
                                       "Relative error [%]", "Absolute error"], tablefmt="grid", floatfmt=".10f"), "\n\n")


comparison(-2, 3, 5)
comparison(-10, 15, 50)
comparison(0, 300, 1000)
comparison(0, 100, 30)
comparison(0, 10, 20)

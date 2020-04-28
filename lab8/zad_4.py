from scipy import optimize as opt
from lab8.zad_1 import *
from lab8.zad_2 import newton_raphson
from lab8.zad_3 import secant_method
from tabulate import tabulate


def comparison_4(fun, a, b, n, fun_name):
    ref = opt.bisect(fun, a, b)  # used as reference value
    b_m = bisection_method(a, b, fun, n)[0]
    n_r = newton_raphson(fun, b, n)
    s_m = secant_method(fun, a, b, n)

    print(f"Function {fun_name}, range: [{a}, {b}]")
    res = [["SciPy bisection method", ref, 0, 0],
           ["Bisection method", b_m, (abs(b_m - ref) / abs(ref))*100, abs(ref - b_m)],
           ["Newton-Raphson method", n_r, (abs(n_r - ref) / abs(ref))*100, abs(ref - n_r)],
           ["Secant method", s_m, (abs(s_m - ref) / abs(ref))*100, abs(ref - s_m)]]

    print(tabulate(res, headers=["Method", "Value", "Relative error [%]", "Absolute error"], tablefmt="grid"))

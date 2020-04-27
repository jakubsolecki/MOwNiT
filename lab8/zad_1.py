import numpy as np
import math
import matplotlib.pyplot as plt
from tabulate import tabulate


f1 = lambda x: 2*x**2 - 2*x + 1
f1_name = "f(x)=2x^2−2x+1"
f2 = lambda x: -26 + 85*x - 91*x**2 + 44*x**3 - 8*x**4 + x**5
f2_name = "f(x)=−26+85x−91x^2+44x^3−8x^4+x^5"
f3 = lambda x: pow(4, x) - pow(3, 2*x) + pow(2, 3*x)
f3_name = "f(x)=4^x−3^(2x)+2^(3x)−1"
f4 = lambda x: 3*x + math.sin(x) - math.cos(x)**3
f4_name = "f(x)=3∗x+sin(x)−(cos(x))^3"
f5 = lambda x: 27*x**3 - 3*x + 1
f5_name = "f(x)=27x^3−3x+1"


def to_chart(fun, a, b, n, func_name):
    x_axis = np.linspace(a, b, n)
    plt.plot(x_axis, np.vectorize(fun)(x_axis), label=func_name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(func_name)
    plt.grid()
    plt.show()


def bisection_method(a, b, fun, n):  # n is the max number of allowed iterations
    if fun(a) * fun(b) > 0:
        # end function, no root
        return None, None
    else:
        d = b - a
        x_0 = None
        for i in range(n):
            x_0 = (a + b) / 2.0
            if fun(x_0) == 0:
                e = d / 2**i
                return x_0, e
            elif fun(a) * fun(x_0) < 0:
                b = x_0
            else:
                a = x_0

        print("Exceeded max number of iterations")
        e = d / 2**n
        return x_0, e


def compute():
    to_chart(f1, -2, 2, 100, f1_name)
    x_0, e = bisection_method(-2, 2, f1, 1000)
    if x_0 is None and e is None:
        print("No roots found")
    else:
        tab = [[x_0, e]]
        print(tabulate(tab, headers=["Root", "E"], tablefmt="grid"), "\n\n")

    to_chart(f2, 0, 1, 100, f2_name)
    x_0, e = bisection_method(0, 1, f2, 100)
    if x_0 is None and e is None:
        print("No roots found")
    else:
        tab = [[x_0, e]]
        print(tabulate(tab, headers=["Root", "E"], tablefmt="grid"), "\n\n")

    to_chart(f3, -4, 2, 100, f3_name)
    x_0, e = bisection_method(-4, 2, f3, 100)
    if x_0 is None and e is None:
        print("No roots found")
    else:
        tab = [[x_0, e]]
        print(tabulate(tab, headers=["Root", "E"], tablefmt="grid"), "\n\n")

    to_chart(f4, -1, 1, 100, f4_name)
    x_0, e = bisection_method(-1, 1, f4, 100)
    if x_0 is None and e is None:
        print("No roots found")
    else:
        tab = [[x_0, e]]
        print(tabulate(tab, headers=["Root", "E"], tablefmt="grid"), "\n\n")

    to_chart(f5, -1, 1, 100, f5_name)
    x_0, e = bisection_method(-1, 1, f5, 100)
    if x_0 is None and e is None:
        print("No roots found")
    else:
        tab = [[x_0, e]]
        print(tabulate(tab, headers=["Root", "E"], tablefmt="grid"), "\n\n")


if __name__ == "__main__":
    compute()

from lab8.zad_1 import *
from scipy.misc import derivative


def newton_raphson(fun, x, n):
    for i in range(n):
        if derivative(fun, x) == 0:
            return "None"
        h = fun(x) / derivative(fun, x)
        x = x - h

    return x


def comparison_2():
    to_chart(f1, -2, 2, 100, f1_name)
    print("Initial guess: 0")
    print(f"Root: {newton_raphson(f1, 0, 100)}")

    to_chart(f2, 0, 1, 100, f2_name)
    print("Initial guess: 1")
    print(f"Root: {newton_raphson(f2, 1, 100)}")

    to_chart(f3, -4, 2, 100, f3_name)
    print("Initial guess: 1")
    print(f"Root: {newton_raphson(f3, 1, 100)}")

    to_chart(f4, -1, 1, 100, f4_name)
    print("Initial guess: 0")
    print(f"Root: {newton_raphson(f4, 0, 100)}")

    to_chart(f5, -1, 1, 100, f5_name)
    print("Initial guess: 0")
    print(f"Root: {newton_raphson(f5, 0, 100)}")


if __name__ == "__main__":
    comparison_2()

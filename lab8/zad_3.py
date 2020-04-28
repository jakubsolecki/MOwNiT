from lab8.zad_1 import *


def secant_method(fun, x0, x1, n):
    if fun(x0) * fun(x1) >= 0 or n <= 0 or x0 >= x1:
        return "No root found"

    for i in range(n):
        x2 = x1 - (fun(x1) * (x1 - x0)) / (fun(x1) - fun(x0))
        x0, x1 = x1, x2

    return x2


def comparison_3():
    to_chart(f1, -2, 2, 100, f1_name)
    print("Initial range: [-1, 2]")
    print(f"Root: {secant_method(f1, -1, 2, 10)}")

    to_chart(f2, 0, 1, 100, f2_name)
    print("Initial range: [0.4, 0.6]")
    print(f"Root: {secant_method(f2, 0.4, 0.6, 10)}")

    to_chart(f3, -4, 2, 100, f3_name)
    print("Initial range: [1, 2]")
    print(f"Root: {secant_method(f3, 1, 2, 10)}")

    to_chart(f4, -1, 1, 100, f4_name)
    print("Initial range: [0, 0.5]")
    print(f"Root: {secant_method(f4, 0, 0.5, 5)}")

    to_chart(f5, -1, 1, 100, f5_name)
    print("Initial range: [-0.75, -0.25]")
    print(f"Root: {secant_method(f5, -0.75, -0.25, 8)}")


if __name__ == "__main__":
    comparison_3()

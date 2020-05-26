from lab12.zad_1_2 import *
from lab11.zad_2 import sor, gauss_seidel
import matplotlib.pyplot as plt
import matplotlib as mpl


def visualize(N=10):
    AA, n = chebyshev_method(A, b, 1000, 0, 2, eps=1e-10)
    x, y = [], []

    for i in range(1, N+1):
        for j in range(1, N+1):
            x.append(i)
            y.append(j)

    plt.scatter(x, y, c=AA, sizes=[1500 for _ in range(N**2)], alpha=1, cmap=mpl.cm.cool, marker="s")
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    A = generate_matrix()
    b = generate_b_vector()
    AA, n = chebyshev_method(A, b, 1000, 0, 2, eps=1e-10)
    print(f"Iterations: {n}")
    print(AA)

    AA, n = gauss_seidel(A, b, 1000, 1e-10)
    print(f"\nIterations: {n}")
    print(AA)

    AA, n = sor(A, b, 1000, 1e-10, 1.9)
    print(f"\nIterations : {n}")
    print(AA)

    visualize()

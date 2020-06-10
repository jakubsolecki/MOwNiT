import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def lin_rand(a, c, m, x, n):
    tab = []
    generator = lambda a, c, m, x: (a*x + c) % m
    for _ in range(n):
        x = generator(a, c, m, x)
        tab.append(x/m)
    return tab


def visualize(tab):
    x = [tab[i] for i in range(len(tab)) if i % 2 == 0]
    y = [tab[i] for i in range(len(tab)) if i % 2 == 1]

    plt.figure(figsize=(7, 7))
    plt.scatter(x, y)
    plt.show()


if __name__ == "__main__":
    tab = lin_rand(1103515245, 12345, 2**32, 1000, 50)
    print(tab)
    visualize(tab)

from numpy import random
import numpy as np
import scipy.integrate as integrate
from tabulate import tabulate


f1 = lambda x: 1 / (x**2)
f2 = lambda x: 1 / np.sqrt(x**5+8)
f3 = lambda x: x**2 + 2*x


def monte_carlo(func, a, b, n):
    res = 0.0
    for _ in range(n):
        res += func(random.uniform(a, b))

    return ((b - a)/n)*res


def sphere(r, n):
    points = []
    points_in_sphere = 0
    for _ in range(n):
        point = np.random.uniform(-r, r), np.random.uniform(-r, r), np.random.uniform(-r, r)
        points.append(point)
        if point[0] ** 2 + point[1] ** 2 + point[2] ** 2 <= r ** 2:
            points_in_sphere += 1
    vol = (points_in_sphere/n)*((2*r)**3)
    print(f"The volume of the sphere with a radius of {r} and the number of samples of {n} is approximately", vol)
    return vol


def cone(r, h, n):
    points = []
    points_in_cone = 0
    for _ in range(n):
        point = np.random.uniform(-r, r), np.random.uniform(-r, r), np.random.uniform(0, h)
        points.append(point)
        if point[0]**2 + point[1]**2 <= ((point[2]*r)/h)**2:
            points_in_cone += 1
    vol = (points_in_cone/n)*(h*(2*r)**2)
    print(f"The volume of the cone with a radius of {r}, height of {h} and the number of samples of {n} "
          f"is approximately", vol)
    return vol


def fancy_block(s_radius, r_radius, h, n):
    points = []
    points_in_block = 0
    for _ in range(n):
        point = np.random.uniform(-s_radius, s_radius), np.random.uniform(-s_radius, s_radius), \
                np.random.uniform(-s_radius, s_radius)
        points.append(point)
        if not (point[0]**2 + point[1]**2 <= r_radius**2 and h/2 >= point[2] >= -h/2) and \
                point[0]**2 + point[1]**2 + point[2]**2 <= s_radius**2:
            points_in_block += 1
    val = (points_in_block/n)*((2*s_radius)**3)
    print(f"The volume of the solid being the difference between a sphere with a radius of {s_radius} and a cylinder "
          f"with a height of {h} and a base radius of {r_radius} and a quantity of {n} samples is about", val)
    return val


if __name__ == "__main__":
    # tab = [
    #     ["f1", monte_carlo(f1, 1, 2, 10000), integrate.quad(f1, 1, 2)[0]],
    #     ["f2", monte_carlo(f2, 1, 6, 10000), integrate.quad(f2, 1, 6)[0]],
    #     ["f3", monte_carlo(f3, 1, 22, 10000), integrate.quad(f3, 1, 22)[0]]
    # ]
    #
    # print(tabulate(tab, headers=['Function', 'Monte Carlo integral', 'Scipy.integrate.quad'], tablefmt="grid",
    #                floatfmt=".10f"))

    # sphere(5, 100)
    # sphere(5, 10000)
    #
    # cone(10, 10, 100)
    # cone(10, 10, 10000)

    fancy_block(10, 3, 6, 10000)
    fancy_block(10, 3, 6, 100000)


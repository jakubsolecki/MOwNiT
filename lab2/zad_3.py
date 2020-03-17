import numpy as np


def has_zero(v):
    print("Zero at:", np.where(v == 0))


def has_inf(v):
    print("inf at:", np.where(v == np.inf))
    print("-inf at:", np.where(v == -np.inf))


def are_equal(a, b):
    if a.ndim == b.ndim and a.size == b.size:
        return a == b
    elif a.size > b.size:
        b = np.resize(b, (1, a.size))
        a = np.resize(a, (1, a.size))
        return a == b
    else:
        a = np.resize(b, (1, b.size))
        b = np.resize(b, (1, b.size))
        return a == b


a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 5])
print(are_equal(a, b))

c = np.array([[1, 2], [3, 4]])
d = np.mat(c)
print(are_equal(d, a))

has_zero(np.array([0, 1, 1]))
has_inf(np.array([np.inf, 1, 1, -np.inf]))
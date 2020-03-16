import numpy as np


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
print(are_equal(c, a))

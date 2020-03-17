import numpy as np


def show_bytes(tab):
    if not isinstance(tab, np.ndarray) and not isinstance(tab, np.matrix):
        tab = np.array(tab)

    return tab.nbytes


a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = [[1, 2, 3], [4, 5, 6]]
m = np.mat(b)
print(show_bytes(a))
print(show_bytes(b))
print(show_bytes(m))

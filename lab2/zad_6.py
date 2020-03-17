import numpy as np
import time


def add_vectors(v1, v2):
    if len(v1) == len(v2):
        start = time.time()
        for i in range(len(v1)):
            v1[i] += v2[i]
        end = time.time()
        return v1, end - start
    else:
        print("You shouldn't add vectors of different lengths")


def cross_multiply_vectors(v1, v2):
    if isinstance(v1, np.ndarray):
        v1 = v1.tolist()
    if isinstance(v2, np.ndarray):
        v2 = v2.tolist()
    if len(v1) == len(v2):
        start = time.time()
        v3 = v1[1:] + v1[:-1]
        v4 = v2[1:] + v2[:-1]
        v5 = []
        for i in range(0, len(v3) - 1):
            v5 += [v3[i]*v4[i+1] - v3[i+1]*v4[i]]
        end = time.time()
        return v5, end - start
    else:
        return "You shouldn't multiply vectors of different lengths"


def multiply_matrices(m1, m2):
    if len(m1[0]) != len(m2):
        return "Incorrect dimensions"
    start = time.time()
    m3 = np.zeros((len(m1), len(m2[0])))
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j] += m1[i][k] * m2[k][j]
    end = time.time()
    return m3, start - end


def numpy_add_vectors(v1, v2):
    start = time.time()
    v3 = np.add(v1, v2)
    end = time.time()
    return v3, end - start


def numpy_cross_multiply_vectors(v1, v2):
    start = time.time()
    v3 = np.cross(v1, v2)
    end = time.time()
    return v3, end - start


def numpy_multiply_matrices(m1, m2):
    start = time.time()
    r = np.dot(m1, m2)
    end = time.time()
    return r, end - start


a = [[12, 7, 3],
     [4, 5, 6]]
b = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
c = [1, 2, 3]
d = [3, 2, 1]

print("Numpy add two vectors:", numpy_add_vectors(c, d))
print("My add two vectors:", add_vectors(c, d), "\n")
print("Numpy cross multiply two vectors:", numpy_cross_multiply_vectors(c, d), "\n")
print("My cross multiply two vectors:", cross_multiply_vectors(c, d), "\n")
print("Numpy multiply matrices: \n", numpy_multiply_matrices(a, b)[0],
      "\n", numpy_multiply_matrices(a, b)[1])
print("My multiply matrices: \n", multiply_matrices(a, b)[0],
      "\n", multiply_matrices(a, b)[1])


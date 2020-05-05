import numpy as np
from tabulate import tabulate


# ============================================================
# Gaussian elimination without pivoting
# ============================================================

def forward_elimination(A, b):
    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - factor * A[k][j]
            b[i] = b[i] - factor * b[k]
    return A, b


def back_substitution(A, b):
    n = len(A)
    x = [0 for _ in range(n)]
    x[n-1] = b[n-1] / A[n-1][n-1]
    for k in range(n-2, -1, -1):
        sums = b[k]
        for j in range(k+1, n):
            sums = sums - A[k][j] * x[j]
        x[k] = sums / A[k][k]
    return x


def gauss_without_pivot(A, b):
    for i in range(len(A)):
        if len(A) != len(A[i]):
            raise Exception('Matrix must be square!')
    A, b = forward_elimination(A, b)
    return back_substitution(A, b)


# ============================================================
# Gaussian elimination with pivoting
# ============================================================

def gauss_with_pivot(A, b):
    n = len(A)
    M = A
    i = 0

    for x in A:
        x.append(b[i])
        i += 1

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]

        for j in range(k+1, n):
            q = M[j][k] / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    x = [0 for _ in range(n)]

    x[n-1] = M[n-1][n] / M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z += M[i][j]*x[j]
        x[i] = (M[i][n] - z) / M[i][i]
    return x


if __name__ == '__main__':
    A = \
        [[0.00000000000000012, 4200, 34, 65, 9012],
         [0.5, 0.00000056, 2320, 53, 456],
         [1, 17.000005, 7, 0.000000000004, 458],
         [38, 9, 896, 0.000000006, 58],
         [586, 6, 3857, 56, 0.000065]]
    b = \
        [7, 3.901, 6, 6, 858]
    x1 = gauss_without_pivot(A, b)

    C = \
        [[0.00000000000000012, 4200, 34, 65, 9012],
         [0.5, 0.00000056, 2320, 53, 456],
         [1, 17.000005, 7, 0.000000000004, 458],
         [38, 9, 896, 0.000000006, 58],
         [586, 6, 3857, 56, 0.000065]]
    d = \
        [7, 3.901, 6, 6, 8585]
    x2 = gauss_with_pivot(C, d)

    E = \
        [[0.00000000000000012, 4200, 34, 65, 9012],
         [0.5, 0.00000056, 2320, 53, 456],
         [1, 17.000005, 7, 0.000000000004, 458],
         [38, 9, 896, 0.000000006, 58],
         [586, 6, 3857, 56, 0.000065]]
    f = \
        [7, 3.901, 6, 6, 8585]
    x3 = np.linalg.solve(E, f)

    tab = [["Without pivoting"] + x1,
           ["With pivoting"] + x2,
           ["numpy.linalg"] + list(x3)]
    print(tabulate(tab, headers=["Type", "x1", "x2", "x3", "x4", "x5"]))

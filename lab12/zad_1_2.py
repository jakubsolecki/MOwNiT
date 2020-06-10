import numpy as np
from scipy.linalg import norm


# def chebyshev_method(A, b, n, l_max, l_min, eps=1e-6, N=10):
#     c = (l_max - l_min) / 2
#     d = (l_max + l_min) / 2
#     x = np.zeros(N**2)
#     r = b - np.matmul(A, x)
#     iterations = 0
#
#     for i in range(1, n+1):
#         iterations += 1
#         z = np.linalg.solve(A, r)
#         alpha = 1
#
#         if i == 1:
#             alpha = 1/d
#             p = z
#         elif i == 2:
#             beta = (1/2)*(c*alpha)**2
#             alpha = 1/(d - beta/alpha)
#             p = z + beta*p
#         else:
#             beta = (c*alpha/2)**2
#             alpha = 1/(d - beta/alpha)
#             p = z + beta*p
#         x = x + alpha*p
#         r = b - np.matmul(A, x)
#
#         if norm(r) < eps:
#             return x, iterations
#
#     return x, iterations


def chebyshev_method(A, b, n, eps, omg):
    if omg < 0 or omg > 2:
        raise Exception("Omega must be from range (0, 2)")
    it = 0
    x = np.zeros_like(b)
    x_new = np.zeros_like(x)

    rho = max(abs(np.linalg.eigvals(np.subtract(np.identity(len(b)), np.dot(b.transpose(), A)))))
    for j in range(n):
        it += 1
        for i in range(b.shape[0]):
            old_sum = np.dot(A[i, i + 1:], x_new[i + 1:])
            new_sum = np.dot(A[i, :i], x[:i])
            x[i] = (b[i] - (old_sum + new_sum)) / A[i, i]
            x[i] = np.dot(x[i], omg) + np.dot(x_new[i], (1 - omg))

        # rho = max(abs(np.linalg.eigvals(A)))
        omg = 1.0 / (1.0 - 0.25 * rho ** 2 * omg)
        if j == 1:
            omg = 1.0 / (1.0 - 0.5 * (rho ** 2))
        if np.linalg.norm(np.dot(A, x) - b) < eps:
            return x_new, it
        x_new = x

    return x, it


def generate_matrix(N=10):
    A = np.zeros((N**2, N**2))
    for i in range(N**2):
        A[i][i] = -4
        if i - 1 >= 0:
            A[i-1][i] = 1.0
        if i + 1 < N**2:
            A[i+1][i] = 1.0
        if i - N >= 0:
            A[i-N][i] = 1.0
        if i + N < N**2:
            A[i+N][i] = 1.0
    return A


def print_A(A, N=10):
    for i in range(N):
        for j in range(N):
            print(A[i][j], " ", end='')
        print("")


def generate_b_vector(N=10):
    b = np.zeros(N**2)
    n = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            b[n] = (i + j)/2
            n += 1
    return b


if __name__ == "__main__":
    b = generate_b_vector()
    print(b)

    A = generate_matrix()
    print_A(A, 20)

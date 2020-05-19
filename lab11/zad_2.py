import numpy as np
from lab11.zad_1 import random_matrix_vector, jacobi


def gauss_seidel(A, b, n, eps):
    x = np.zeros_like(b)
    it = 0
    for _ in range(n):
        x_new = np.zeros_like(x)
        it += 1
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, atol=eps, rtol=0):
            return x_new, it
        x = x_new
    return x, it


def sor(A, b, n, eps, omg):
    if omg < 0 or omg > 2:
        raise Exception("Omega must be from range (0, 2)")
    it = 0
    x = np.zeros_like(b)
    x_new = np.zeros_like(x)
    for _ in range(n):
        it += 1
        for i in range(b.shape[0]):
            old_sum = np.dot(A[i, i + 1:], x_new[i + 1:])
            new_sum = np.dot(A[i, :i], x[:i])
            x[i] = (b[i] - (old_sum + new_sum)) / A[i, i]
            x[i] = np.dot(x[i], omg) + np.dot(x_new[i], (1 - omg))
        if np.linalg.norm(np.dot(A, x) - b) < eps:
            return x_new, it
        x_new = x
    return x, it


def comparison2(m_min, m_max, v_min, v_max, n_size, n_iter, eps=1e-10, omg=0.2):
    A, b = random_matrix_vector(m_min, m_max, v_min, v_max, n_size)
    print(f"Numpy:\n{np.linalg.solve(A, b)}")
    print(f"Gauss_Seidel:\n{gauss_seidel(A, b, n_iter, eps)[0]}")
    print(f"SOR:\n{sor(A, b, n_iter, eps, omg)[0]}")


def comparison3(m_min, m_max, v_min, v_max, n_size, n_iter, eps=1e-10, omg=0.2):
    A, b = random_matrix_vector(m_min, m_max, v_min, v_max, n_size)
    x, it = jacobi(A, b, eps, n_iter)
    print(f"Jacobi:\n Iterations: {it}\n{x}")
    x, it = gauss_seidel(A, b, n_iter, eps)
    print(f"Gauss_Seidel:\nIterations: {it}\n{x}")
    x, it = sor(A, b, n_iter, eps, omg)
    print(f"SOR:\nIterations: {it}\n{x}")


if __name__ == "__main__":
    comparison3(-50, 50, -20, 20, 25, 1000)

import numpy as np
import random


def jacobi(A, b, eps=1e-10, n=500):
    D = np.diag(np.diag(A))
    LU = A - D
    x = np.zeros(len(b))
    it = 0

    for i in range(n):
        D_inv = np.diag(1 / np.diag(D))
        x_new = np.dot(D_inv, b - np.dot(LU, x))
        it += 1
        if np.linalg.norm(x_new - x) < eps:
            return x_new, it
        x = x_new

    return x, it


def random_matrix_vector(m_min, m_max, v_min, v_max, n):
    A = np.zeros((n, n))
    b = np.random.uniform(low=v_min, high=v_max + 1, size=(n,))

    for i in range(n):
        sum = 0

        for j in range(n):
            if j >= i:
                A[i][j] = random.randint(m_min, m_max)
                A[j][i] = A[i][j]
            if i != j:
                sum += abs(A[i][j])

        A[i][i] = sum

    return A, b


def comparison(m_min, m_max, v_min, v_max, n_size, n_iter, eps=1e-10):
    A, b = random_matrix_vector(m_min, m_max, v_min, v_max, n_size)
    print(f"Numpy\n{np.linalg.solve(A, b)}")
    print(f"Jacobi method:\n{jacobi(A, b, eps, n_iter)[0]}\n\n")


if __name__ == "__main__":
    comparison(-15, 15, -10, 10, 5, 1000)

from lab9.zad_1 import *
import matplotlib.pyplot as plt
import time


def measure():
    tab1 = []
    tab2 = []
    x_axis = []
    for n in range(100, 400):
        A = np.random.randint(-10000, 10000, size=(n, n))
        b = np.random.rand(len(A))
        C = A.copy()
        d = b.copy()
        try:
            start_time_1 = time.time()
            gauss_with_pivot(A.tolist(), b.tolist())
            stop_time_1 = time.time()
            start_time_2 = time.time()
            gauss_without_pivot(C.tolist(), d.tolist())
            stop_time_2 = time.time()
            t1 = stop_time_1 - start_time_1
            t2 = stop_time_2 - start_time_2
            tab1.append(t1)
            tab2.append(t2)
            x_axis.append(n)
            print(f"{n}x{n} With pivot: {t1}")
            print(f"{n}x{n} Without pivot: {t2}\n")
        except ZeroDivisionError:
            pass
    return tab1, tab2, x_axis


tab1, tab2, x_axis = measure()

plt.plot(x_axis, tab1, 'b.', label="With pivoting")
plt.plot(x_axis, tab2, 'r.', label="Without pivoting")
plt.xlabel("Square matrix size")
plt.ylabel("Time [s]")
plt.title("Time of evaluation fro Gaussian elimination")
plt.legend()
plt.grid()
plt.show()

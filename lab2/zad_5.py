import numpy as np

print("Matrix 3x4 filled with 0's:")
print(np.zeros((3, 4)), "\n")

print("Matrix 2x6 filled with 1's:")
print(np.ones((2, 6)), "\n")

print("Matrix 4x4 filled with any number (eg. 9's):")
print(np.full((4, 4), 9), "\n")

print("Identity matrix 5x5:")
print(np.identity(5), "\n")

print("Matrix 3x5 filled with random numbers from range [-5, 5]")
A = np.random.randint(-5, 5, size=(3, 5))
print(A, "\n")

print("Evenly spaced values within a given interval:")
print(np.arange(0., 4.5, 0.5),  "\n")

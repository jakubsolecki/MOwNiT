import numpy as np
from zad2 import show_bin_and_dec


def next_float(x):
    print("Next (closest) value to {} is {}".format(x, np.nextafter(x, 1)))
    print(show_bin_and_dec(x))
    print(show_bin_and_dec(np.nextafter(x, 1)))


next_float(1.2)
next_float(1.75)
next_float(1.25)

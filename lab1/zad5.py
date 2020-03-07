import numpy as np
import bitstring as bs


def float_bin(number, places=3):
    if "." in str(number):
        whole, dec = str(number).split(".")
        whole = int(whole)
    else:
        whole = 0
        dec = str(number)

    if "e" in dec:
        e = int(dec.split("e", 1)[1])
        e = int(e)
        before_e = int(dec.split("e", 1)[0])
        dec = int(before_e**abs(e))
    else:
        dec = int(dec)

    if whole == 0:
        res = str(0) + "."
    else:
        res = bin(whole).lstrip("0b") + "."

    for x in range(places):
        whole, dec = str((decimal_converter(float(dec))) * 2).split(".")
        dec = int(dec)
        res += whole

    print("Is normalised:", is_normalised(whole))

    return res


def decimal_converter(num):
    while num >= 1:
        num /= 10
    return num


def is_normalised(number):
    return number == 1


a = np.float32(1.1)
for i in range(0, 149):
    a = a/np.float32(2.0)
    # b = bs.BitArray(float=a, length=32)
    print("Float (dec, 32-bit):", a)
    # print("FPT representation (32-bit):", b.bin)
    print("Binary repr.:", float_bin(a, 23))
    print("\n")

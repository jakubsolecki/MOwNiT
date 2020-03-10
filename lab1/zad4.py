import numpy as np
from bitstring import BitArray


def float_dec2bin(number, bits=64):
    d_bin = BitArray(float=number, length=bits)
    sign = int(d_bin[0])
    if bits == 64:
        exp = d_bin[1:12].bin
        man = d_bin[12:].bin
    elif bits == 32:
        exp = d_bin[1:9].bin
        man = d_bin[9:].bin
    else:
        exp = d_bin[1:6].bin
        man = d_bin[6:].bin

    return sign, exp, man


print("float64:", float_dec2bin(np.float64(1/10)))
print("float32:", float_dec2bin(np.float32(1/3)))
print("float16:", float_dec2bin(np.float16(1/3)))

print("float16 -> float32:", float_dec2bin(np.float32(np.float16(1/3))))
print("float32 -> float64:", float_dec2bin(np.float64(np.float32(1/3))))
print("float16 -> float64:", float_dec2bin(np.float16(np.float32(1/3))))

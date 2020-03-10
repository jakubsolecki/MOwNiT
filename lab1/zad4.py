import numpy as np


hex2bin = dict('{:x} {:04b}'.format(x, x).split() for x in range(16))


def float_dec2bin(d):
    hx = float(d).hex()
    p = hx.index('p')
    bn = ''.join(hex2bin.get(char, char) for char in hx[2:p])
    return (bn.strip('0') + hx[p:p + 2]
            + bin(int(hx[p + 2:]))[2:]).split("p")[0]


print("1/3 float to binary")
print("float64:", float_dec2bin(np.float64(1/10)))
print("float32:", float_dec2bin(np.float32(1/3)))
print("float16:", float_dec2bin(np.float16(1/3)))

print("float16 -> float32:", float_dec2bin(np.float32(np.float16(1/3))))
print("float32 -> float64:", float_dec2bin(np.float64(np.float32(1/3))))
print("float16 -> float64:", float_dec2bin(np.float16(np.float32(1/3))))

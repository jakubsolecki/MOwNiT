import numpy as np
import bitstring as bs

a=np.float32(1.1)
for i in range(0, 149):
    a=a/np.float32(2.0)
    b=bs.BitArray(float=a, length=32)
    print(a)
    # exponent = b.bin[1:9]
    # mantissa = b.bin[9:]
    # print(b.bin[0], exponent, mantissa, '\n')
    print(b.bin)



import numpy as np
import bitstring as bs


f64 = np.float64(1.0/3.0)
f32 = np.float32(1.0/3.0)
f16 = np.float16(1.0/3.0)
b64 = bs.BitArray(float=f64, length=64)
b32 = bs.BitArray(float=f32, length=32)
b16 = bs.BitArray(float=f16, length=16)

print('1/3 as float64:', b64.bin)
print('1/3 as float32:', b32.bin)
# print(b16.bin)
import numpy as np
from bitstring import BitArray


def to_binary(number):
    number_binary = BitArray(float=number, length=32)
    if number_binary[1:9].bin == '00000000':
        x = 'de'
    else:
        x = ''
    print(number)
    print(f'Is {x}normalised', int(number_binary[0]), number_binary[1:9].bin, number_binary[9:].bin, '\n')


a = np.float32(1.1)
for i in range(0, 149):
    a = a/np.float32(2.0)
    to_binary(a)

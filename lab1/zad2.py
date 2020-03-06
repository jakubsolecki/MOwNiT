import bitstring as bs
from tabulate import tabulate

def show_bin_and_dec(number):
    float64 = bs.BitArray(float=number, length=64)
    exponent = float64.bin[1:12]
    mantissa = float64.bin[12:]

    if float64[0] == 1:
        sign = '-'
    else:
        sign = '+'

    exponent_dec = 0
    pow = 10
    for i in exponent[0:]:
        if i == '1':
            exponent_dec += 2 ** pow
        pow -= 1

    pow = -1
    mantissa_dec = 0
    for i in mantissa[0:]:
        if i == '1':
            mantissa_dec += 2 ** pow
        pow -= 1

    table = [[float64.bin[0], exponent, mantissa], [sign, exponent_dec, mantissa_dec]]
    print('Floating point numbers (64-Bit):', '\n')
    print('number (dec) = sign (1 + mantissa) x 2 ** (exponent - 1023)')
    print(number, '(dec) =', sign, f'(1 + {mantissa_dec}) x 2 ** ({exponent_dec} - 1023) = '
                                   f'{sign}{1 + mantissa_dec} x 2 ** {exponent_dec - 1023}', '\n')
    print(tabulate(table, headers=['Sign', 'Exponent', 'Mantissa']))

show_bin_and_dec(13.25)
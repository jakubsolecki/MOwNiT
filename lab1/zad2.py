import bitstring as bs


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

    # print('Floating point numbers (64-Bit):')
    print('number (dec) = sign (1 + mantissa) x 2 ** (exponent - 1023)')
    print(number, '(dec) =', sign, f'(1 + {mantissa_dec}) x 2 ** ({exponent_dec} - 1023) = '
                                   f'{sign}{1 + mantissa_dec} x 2 ** {exponent_dec - 1023}')
    print("Sign Exponent Mantissa")
    print(float64.bin[0], exponent, mantissa)
    print(sign, exponent_dec, mantissa_dec, '\n')


show_bin_and_dec(1.2)
show_bin_and_dec(1.75)
show_bin_and_dec(1.25)

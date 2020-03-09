import numpy as np


def float_bin(number, places=23):
    # if "." in str(number):
    #     whole, dec = str(number).split(".")
    #     whole = int(whole)
    # else:
    #     whole = 0
    #     dec = str(number)

    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = int(dec)

    # print(dec)

    # if "e" in dec:
    #     # e = int(dec.split("e", 1)[1])
    #     # e = int(e)
    #     # before_e = int(dec.split("e", 1)[0])
    #     before_e, e = dec.split("e")
    #     before_e = str(int(before_e))
    #
    #     if whole != 0:
    #         before_e = str(whole) + before_e
    #         print(before_e)
    #
    #     # before_e = int(before_e)
    #     e = int(e)
    #     # dec = int(before_e**abs(e))
    #     dec = int(("0" * abs(e)) + before_e)
    # else:
    #     dec = int(dec)

    # if whole == 0:
    #     res = str(0) + "."
    # else:
    #     res = bin(whole).lstrip("0b") + "."

    # res = bin(whole).lstrip("0b") + "."
    res = "0."

    for x in range(places):
        whole, dec = str((decimal_converter(np.float32(dec))) * 2).split(".")
        dec = int(dec)
        res += whole

    return res


def decimal_converter(num):
    while num > 1:
        num /= 10
    return num


# def is_normalised(num):
#     _, dec = str(num).split(".")
#     return dec[0] == "1"


a = np.float32(1.1)
for i in range(0, 149):
    a = a/np.float32(2.0)
    print("Float (dec, 32-bit):", a)
    binary = float_bin(a, 23)
    print("Binary repr.:", binary)
    # print("Is normalised:", is_normalised(binary))
    print("\n")

def floatoctal_convert(my_number, places = 3):
   my_whole, my_dec = str(my_number).split(".")
   my_whole = int(my_whole)
   my_dec = int (my_dec)
   res = bin(my_whole).lstrip("0b") + "."
   for x in range(places):
      my_whole, my_dec = str((my_decimal_converter(my_dec)) * 8).split(".")
      my_dec = int(my_dec)
      res += my_whole
   return res
def my_decimal_converter(num):
   while num > 1:
      num /= 10
   return num
# Driver Code
n = input("Enter floating point value : \n")
p = int(input("Enter the number of decimal places of the result : \n"))
print(floatoctal_convert(n, places = p))
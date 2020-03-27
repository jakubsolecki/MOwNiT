from lab3.zad_1 import to_table
from lab3.zad_3 import lagrange_interpolation, to_chart, cmp_inbetween_points
import math

def comparison(min, max, n):
    x_sqrt, y_sqrt, sqrt_tab = to_table(min, max, n, math.sqrt, "sqrt(x)")
    x_sin, y_sin, sin_tab = to_table(min, max, n, math.sin, "sin(x)")
    f = lambda x: x ** 3 + 2 * x
    x_f, y_f, f_tab = to_table(min, max, n, f, "x^3 + 2x")

    sqrt_approx = lambda x: lagrange_interpolation(x_sqrt, y_sqrt, x)
    sin_approx = lambda x: lagrange_interpolation(x_sin, y_sin, x)
    f_approx = lambda x: lagrange_interpolation(x_f, y_f, x)

    print(sqrt_tab)
    cmp_inbetween_points(min, max, n, math.sqrt, sqrt_approx, "sqrt(x)")
    to_chart(min, max, 1000, math.sqrt, sqrt_approx, "sqrt(x)")

    print(sin_tab)
    cmp_inbetween_points(min, max, n, math.sin, sin_approx, "sin(x)")
    to_chart(min, max, 1000, math.sin, sin_approx, "sin(x)")

    print(f_tab)
    cmp_inbetween_points(min, max, n, f, f_approx, "x^3 + 2x")
    to_chart(min, max, 1000, f, f_approx, "x^3 + 2x")


# comparison(0, 10, 7)

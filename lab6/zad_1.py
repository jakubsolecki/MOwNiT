def rectangle_rule(fun, a, b, n):
    total = 0.0
    dx = float(b - a)/n
    for k in range(0, n):
        total += fun(a + k*dx)
    return dx*total


def trapezoidal_rule(fun, a, b, n):
    total = 0.0
    dx = float(b - a)/n
    total += fun(a)/2.0
    for i in range(1, n):
        total += fun(a + i*dx)
    total += fun(b)/2.0
    return dx * total


def simpson_rule(fun, a, b, n):
    total = 0.0
    dx = float(b - a)/n
    x = a + dx
    for i in range(1, int(n/2 + 1)):
        total += 4*fun(x)
        x += 2*dx

    x = a + 2*dx
    for i in range(1, int(n/2)):
        total += 2*fun(x)
        x += 2*dx
    return (dx/3)*(fun(a) + fun(b) + total)

from math import sqrt


def delta(x, y, z):
    return y**2 - 4 * x * z


def raizes(a, b, c):
    determinante = delta(a, b, c)
    x1 = complex(-b / (2 * a), sqrt(abs(determinante)) / (2 * a))
    x2 = x1.conjugate()
    if determinante >= 0:
        x1 = x1.real + x1.imag
        x2 = x2.real + x2.imag
    return x1, x2

from math import sqrt


def delta(x, y, z):
    return y**2 - 4 * x * z


def raizes(a, b, c):
    determinante = delta(a, b, c)
    x1 = (-b + sqrt(determinante)) / (2 * a)
    x2 = (-b - sqrt(determinante)) / (2 * a)
    return x1, x2

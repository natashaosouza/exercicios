import math

V0 = 10
a = 2.5
z = 4 * 1/3


def V(V0, a, z):
    return V0 * (1 - z / math.sqrt(a**2 + z**2))


print(V(V0, a, z))

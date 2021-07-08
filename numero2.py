import math

V0 = 10
a = 2.5
z = 4 * 1/3

V = V0 * (1 - z / math.sqrt(a**2 + z**2))
print(V)

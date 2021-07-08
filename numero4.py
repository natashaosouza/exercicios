from math import sqrt

a, b, c = 1, 1, 0
delta = b**2 - 4 * a * c

x1 = (-b + sqrt(delta)) / (2 * a)
x2 = (-b - sqrt(delta)) / (2 * a)

print(x1, x2)

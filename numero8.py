from math import pi, sin

raio = 0.5
lados = (3, 4, 5, 100, 10_000, 1_000_000)

def func_1(pi, n):
    return pi / n

for n in lados:
    perimetro = 2 * n * raio * sin(func_1)
    print(perimetro)
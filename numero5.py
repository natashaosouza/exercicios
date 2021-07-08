from math import pi, sin

raio = 0.5
lados = (3, 4, 5, 100, 10_000, 1_000_000)

for n in lados:
    perimetro = 2 * n * raio * sin(pi / n)
    print(perimetro)

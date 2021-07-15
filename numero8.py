from math import pi, sin

raio = 0.5
lados = (3, 4, 5, 100, 10_000, 1_000_000)


def perimetro(numero_de_lados):
    return 2 * numero_de_lados * raio * sin(pi / numero_de_lados)


for n in lados:
    print(perimetro(n))

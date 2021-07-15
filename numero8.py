from numpy import pi, sin, array

raio = 0.5
lados = (3, 4, 5, 100, 10_000, 1_000_000)


def perimetro(numero_de_lados):
    """Calcula o perímetro para um dado número de lados
    numero_de_lados : int, float, lista, tupla
    return : float ou array
    """
    return 2 * array(numero_de_lados) * raio * sin(pi / array(numero_de_lados))


print(perimetro(lados))
print(perimetro(10))

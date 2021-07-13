# Equação do segundo grau
from math import sqrt

a = int(input("Digite o valor do coeficiente a: "))
b = int(input("Digite o valor do coeficiente b: "))
c = int(input("Digite o valor do coeficiente c: "))

delta = b**2 - 4 * a * c

def raizes (x1, x2):
    x1 = (-b + sqrt(delta)) / 2*a
    x2 = (-b - sqrt(delta)) / 2*a
    return x1, x2


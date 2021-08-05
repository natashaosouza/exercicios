import pint
GRAVIDADE = 9.8   # m/s^2

ureg = pint.UnitRegistry()

# altura_inicial = 1.6   # m
# velocidade_inicial = 14.2   # m/s
# tempo = 0.5  # s


@ureg.wraps('m', ('m', 'm / s', 's'), strict=False)
def altura(altura_inicial, velocidade_inicial, tempo):
    return altura_inicial + velocidade_inicial * tempo - 1/2 * GRAVIDADE * tempo**2


@ureg.wraps('m / s', ('m / s', 's'), strict=False)
def velocidade(velocidade_inicial, tempo):
    return velocidade_inicial - GRAVIDADE * tempo

# print(altura)
# print(velocidade)

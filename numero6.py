import pint

ureg = pint.UnitRegistry()


@ureg.wraps('m / s', ('m', 's'))
def velocidade_media(distancia, tempo):
    """Calcula a velocidade media a partir de distancia e tempo.

    Parâmetros:
    ----------
    distancia : int ou float
    tempo : int ou float

    Saída:
    ------
    velocidade media : float
    """
    return distancia / tempo


x = input("Forneça um valor de distância com a unidade: ")
t = input("Forneça um valor de tempo com a unidade: ")

resultado = velocidade_media(x, t)

print(f"A velocidade média é {resultado:.3f~P}")

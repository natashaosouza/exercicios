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


x = float(input("Forneça um valor de distância: "))
t = float(input("Forneça um valor de tempo: "))

resultado = velocidade_media(x, t)

print(f"A velocidade média é {resultado:.3f}")

GRAVIDADE = 9.8   # m/s^2

altura_inicial = 1.6   # m
velocidade_inicial = 14.2   # m/s
tempo = 0.5  # s

altura = altura_inicial + velocidade_inicial * tempo - 1/2 * GRAVIDADE * tempo**2
velocidade = velocidade_inicial - GRAVIDADE * tempo

print(altura)
print(velocidade)

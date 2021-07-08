import numpy

Velocidade_inicial = 10    # m/s
a = 2.5
z = 4 * (1/3)

V = Velocidade_inicial * numpy.sqrt (1 - (z /(a**2 + z**2)))
print(V) 

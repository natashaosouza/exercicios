import numpy 

log_de_dois = numpy.log(2)  
raiz_de_cinco = numpy.sqrt(5)

letra_b = (1 - (1 + log_de_dois ** -3.5)) / 1 + raiz_de_cinco


numerador = 2 - numpy.sqrt(2)
denominador = 2 + numpy.sqrt(2)

letra_c = numpy.sin(numerador / denominador)

print( letra_b , letra_c)
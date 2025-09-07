# Algoritmo que faz um calculo com base em uma fórmula matemática

# Módulos
from math import sqrt

# Variáveis
diagonal = 0
x1 = y1 = x2 = y2 = 0

# Procedimentos, Funções ou Rotinas
def solicitarValorDeVariavel(nome):
    valor = 0
    valor = int(input("Valor de {} : ".format(nome)))
    return valor

# Entradas
x1 = solicitarValorDeVariavel("x1")
y1 = solicitarValorDeVariavel("y1")
x2 = solicitarValorDeVariavel("x2")
y2 = solicitarValorDeVariavel("y2")

# Calculo
d = (x2-x1)**2 + (y2-y1)**2
d = sqrt(d)

# Saída
print ("O valor da diagonal é {:.3f}".format(d))
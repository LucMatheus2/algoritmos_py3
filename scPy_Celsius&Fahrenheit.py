# Algoritmo conversor de Celsius para Fahrenheit

# Variáveis
temperaturaF = 0
temperaturaC = 0

# Funcao
def conversorParaF(tempC):
    tempF = (9/5)*tempC + 32
    return tempF

# Entrada
temperaturaC = input("Qual a temperatura em C : ")
temperaturaC = float(temperaturaC)

# Calculo
temperaturaF = conversorParaF(temperaturaC)

# Saída
print("A temperatura em Fahrenheit é {:.1f} F".format(temperaturaF))
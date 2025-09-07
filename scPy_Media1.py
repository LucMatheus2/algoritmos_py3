# Algoritmo que é usado de média para calculos aritméticos

# Variaveis e Constantes
numeros = [] # Vetor de float
pesos = [2,3,5] # Vetor de int
media = 0
LIMITE = 3

# Procedimentos
def limitarValoresDasNotas(nota,min=0,max=10):
    if (nota < min):
        nota = min
    elif (nota > max):
        nota = max

# Entrada
for i in range(LIMITE):
    numeros_i = float(input("Avaliação {}ªava : ".format(i+1)))
    limitarValoresDasNotas(numeros_i)
    numeros.insert(i,numeros_i)

# Calculos
for i in range(LIMITE):
    media += numeros[i] * pesos[i]
media /= 10

# Saída
print("A média é {:.1f}".format(media))
# Algoritmo que faz a faixa de natação

# Variáveis
idade = -1
classificacao = ""

# Entrada
idade = input("Qual a sua idade? : ")
idade = int(idade)

# Processamento
if 5 <= idade <= 7:
    classificacao = "Infantil A"
elif 8 <= idade <= 10:
    classificacao = "Infantil B"
elif 11 <= idade <= 13:
    classificacao = "Juvenil A"
elif 14 <= idade <= 17:
    classificacao = "Juvenil B"
elif idade >= 18:
    classificacao = "Adulto"
else:
    classificacao = "OOO"

# Saída
print("A sua arraia é o {}".format(classificacao))
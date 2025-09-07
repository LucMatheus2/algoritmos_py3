'''
Algoritmo de classificação de natação
@autor Lucas Matheus <lucasmccosta@outlook.com.br>
'''
# Variaveis
idadeNadador = 0

# Função
def classificarNadador(idade):
    classificacao=""
    if 5 <= idade <= 7:
        classificacao = "Infantil A"
    elif 8 <= idade <= 10:
        classificacao = "Infantil B"
    elif 11 <= idade <= 13:
        classificacao = "Juvenil A"
    elif 14 <= idade <= 17:
        classificacao = "Juvenil B"
    elif 18 <= idade <= 30:
        classificacao = "Adulto"
    elif 31 <= idade <= 50:
        classificacao = "Master"
    else:
        classificacao = "_"
    return classificacao

# Entrada
idadeNadador = input("Qual a sua idade? : ")
idadeNadador = int(idadeNadador)

# Saída
print("Classificação : {}".format(classificarNadador(idadeNadador)))
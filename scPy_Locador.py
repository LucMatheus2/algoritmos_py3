# Algoritmo da calculadora de custo

# Subrotinas

# Calculo de porcentagem
def porC(numero):
    LIMITE = 100

    if (numero > LIMITE):
        numero = LIMITE
    elif numero < 0:
        numero = 0

    return float(numero/100)

def ImpressaoDeTextoDoRelatorio(titulo,variavel):
    print(titulo," : R$ {:.2f}".format(variavel))

# Variaveis
precoCarroNovo = 0
custoFabril = 0
porcentagemDoDistribuidor = porC(28)
alicotaDeImpostos = porC(45)

# Entrada
custoFabril = float( input("Quanto custa produzir um carro novo? : ") )

# Calculo
precoCarroNovo = custoFabril + (custoFabril * porcentagemDoDistribuidor) + (custoFabril * alicotaDeImpostos)

# Saída
print("=== RELATÓRIO DO NOVO CARRO ===")
ImpressaoDeTextoDoRelatorio("Custo de Produção",custoFabril)
ImpressaoDeTextoDoRelatorio("Distribuição",custoFabril*porcentagemDoDistribuidor)
ImpressaoDeTextoDoRelatorio("Tributos",custoFabril*alicotaDeImpostos)
ImpressaoDeTextoDoRelatorio("Valor Total",precoCarroNovo)
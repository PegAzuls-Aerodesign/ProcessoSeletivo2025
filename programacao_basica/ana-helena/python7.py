#9. Crie uma estrutura (pode ser uma lista de dicionários) para representar várias configurações
#de aeromodelo, incluindo nome, envergadura, peso e empuxo. Depois, mostre como filtrar
#apenas aquelas com empuxo maior que X.

# Criação da lista de dicionários com os aeromodelos
aeromodelos = [
    {"nome": "Aero1", "envergadura": 3.0, "peso": 1200, "empuxo": 1000},
    {"nome": "Aero2", "envergadura": 1.9, "peso": 1000, "empuxo": 500},
    {"nome": "Aero3", "envergadura": 3.3, "peso": 1300, "empuxo": 2000},
    {"nome": "Aero4", "envergadura": 1.0, "peso": 1800, "empuxo": 3100}
]

# Limite de empuxo
limite_de_empuxo = 1500

# Filtro de empuxo (Maior empuxo)
filtro = []

for modelo in aeromodelos:
    if modelo["empuxo"] > limite_de_empuxo:
        filtro.append(modelo)

# Mostrando resultados na tela
print("Aeromodelos com valor de empuxo maior que", limite_de_empuxo, ":")
for modelo in filtro:
    print(modelo["nome"], "--> Empuxo:", modelo["empuxo"])
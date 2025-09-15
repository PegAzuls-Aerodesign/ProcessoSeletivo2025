planes = [] # lista de dicionários

for i in range(4): # para 4 aeromodelos
    nome = input("Digite o nome do aeromodelo: ")
    enver = input("Digite a envergadura do aeromodelo (em metros): ")
    peso = float(input("Digite o peso do aeromodelo (em kg): "))
    empuxo = float(input("Digite o empuxo do aeromodelo (em Newtons): "))

    #depois de ler os dados, criar um dicionário e adicionar na lista
    dic = {
        "nome": nome,
        "envergadura": enver,
        "peso": peso,
        "empuxo": empuxo
    }
    planes.append(dic) #adiciona o dicionário na lista
    print("_______________________________")

x = float(input("qual o empuxo mínimo que você quer filtrar?(em Newtons): "))
for i in range(len(planes)):
    if planes[i]["empuxo"] > x: #filtra apenas os com empuxo adequado
        print("O aeromodelo:", planes[i]["nome"], "tem empuxo adequado, mais de", x, "N.")
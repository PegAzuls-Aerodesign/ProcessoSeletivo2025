AoA = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] #Ângulos de ataque em graus
aList = [] #lista de dicionários

for i in range(len(AoA)):
    cL = 0.1 * AoA[i] #Cálculo do coeficiente de sustentação
    cD = 0.01 * AoA[i] + 0.02 #Cálculo do coeficiente de arrasto
    Ef = cL / cD #Cálculo da eficiência aerodinâmica
    dic = {
        "AoA": AoA[i],
        "cL": cL,  
        "cD": cD,
        "Eficiência": Ef
    }
    aList.append(dic) #Adiciona o dicionário na lista

for i in range(len(aList)):
    angle = str(aList[i]["AoA"]) + "º," #Formata o ângulo com o símbolo de grau, conforme o output esperado
    if aList[i]["Eficiência"] < 5: #Verifica se a eficiência é menor que 5
        print("Ângulo:", angle, "Ef:", round(aList[i]["Eficiência"], 2), "- Baixa eficiência.")
    else:
        print("Ângulo:", angle, "Ef:", round(aList[i]["Eficiência"], 2))
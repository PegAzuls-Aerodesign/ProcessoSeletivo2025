# Questão 8

# Lista com os ângulos de ataque
angulos = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Dicionário para armazenar a eficiência aerodinâmica  
eficiencias = {}

# Loop para calcular CL, CD, Ef
for angulo in angulos:
    CL = 0.1 * angulo
    CD = 0.01 * angulo + 0.02
    Ef = CL / CD
    eficiencias[angulo] = Ef

# Resultados com o aviso de baixa eficiência
for angulo, Ef in eficiencias.items():
    print("Ângulo: {}°, Ef: {:.2f}".format(angulo, Ef))
    if Ef < 5:
        print(" → Baixa eficiência")
    else:
        print()
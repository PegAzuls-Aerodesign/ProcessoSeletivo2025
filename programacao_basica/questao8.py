angulos = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
resultados = {}

for angulo in angulos:
    CL = 0.1 * angulo
    CD = 0.01 * angulo + 0.02
    Ef = CL / CD
    resultados[angulo] = Ef

for angulo, eficiencia in resultados.items():
    print(f"Ângulo: {angulo}° → Ef: {eficiencia:.2f}")
    if eficiencia < 5:
        print("<- Baixa eficiência")
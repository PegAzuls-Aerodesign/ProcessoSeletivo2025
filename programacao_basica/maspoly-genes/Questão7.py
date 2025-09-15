limite = 0.05
coeficiente_de_arrasto = float(input("Digite o coeficiente de arrasto do aeromodelo: "))
if coeficiente_de_arrasto > limite:
    print("Isso não é seguro.")
    print("Cuidado!")
else:
    print("Isso é seguro.")

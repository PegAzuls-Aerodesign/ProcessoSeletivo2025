pesos = {
    "motor": 1.5,  # em kg
    "asa": 0.5,    # em kg
    "bateria": 0.3  # em kg
}
componentes = ["motor", "asa", "bateria"]
soma = 0
for i in range(len(componentes)):
    soma += pesos[componentes[i]]
print("O peso total do aeromodelo é:", soma, "kg")
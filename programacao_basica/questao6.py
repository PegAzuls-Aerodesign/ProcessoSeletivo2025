componentes = ["motor", "asa", "bateria"]
pesos = {"motor": 50, "asa": 30, "bateria": 20}
total = 0 
for componente in componentes:
    total = total + pesos[componente]
    print("Preço total:", total)
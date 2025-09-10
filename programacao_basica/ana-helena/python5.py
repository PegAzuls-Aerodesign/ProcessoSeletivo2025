#6. Suponha que você tenha uma lista com vários componentes de um aeromodelo (ex:
#componentes = [“motor”, “asa”, “bateria”] e um dicionário de pesos. Escreva
#um trecho de código que calcule o peso total percorrendo essa lista e somando os pesos.

# Criação da lista de componentes
componentes = ["motor", "asa", "bateria"]

# Dicionário com os pesos 
pesos = {
    "motor":  float( input('Insira o valor do peso do motor: '))
,
    "asa": float( input('Insira o valor do peso da asa: '))
,
    "bateria": float( input('Insira o valor do peso da bateria: '))

}

# Definição da variável

peso_total = 0

# Percorre a lista e somar os pesos
for item in componentes:
    peso_total += pesos[item]

# Resultado final
print("O peso total do aeromodelo é:", peso_total, "kg")
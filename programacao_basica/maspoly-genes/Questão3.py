# Velocidade máxima do aeromodelo em km/h
velocidade_maxima = float(input("Digite a velocidade máxima do aeromodelo (em km/h): "))

if velocidade_maxima > 200:
    print("O aeromodelo é rápido.")
elif 100 <= velocidade_maxima <= 200:
    print("O aeromodelo é normal.")
else:
    print("O aeromodelo é lento.")
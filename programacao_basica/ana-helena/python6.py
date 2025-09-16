#7. No aerodesign, se o coeficiente_de_arrasto ultrapassar o limite seguro (por exemplo, 0.05),
#devemos ativar um protocolo de aviso. Como seria essa verificação em Python?

# Criação de atributos 
forca_de_arrasto = float( input('Insira o valor da força de arrastor: '))        # força de arrasto (em N)
densidade_ar = float( input('Insira o valor da densidade do ar: '))              # densidade do ar (em kg/m³)
velocidade = float( input('Insira o valor da velocidade: '))                     # velocidade (em m/s)
area = float( input('Insira o valor da área de referência: '))                   # área de referência (em m²)

# Cálculo do coeficiente de arrasto
coeficiente_de_arrasto = (2 * forca_de_arrasto) / (densidade_ar * (velocidade**2) * area)

print('Coeficiente de arrasto:', round(coeficiente_de_arrasto, 3))

if coeficiente_de_arrasto > 0.05:
    print('ALERTA! Coeficiente de arrasto maior que 0.05!')
else:
    print('Coeficiente de arrasto aprovado!')
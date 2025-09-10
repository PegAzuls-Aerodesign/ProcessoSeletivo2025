## Questão 3
## 3. Suponha que você tenha uma variável velocidade_maxima. Escreva um trecho de
## código que verifica se ela excede 200 km/h e imprime uma mensagem diferente em cada caso.


# Criação de variáveis
velocidade_maxima = int(input('Insira a velocidade máxima: '))     ## Peso do planador


if velocidade_maxima > 200:                                        ## Velocidade maior que 200km/h
    print('Velocidade máxima maior que 200 km/h')
    print('Velocidade: ', velocidade_maxima, 'km/h')
elif velocidade_maxima == 200:                                     ## Velocidade igual a 200km/h
    print('Velocidade máxima igual a 200 km/h')
    print('Velocidade:', velocidade_maxima, 'km/h')
else:                                                              ## Velocidade menor que 200km/h
    print('Velocidade máxima menor que 200 km/h')
    print('Velocidade:', velocidade_maxima, 'km/h')


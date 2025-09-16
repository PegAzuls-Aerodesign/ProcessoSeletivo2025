## Questão 4
## 4. Imagine que você esteja simulando cinco voltas de um aeromodelo. Escreva um loop for
## em Python que repita uma ação (como imprimir “Volta X”) cinco vezes.

# Criação de dicionário
aeromodelo = {
    "asa": int( input('Insira o valor da asa: ')),
    "peso": int( input('Insira o peso: ')),         
    "motor": int( input('Insira o valor do peso do motor: ')),         
}

## Para acessar o valor do pessoa é necessário 
## referenciar primeiro o nome do dicionário, abrir [] e por último indicar o parâmetro escolhido
print('Valor do peso:', aeromodelo["peso"])  

class Motor:
    """Representa a parte 'Motor'."""
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia}cv ligado.")

class Carro:
    """Representa o todo 'Carro'."""
    def __init__(self, modelo, potencia_motor):
        # A Composição acontece aqui!
        # O objeto Motor é CRIADO DENTRO do construtor de Carro.
        # Ele não é recebido de fora.
        self.modelo = modelo
        self.motor = Motor(potencia_motor) # <-- O Motor é PARTE-DE Carro

    def descrever(self):
        print(f"Este é um {self.modelo}.")
        self.motor.ligar()

# Ao criar um Carro, o Motor é automaticamente criado junto.
meu_fusca = Carro("Fusca", 50)
meu_fusca.descrever()

# Você não tem acesso a 'meu_fusca.motor' como uma entidade separada
# antes de criar o carro. Se 'meu_fusca' for deletado, seu motor se vai junto.
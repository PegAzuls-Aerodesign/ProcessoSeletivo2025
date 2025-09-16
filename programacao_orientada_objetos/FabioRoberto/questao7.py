from abc import ABC, abstractmethod

class Aeronave:
    def __init__(self, nome, peso_vazio_kg, carga_paga_kg):
        self.nome = nome
        self.peso_vazio_kg = peso_vazio_kg
        self.carga_paga_kg = carga_paga_kg

class Critério(ABC):
    @abstractmethod
    def calcular_pontos(self, aeronave):
        pass

class CritérioCargaPaga(Critério):
    def calcular_pontos(self, aeronave):
        return aeronave.carga_paga_kg * 10

class CritérioLeveza(Critério):
    def calcular_pontos(self, aeronave):
        return max(0, 100 - (aeronave.peso_vazio_kg * 5))

class CalculadoraDePontuacao:
    def calcular_pontuacao_final(self, aeronave, criterios):
        total = 0
        for critério in criterios:
            total += critério.calcular_pontos(aeronave)
        return total

class CritérioVelocidade(Critério):
    def calcular_pontos(self, aeronave):
        return aeronave.carga_paga_kg * 0.5

if __name__ == "__main__":
    # Criação de uma aeronave
    aeronave = Aeronave("X-1", 100, 50)
    
    criterios_iniciais = [
        CritérioCargaPaga(),
        CritérioLeveza()
    ]
    calculator = CalculadoraDePontuacao()
    total_inicial = calculator.calcular_pontuacao_final(aeronave, criterios_iniciais)
    print(f"Pontuação inicial: {total_inicial}")
    
    criterios_expandidos = [
        CritérioCargaPaga(),
        CritérioLeveza(),
        CritérioVelocidade()
    ]
    total_expandido = calculator.calcular_pontuacao_final(aeronave, criterios_expandidos)
    print(f"Pontuação expandida: {total_expandido}")
    
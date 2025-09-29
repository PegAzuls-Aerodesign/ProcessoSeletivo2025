# Classe pai
class Aeronave:
    def __init__(self, nome: str, carga_vazia_kg: float, carga_paga_kg: float):
        self.nome = nome
        self.carga_vazia = carga_vazia_kg
        self.carga_paga = carga_paga_kg

# alcula a pontuação da parte do CargaPaga
class CargaPaga(Aeronave):
    def rate(self):
        return self.carga_paga * 10
    
# Calcula a pontuação da parte da Levesa
class Levesa(Aeronave):
    def rate(self):
        return max(0, 100 - (self.carga_vazia * 5))
    
# Nova parte que deveríamos adcionar    
class EficienciaEstrutural(Aeronave):
    def rate(self):
        return (self.carga_paga/self.carga_vazia) * 20
    
class Calculadora: # Calcula a eficiência com base nas outras pontuações, de modo modular
    def __init__(self, aeronaves: list[Aeronave]):
        self.aeronaves = aeronaves

    def calcular_total(self):
        total = 0
        for aeronave in self.aeronaves:
            total += aeronave.rate()
        return total
    
dadosDic = {
    "nome": "Teste",
    "carga_vazia": 1,   # Dados da aeronave que será avaliada
    "carga_paga": 8
}

dadosAeronave = [CargaPaga(*dadosDic.values()), Levesa(*dadosDic.values()), 
                 EficienciaEstrutural(*dadosDic.values())] # Cria a lista com as classes que serão usadas
calcular = Calculadora(dadosAeronave) # Cria um objeto da lista
print(f"A eficiencia do avião {dadosDic['nome']} é", calcular.calcular_total())


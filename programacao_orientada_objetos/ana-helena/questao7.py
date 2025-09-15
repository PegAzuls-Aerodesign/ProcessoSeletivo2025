# Classe Mãe, recebe os valores das variáveis 
class Aeronave:
    def __init__(self, nome: str, carga_vazia: float, carga_paga: float):
        self.nome = nome
        self.carga_vazia = carga_vazia
        self.carga_paga = carga_paga

# Classe (Filha) resonsável por calcular o critério Carga Paga
class CriterioCargaPaga(Aeronave):
    def rate(self):
        return self.carga_paga * 10

# Classe (Filha) resonsável por calcular o critério Leveza
class CriterioLeveza(Aeronave):
    def rate(self):
        return max(0, 100 - self.carga_vazia * 5)

# Classe responsável por calcular o valor total
class Calculadora:
    # Função que recebe os valores das variáveis da lista
    def __init__(self, aeronaves: list[Aeronave]):
        self.aeronaves = aeronaves

# Função que calcula o valor total de eficiência
    def calcularTotal(self):
        total = 0
        for aeronave in self.aeronaves:
            total += aeronave.rate() 
        return total

# -- Função principal --
def Iniciar():
    nome = input("Nome do avião: ")
    carga_vazia = float(input("Peso vazio (kg): "))
    carga_paga = float(input("Carga paga (kg): "))

    aeronaves = [
        CriterioCargaPaga(nome, carga_vazia, carga_paga),
        CriterioLeveza(nome, carga_vazia, carga_paga)
    ]

    calc = Calculadora(aeronaves)
    eficiencia = calc.calcularTotal()

    print(f"A eficiência do avião {nome} é {eficiencia:.2f}")

# -- Chamando a função principal --
Iniciar()

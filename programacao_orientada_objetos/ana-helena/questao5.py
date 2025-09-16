
# -- Criação da classe com os dados dos funcionários --
class dados_funcionario:

    # -- Método com os atributos de cada funcinário --
    def __init__(self, nome: str, grossSalary: float, tax: float ):
        self.nome = nome
        self.grossSalary = grossSalary
        self.tax = tax

    # -- Método para calcular o salário líquido do funcionário -- 
    def __NetSalary(self):
        return float(self.grossSalary - (self.grossSalary * self.tax/100))
    
    # -- Método para calcular o salário pós aumento --
    def __IncreaseSalary(self, percentage: float) -> None:
        self.grossSalary += self.grossSalary * (percentage/100)
        

# -- Programa Principal --
nome = input("Insira seu nome: ")
grossSalary = float(input("Insira seu salário bruto: "))
tax = float(input("Insira seu imposto em porcentagem: "))

# -- Criação do novo objeto dentro da classe dados_funcionário --
funcionario0 = dados_funcionario(nome, grossSalary, tax)

# -- Demonstração --
print("Nome: ", funcionario0.nome)
print("Salário Bruto: ", funcionario0.grossSalary)
print("Salário líquido: ", funcionario0.NetSalary()) 
funcionario0.IncreaseSalary(10)
print("Novo salário: ", funcionario0.grossSalary)





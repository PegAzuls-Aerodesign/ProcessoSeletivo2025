class Employee:
    def __init__(self, name, gross_salary, tax):
        self.Name = name
        self.GrossSalary = gross_salary
        self.Tax = tax

    def NetSalary(self):
        return self.GrossSalary - self.Tax

    def IncreaseSalary(self, percentage):
        self.GrossSalary *= (1 + percentage / 100)

# Leitura dos dados
name = input("Digite o nome do funcionário: ")
gross = float(input("Digite o salário bruto: "))
tax = float(input("Digite o imposto: "))

# Criando objeto Employee
employee = Employee(name, gross, tax)

# Exibindo dados iniciais
print("\nDados do funcionário:")
print(f"Nome: {employee.Name}")
print(f"Salário Líquido: R$ {employee.NetSalary():.2f}")

# Aumento de salário
percentage = float(input("\nDigite a porcentagem de aumento: "))
employee.IncreaseSalary(percentage)

# Exibindo dados atualizados
print("\nDados atualizados do funcionário:")
print(f"Nome: {employee.Name}")
print(f"Salário Líquido: R$ {employee.NetSalary():.2f}")
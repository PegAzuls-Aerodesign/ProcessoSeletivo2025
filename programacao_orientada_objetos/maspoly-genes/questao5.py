class funcionario:
    def __init__(self, name: str, grossSalary: float, tax: float):
        self.name = name
        self.__grossSalary = grossSalary # Atributo privado, não pode ser acessado fora da classe, apenas por métodos da classe
        self.tax = tax

    # Função para calcular o salário líquido
    def netSalary(self):
        return self.__grossSalary - (self.tax / 100 * self.__grossSalary)
    
    # Função para aumentar o salário em uma porcentagem
    def increaseSalary(self, percentage: float):
        self.__grossSalary += (percentage / 100 * self.__grossSalary)
        return self.__grossSalary

    # Função para mostrar os dados do funcionário ou para receber os dados do funcionário
    def bio(self, do: str):
        if do == "print":
            print("O nome do funcionário é: ", self.name)
            print(f"O salário líquido do funcionário é: R${self.netSalary()}")
        elif do == "input":
            self.name = input("O nome do funcionário é: ")
            self.__grossSalary = float(input("O salário bruto do funcionário é: "))
            self.tax = float(input("O imposto do funcionário é, em %: "))

# Criando um objeto da classe funcionario e exibindo os dados
fun1 = funcionario("Nome", 0, 0)
fun1.bio("input")
fun1.bio("print")

# Aumento do salário
percentage = float(input("Qual a porcentagem de aumento do salário? "))
fun1.increaseSalary(percentage)

# Mostrar os dados atualizados
fun1.bio("print")






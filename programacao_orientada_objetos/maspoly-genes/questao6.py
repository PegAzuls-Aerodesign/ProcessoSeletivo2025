# Classe base para produtos comuns, usados e importados
class productComum:
    def __init__(self, name: str, price: float):
        self.name = name
        self.__price = price # Atributo privado, não pode ser acessado fora da classe, apenas por métodos da classe

    # Função para mostrar os dados do produto ou para receber os dados do produto
    def bio(self, do: str):
        if do == "print":
            print(self.name, end=" ")
            print(f"R${round(self.__price, 2)}", end=" ")
        elif do == "input":
            self.name = input("Nome: ")
            self.__price = float(input("Preço: "))

# Produto usado herda de produto comum       
class productUsed(productComum):
    def __init__(self, name: str, price: float, manufactureDate: str):
        # Herdando os atributos da classe mãe e adicionando o atributo manufactureDate
        super().__init__(name, price)
        self.name = name + " (Usado)" # Adiciona a tag "(Usado)" ao nome do produto
        self.manufactureDate = manufactureDate

    # Função herdada, mas com adição de data de fabricação
    def bio (self, do: str):
        super().bio(do)
        if do == "print": 
            print(f"(Data de fabricação: {self.manufactureDate})", end=" ")
        elif do == "input":
            self.manufactureDate = input("Data de fabricação (DD/MM/AAAA): ")

# Produto importado herda de produto comum
class productImport(productComum):
    def __init__(self, name: str, price: float, customsFee: float):
        # Herdando os atributos da classe mãe e adicionando o atributo customsFee
        super().__init__(name, price)
        self.customsFee = customsFee

    # Função herdada, mas com adição da taxa alfandegária
    def bio(self, do: str):
        super().bio(do)
        if do == "print":
            print(f"(Taxa alfandegária: R${round(self.customsFee, 2)})", end=" ")
        elif do == "input":
            self.customsFee = float(input("Taxa alfandegária: "))

# Lista para armazenar os produtos, de modo que possa ser de qualquer tipo, estar sempre aumentando e permanecendo na ordem
products = []

# Recebendo os dados dos produtos
for i in range(int(input("Insira o número de produtos: "))):
    print(f"Produto #{i+1} dados:")
    productType = input(str("Comum, usado ou importado (c/u/i)? ").lower())
    if productType == "c":
        products.append(productComum("", 0)) # Adiciona um produto comum à lista
        products[i].bio("input") # Recebe os dados do produto comum
    elif productType == "u":
        products.append(productUsed("", 0, "")) # Adiciona um produto usado à lista
        products[i].bio("input") # Recebe os dados do produto usado
    elif productType == "i":
        products.append(productImport("", 0, 0)) # Adiciona um produto importado à lista
        products[i].bio("input") # Recebe os dados do produto importado
    else:
        print("Tipo de produto inválido. Tente novamente.") # Caso o tipo de produto seja inválido
        continue

print("\nFICHA DOS PRODUTOS:")

# Mostrando os dados dos produtos
for i in range(len(products)):
    products[i].bio("print")
    print()

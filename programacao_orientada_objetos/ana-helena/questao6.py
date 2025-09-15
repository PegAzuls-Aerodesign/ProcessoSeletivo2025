# --- Classe Mãe, base para a adição de todos os tipos de produto ---
class product:

    # Função que recebe as variáveis nome e preço 
    def __init__(self, name: str, price: float):                         
        self.name = name
        self.price = price

    # Função que mostra as informações do produto comum (Etiquetamento do produto) 
    def priceTag(self) -> str:                                            
        return f"{self.name} $ {self.price:.2f}"

# --- Classe filha, productImport herda product --- 
class productImport(product):

     # Função importada da classe mãe 
    def __init__(self, name: str, price: float, costomsFee: float):      
        super().__init__(name, price)                                     
        self.costomsFee = costomsFee

    # Função como valor total do produto (preço inicial + taxa) 
    def totalPrice(self) -> float:                                        
        return self.price + self.costomsFee

    # Função que mostra as informações do produto importado (Etiquetamento do produto) 
    def priceTag (self) -> str:                                           
        return f"{self.name} $ {self.totalPrice():.2f} (Manufacturing date: $ {self.costomsFee:.2f})"

# --- Classe filha, productUsed herda product ---
class productUsed(product):

    # Função importada da classe mãe 
    def __init__(self, name: str, price: float, manufacturingDate: str):  
        super().__init__(name, price)
        self.manufacturingDate = manufacturingDate

    # Função que mostra as informações do usado (Etiquetamento do produto) 
    def priceTag(self) -> str:                                           
        return f"{self.name} (used) $ {self.price:.2f} (Manufacturing date: {self.manufacturingDate})"


# -- Programa principal --

# Listagem de produtos 
products = []

# Recebimento da variável num (representa o número de produtos escolhidos)
num = int(input("Enter the numbers of products: "))

# Loop para recebimento dos dados do produto
for i in range(1, num + 1):
    print(f"Product #{i} data:")
    type = input("Commos, used or import (c/u/i)? ").lower()

    name = input("Name: ")
    price = float(input("Price: "))

    if type == "i": # Produto importado
        costomsFee = float(input("Costoms Fee: "))
        products.append(productImport(name, price, costomsFee))

    elif type == "u": # Protudo usado
        data = input("Manufacturing date: ")
        products.append(productUsed(name, price, data))

    else: #Produto comum
        products.append(product(name, price))

# -- Chamamento da função responsável pelo etiquetamento --
print("\nPRICE TAGS:")
for a in products:
    print(a.priceTag())

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_label(self):
        return f"Nome: {self.name}, Preço: R$ {self.price:.2f}"

class ImportedProduct(Product):
    def __init__(self, name, price, tax_rate):
        super().__init__(name, price)
        self.tax_rate = tax_rate
    
    def get_label(self):
        total = self.price * (1 + self.tax_rate / 100)
        return (f"Nome: {self.name}, Preço: R$ {self.price:.2f}, "
                f"Taxa de alfândega: {self.tax_rate}%, "
                f"Total: R$ {total:.2f}")

class UsedProduct(Product):
    def __init__(self, name, price, manufacture_date):
        super().__init__(name, price)
        self.manufacture_date = manufacture_date
    
    def get_label(self):
        return (f"Nome: {self.name}, Preço: R$ {self.price:.2f}, "
                f"Data de fabricação: {self.manufacture_date}")

def main():
    n = int(input("Digite o número de produtos: "))
    products = []
    
    for _ in range(n):
        product_type = input("Tipo do produto (Comum, Importado, Usado): ").strip()
        
        name = input("Nome: ")
        price = float(input("Preço: "))
        
        if product_type == "Comum":
            products.append(Product(name, price))
        elif product_type == "Importado":
            tax_rate = float(input("Taxa de alfândega (%): "))
            products.append(ImportedProduct(name, price, tax_rate))
        elif product_type == "Usado":
            manufacture_date = input("Data de fabricação (DD/MM/YYYY): ")
            products.append(UsedProduct(name, price, manufacture_date))
    
    print("\nEtiquetas de preço:")
    for product in products:
        print(product.get_label())

if __name__ == "__main__":
    main()
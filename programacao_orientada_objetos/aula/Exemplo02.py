class Veiculo:
    """
    Representa um veículo no sistema da locadora AutoFácil.
    A classe ABSTRAI a complexidade de um carro real, focando
    apenas no que é essencial para o processo de locação.
    """

    # --- Atributos Essenciais para a Locação ---
    def __init__(self, modelo, placa, cor, valor_diaria):
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.valor_diaria = valor_diaria
        self.disponivel = True  # Um carro novo no sistema sempre está disponível

    # --- Métodos Essenciais para a Locação ---
    def reservar(self, cliente): 
        """Altera o estado do veículo para 'não disponível'."""
        if self.disponivel:
            self.disponivel = False
            print(f"Veículo {self.modelo} (placa {self.placa}) reservado com sucesso para {cliente}.")
        else:
            print(f"Desculpe, o veículo {self.modelo} já está reservado.")

    def devolver(self):
        """Altera o estado do veículo para 'disponível'."""
        if not self.disponivel:
            self.disponivel = True
            print(f"Veículo {self.modelo} (placa {self.placa}) foi devolvido e está disponível novamente.")
        else:
            print(f"Atenção: Este veículo já constava como disponível.")

    def __str__(self):
        """Retorna uma descrição simples e útil do veículo para o sistema."""
        status = "Disponível" if self.disponivel else "Reservado"
        return f"Modelo: {self.modelo} | Cor: {self.cor} | Diária: R${self.valor_diaria:.2f} | Status: {status}"

# --- Demonstração ---
carro1 = Veiculo("Fiat Mobi", "ABC-1234", "Branco", 95.50)
carro2 = Veiculo("Jeep Renegade", "XYZ-5678", "Cinza", 180.00)

print("--- Frota da AutoFácil ---")
print(carro1)
print(carro2)
print("-" * 25)

carro1.reservar("João Silva")
print("\n--- Após a primeira reserva ---")
print(carro1)
print(carro2)
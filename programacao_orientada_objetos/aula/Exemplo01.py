class Aerodesign:
    asa: str = "Monoplano"
    fuselagem: str = "Caixão"
    MTOW: float = 9.18
    equipe: str = "Dragão Branco"
    voando: bool = False

    def decolar(self):
        """
        Muda o estado do avião para 'voando' se ele estiver em terra.
        """
        if not self.voando:
            self.voando = True
            print("Decolando...")
        else:
            print("O avião já está voando.")
    
    def pousar(self):
        """
        Muda o estado do avião para 'em terra' se ele estiver voando.
        """
        if self.voando:
            self.voando = False
            print("Pousando...")
        else:
            print("O avião já está em terra.")
    
    def ficha_tecnica(self):
        """
        Exibe as especificações técnicas do avião.
        """
        print(f"=== Ficha Técnica ===")
        print(f"Asa: {self.asa}")
        print(f"Fuselagem: {self.fuselagem}")
        print(f"MTOW: {self.MTOW} kg")
        print(f"Equipe: {self.equipe}")
        estado = "Voando" if self.voando else "Em terra"
        print(f"Estado atual: {estado}")
        print("====================\n")


if __name__ == "__main__":
    # Criando uma instância (objeto) da classe Aerodesign
    meu_aviao = Aerodesign()
    
    # Exibindo a ficha técnica do avião
    meu_aviao.ficha_tecnica()
    
    # Tentando decolar
    meu_aviao.decolar()
    
    # Exibindo a ficha técnica novamente para ver o estado atualizado
    meu_aviao.ficha_tecnica()
    
    # Tentando pousar
    meu_aviao.pousar()
    
    # Exibindo a ficha técnica novamente para ver o estado atualizado
    meu_aviao.ficha_tecnica()
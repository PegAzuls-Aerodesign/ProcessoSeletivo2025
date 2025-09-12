class ContaBancaria:
    """
    Representa uma conta bancária usando ENCAPSULAMENTO para proteger o saldo.
    """
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # A convenção do underline sinaliza que '_saldo' não deve ser acessado diretamente.
        # Ele está "encapsulado" ou "protegido".
        self._saldo = saldo_inicial if saldo_inicial > 0 else 0

    # --- Métodos Públicos (A Interface Segura) ---
    # Estes são os "portões" de acesso controlado ao estado do objeto.

    def depositar(self, valor):
        """Método seguro para adicionar dinheiro à conta."""
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        """Método seguro para retirar dinheiro, com validação."""
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def get_saldo(self):
        """Método seguro para consultar o saldo."""
        # Não damos acesso direto ao atributo, mas a uma cópia do seu valor.
        return self._saldo

# --- Demonstração ---
conta_ana = ContaBancaria("Ana", 1000)

print(f"Saldo inicial da Ana: R${conta_ana.get_saldo()}")

# Tentativa de corromper o saldo (o que um programador bem-intencionado evitaria)
# Embora Python permita, a convenção do '_' deixa claro que isso é errado.
# conta_ana._saldo = -5000  # <--- MÁ PRÁTICA! VIOLA O ENCAPSULAMENTO.

# A forma CORRETA de interagir com o objeto:
conta_ana.sacar(200)   # Operação válida e segura
conta_ana.sacar(900)   # Operação inválida, bloqueada pela regra de negócio
conta_ana.depositar(50)  # Operação válida e segura

print(f"Saldo final da Ana: R${conta_ana.get_saldo()}") # Saída: 850
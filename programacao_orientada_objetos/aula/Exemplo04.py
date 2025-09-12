# --- CLASSE MÃE (Superclasse) ---
# A base que será reutilizada por todos os tipos de conta.
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial if saldo_inicial > 0 else 0

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print("Saque realizado.")
        else:
            print("Saldo insuficiente.")

    def get_saldo(self):
        return self._saldo

# --- CLASSES FILHAS (Subclasses) ---
# Elas herdam tudo da ContaBancaria e adicionam suas especialidades.

# 1. Conta Poupança
class ContaPoupanca(ContaBancaria):  # A herança é declarada aqui!
    """
    Herda tudo de ContaBancaria e adiciona um comportamento novo.
    """
    def render_juros(self, taxa):
        juros = self._saldo * taxa
        self._saldo += juros
        print(f"Juros de R${juros:.2f} aplicados. Novo saldo: R${self._saldo:.2f}")

# 2. Conta Corrente
class ContaCorrente(ContaBancaria):
    """
    Herda de ContaBancaria, adiciona um novo atributo e
    modifica (sobrescreve) um método existente.
    """
    def __init__(self, titular, saldo_inicial, limite_cheque):
        # Chama o construtor da classe mãe para não repetir a lógica
        super().__init__(titular, saldo_inicial) # Super() chama o construtor da superclasse
        self._limite_cheque = limite_cheque

    # Sobrescrevendo o método sacar
    def sacar(self, valor):
        """
        Altera o comportamento do saque para permitir o uso do cheque especial.
        """
        saldo_disponivel = self._saldo + self._limite_cheque
        if 0 < valor <= saldo_disponivel:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
            if self._saldo < 0:
                print(f"Atenção: Você está usando R${abs(self._saldo):.2f} do seu cheque especial.")
        else:
            print("Limite de cheque especial excedido.")

# --- Demonstração ---
poupanca_ana = ContaPoupanca("Ana", 1000)
corrente_joao = ContaCorrente("João", 500, 1000) # Saldo 500, Limite 1000

print("--- Conta Poupança da Ana ---")
poupanca_ana.depositar(200)  # Método herdado
poupanca_ana.render_juros(0.005) # Método próprio
print(f"Saldo final: R${poupanca_ana.get_saldo():.2f}")

print("\n--- Conta Corrente do João ---")
corrente_joao.sacar(700) # Usa o método 'sacar' modificado
print(f"Saldo final: R${corrente_joao.get_saldo():.2f}")
# --- As Classes (Mãe e Filhas) ---
# Adicionamos um método 'processar_virada_de_mes' em cada uma.

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial
    
    def get_saldo(self):
        return self._saldo

    # Método genérico na classe mãe.
    def processar_virada_de_mes(self):
        # Contas comuns não têm processamento especial.
        pass

class ContaPoupanca(ContaBancaria):
    # Sobrescrevendo o método para dar um comportamento específico.
    def processar_virada_de_mes(self):
        juros = self._saldo * 0.005 # Taxa de 0.5%
        self._saldo += juros
        print(f"[POUPANÇA] Juros de R${juros:.2f} aplicados para {self.titular}.")

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo_inicial, limite_cheque):
        super().__init__(titular, saldo_inicial)
        self._limite_cheque = limite_cheque
        
    # Sobrescrevendo o método com outro comportamento.
    def processar_virada_de_mes(self):
        taxa = 15.00
        self._saldo -= taxa
        print(f"[CORRENTE] Taxa de manutenção de R${taxa:.2f} cobrada de {self.titular}.")

# --- A FUNÇÃO POLIMÓRFICA ---
# Esta função não precisa saber o tipo dos objetos na lista.
# Ela apenas confia que cada objeto 'conta' sabe como responder
# à mensagem 'processar_virada_de_mes()'.

def roda_virada_de_mes(lista_de_contas):
    print("\n--- PROCESSANDO VIRADA DE MÊS PARA TODAS AS CONTAS ---")
    for conta in lista_de_contas:
        # O POLIMORFISMO ACONTECE EXATAMENTE AQUI!
        # Python automaticamente chama o método correto para cada tipo de conta.
        conta.processar_virada_de_mes()
    print("--- PROCESSAMENTO FINALIZADO ---\n")

# --- Demonstração ---

# 1. Criamos uma lista com OBJETOS DE TIPOS DIFERENTES.
contas_do_banco = [
    ContaPoupanca("Ana", 2000),
    ContaCorrente("João", 1500, 500),
    ContaPoupanca("Maria", 5000),
    ContaBancaria("José", 100) # Uma conta comum, sem processamento.
]

print("--- SALDOS ANTES DA VIRADA DE MÊS ---")
for conta in contas_do_banco:
    print(f"Saldo de {conta.titular}: R${conta.get_saldo():.2f}")

# 2. Chamamos a ÚNICA função genérica.
roda_virada_de_mes(contas_do_banco)

print("--- SALDOS DEPOIS DA VIRADA DE MÊS ---")
for conta in contas_do_banco:
    print(f"Saldo de {conta.titular}: R${conta.get_saldo():.2f}")
# -------------------------------------------------------------------
# SOLUÇÃO COM PROGRAMAÇÃO ORIENTADA A OBJETOS
# -------------------------------------------------------------------

class ContaBancaria:
    # O método __init__ é o construtor. Ele cria o objeto.
    # Os dados (atributos) agora pertencem ao objeto (self).
    def __init__(self, titular, numero, saldo_inicial=0):
        self.titular = titular
        self.numero = numero
        # Solução 1: Encapsulamento. O saldo é "protegido" dentro do objeto.
        # O underscore (_) é uma convenção em Python para indicar que o atributo é de uso interno.
        self._saldo = saldo_inicial
        print(f"Conta para {self.titular} criada com sucesso.")

    # Os comportamentos (métodos) operam nos dados do próprio objeto (self).
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    # Solução 3: Reuso de lógica de negócio.
    # Transferir agora usa os outros métodos do próprio objeto, evitando duplicação.
    def transferir(self, conta_destino, valor):
        if valor > 0 and self._saldo >= valor:
            # Reutiliza a lógica de saque do próprio objeto.
            self.sacar(valor) 
            # Reutiliza a lógica de depósito do objeto de destino.
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para {conta_destino.titular} realizada.")
        else:
            print("Transferência falhou: saldo insuficiente ou valor inválido.")

    # Método para acesso controlado ao saldo.
    def mostrar_saldo(self):
        print(f"O saldo da conta de {self.titular} é R${self._saldo:.2f}")


# --- "Programa Principal" (Execução) ---
print("--- Criando Objetos ---")
# Agora, em vez de variáveis globais, criamos instâncias da nossa classe.
conta_joao = ContaBancaria("João Silva", "123-4", 1000.00)
conta_maria = ContaBancaria("Maria Souza", "567-8", 2500.00)

print("\n--- Realizando Operações (Chamando Métodos) ---")
# As operações são mensagens enviadas aos objetos.
conta_joao.depositar(500.00)
conta_maria.sacar(1000.00)
conta_joao.transferir(conta_maria, 200)

print("\n--- Saldos Finais ---")
conta_joao.mostrar_saldo()
conta_maria.mostrar_saldo()

print("\n" + "="*40)
print("!!! A SEGURANÇA DA POO !!!")
print("="*40)
print("Tentando corromper os dados diretamente...")
# Embora Python permita o acesso, a convenção do "_" deixa claro que isso é errado.
# O programador sabe que não deve fazer isso. Em outras linguagens (Java/C#),
# seria possível tornar o atributo `saldo` verdadeiramente privado e inacessível.
conta_joao._saldo = -99999.99
print(f"Saldo corrompido (violando as regras): R${conta_joao._saldo:.2f}")
# No entanto, a lógica de negócio permanece protegida pelos métodos.
conta_joao.sacar(50) # A regra de negócio dentro do método ainda funciona!
print("="*40)
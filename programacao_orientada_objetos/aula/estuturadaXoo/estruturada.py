# -------------------------------------------------------------------
# EXEMPLO EM PROGRAMAÇÃO ESTRUTURADA
# -------------------------------------------------------------------

# Problema 1: Dados globais e expostos.
# Qualquer parte do código pode acessar e modificar estas variáveis diretamente.
# Não há nenhuma proteção ou regra de negócio associada diretamente aos dados.
conta1 = {
    "titular": "João Silva",
    "numero": "123-4",
    "saldo": 1000.00
}

conta2 = {
    "titular": "Maria Souza",
    "numero": "567-8",
    "saldo": 2500.00
}

# --- Funções que operam em dados externos ---

# Problema 2: Funções genéricas e "sem dono".
# A quem pertence a função "depositar"? Ela não sabe o que é uma "conta",
# apenas espera receber um dicionário com uma chave "saldo".
def depositar(conta, valor):
    """Adiciona um valor ao saldo da conta."""
    if valor > 0:
        conta["saldo"] += valor
        print(f"Depósito de R${valor:.2f} realizado na conta de {conta['titular']}.")
    else:
        print("Valor de depósito inválido.")

def sacar(conta, valor):
    """Retira um valor do saldo da conta, se houver fundos."""
    if valor > 0 and conta["saldo"] >= valor:
        conta["saldo"] -= valor
        print(f"Saque de R${valor:.2f} realizado na conta de {conta['titular']}.")
    else:
        print(f"Saldo insuficiente ou valor de saque inválido na conta de {conta['titular']}.")

def transferir(conta_origem, conta_destino, valor):
    """Transfere valor de uma conta para outra."""
    # Problema 3: Lógica de negócio complexa e espalhada.
    # A lógica de saque está implícita aqui, mas não é uma chamada explícita à função sacar.
    # O que acontece se a regra de saque mudar? Teremos que lembrar de mudar aqui também.
    if valor > 0 and conta_origem["saldo"] >= valor:
        conta_origem["saldo"] -= valor
        conta_destino["saldo"] += valor
        print(f"Transferência de R${valor:.2f} de {conta_origem['titular']} para {conta_destino['titular']} realizada.")
    else:
        print("Transferência falhou: saldo insuficiente ou valor inválido.")

def mostrar_saldo(conta):
    """Exibe o saldo da conta."""
    print(f"O saldo da conta de {conta['titular']} é R${conta['saldo']:.2f}")


# --- "Programa Principal" (Execução) ---
print("--- Início das Operações ---")
mostrar_saldo(conta1)
mostrar_saldo(conta2)

print("\n--- Realizando Operações Válidas ---")
depositar(conta1, 500.00)
sacar(conta2, 1000.00)
transferir(conta2, conta1, 300.00)

print("\n--- Saldos Após Operações ---")
mostrar_saldo(conta1)
mostrar_saldo(conta2)


# --- O GRANDE PROBLEMA: ACESSO DIRETO E CORRUPÇÃO DE DADOS ---
print("\n" + "="*40)
print("!!! O PERIGO DA PROGRAMAÇÃO ESTRUTURADA !!!")
print("="*40)
print(f"Saldo antigo da conta de João: R${conta1['saldo']:.2f}")

# Qualquer parte do sistema pode fazer isso, ignorando todas as regras de negócio!
# Não há encapsulamento. O estado da conta é totalmente vulnerável.
conta1["saldo"] = -99999.99  # Um hacker? Um bug? Um desenvolvedor desatento?

print(f"Saldo NOVO e INVÁLIDO da conta de João: R${conta1['saldo']:.2f}")
print("O estado do sistema foi corrompido facilmente!")
print("="*40)
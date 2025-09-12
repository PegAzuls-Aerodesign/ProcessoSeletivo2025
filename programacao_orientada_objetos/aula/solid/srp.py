# --- MODO ERRADO (Múltiplas Responsabilidades) ---
class OrdemDeServico_ERRADO:
    def __init__(self, id, cliente, total):
        self.id = id
        self.cliente = cliente
        self.total = total

    def salvar_no_banco(self):
        print(f"Salvando Ordem {self.id} no banco de dados...")

    def enviar_email_confirmacao(self):
        print(f"Enviando e-mail para {self.cliente}...")

# --- MODO CORRETO (Responsabilidades Separadas) ---
class OrdemDeServico:
    """Responsabilidade: Apenas gerenciar os dados da ordem."""
    def __init__(self, id, cliente, total):
        self.id = id
        self.cliente = cliente
        self.total = total

class RepositorioDeOrdens:
    """Responsabilidade: Apenas persistir os dados."""
    def salvar(self, ordem):
        print(f"Salvando Ordem {ordem.id} no banco de dados...")

class ServicoDeNotificacao:
    """Responsabilidade: Apenas notificar o cliente."""
    def enviar_email_confirmacao(self, ordem):
        print(f"Enviando e-mail para {ordem.cliente}...")

# Agora, se a lógica de notificação mudar, alteramos apenas ServicoDeNotificacao.
# Se o banco de dados mudar, alteramos apenas RepositorioDeOrdens.

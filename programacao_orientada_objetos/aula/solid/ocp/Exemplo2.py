# --- MODO ERRADO ---
class Notificador_ERRADO:
    def enviar(self, mensagem, canal):
        if canal == "email":
            print(f"Enviando via Email: {mensagem}")
        # MODIFICAR aqui para "sms".

# --- MODO CORRETO ---

# 1. A abstração
class CanalDeNotificacao:
    def enviar(self, mensagem):
        pass

# 2. As extensões
class CanalEmail(CanalDeNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando via Email: {mensagem}")

class CanalSMS(CanalDeNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando via SMS: {mensagem}")
        
class CanalPush(CanalDeNotificacao): # <-- Nova extensão
    def enviar(self, mensagem):
        print(f"Enviando via Push Notification: {mensagem}")

# 3. O código cliente
class Notificador:
    def __init__(self, canais: list[CanalDeNotificacao]):
        self.canais = canais

    def notificar_todos(self, mensagem):
        for canal in self.canais:
            canal.enviar(mensagem)

# Uso:
canais_do_usuario = [CanalEmail(), CanalPush()]
notificador_app = Notificador(canais_do_usuario)
notificador_app.notificar_todos("Sua fatura fechou!")

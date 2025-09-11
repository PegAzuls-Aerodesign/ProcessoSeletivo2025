
# --- MODO ERRADO (Modificando a função existente) ---
def gerar_relatorio_ERRADO(pagamentos, formato):
    if formato == "pdf":
        print("Exportando pagamentos para PDF...")
    elif formato == "csv": # <-- Tivemos que MODIFICAR a função
        print("Exportando pagamentos para CSV...")

# --- MODO CORRETO (Estendendo com novas classes) ---
# 1. Criamos uma abstração (interface)
class Exportador:
    def exportar(self, pagamentos):
        pass

# 2. Criamos implementações concretas (EXTENSÕES)
class ExportadorPDF(Exportador):
    def exportar(self, pagamentos):
        print("Exportando pagamentos para PDF...")

class ExportadorCSV(Exportador):
    def exportar(self, pagamentos):
        print("Exportando pagamentos para CSV...")

class ExportadorJSON(Exportador): # <-- Nova extensão, sem tocar no código antigo!
    def exportar(self, pagamentos):
        print("Exportando pagamentos para JSON...")

# 3. A função principal agora está FECHADA para modificação.
def gerar_relatorio(pagamentos, exportador: Exportador):
    # Ela não se importa com o formato, apenas chama o método 'exportar'.
    exportador.exportar(pagamentos)

# Uso:
pagamentos_de_hoje = [100, 250, 80]
gerar_relatorio(pagamentos_de_hoje, ExportadorPDF())
gerar_relatorio(pagamentos_de_hoje, ExportadorCSV())
gerar_relatorio(pagamentos_de_hoje, ExportadorJSON())

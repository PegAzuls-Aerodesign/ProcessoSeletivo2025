class Professor:
    """Representa o objeto independente 'Professor'."""
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def lecionar(self):
        print(f"O Professor {self.nome} está lecionando a disciplina {self.disciplina}.")

class Departamento:
    """Representa o objeto 'agregador'."""
    def __init__(self, nome):
        self.nome = nome
        self.professores = [] # O departamento tem uma lista de professores

    def adicionar_professor(self, professor):
        """
        A Agregação acontece aqui!
        O departamento NÃO CRIA o professor, apenas o recebe e o armazena.
        """
        self.professores.append(professor)

# 1. Os objetos 'Professor' são criados de forma independente.
prof_alan = Professor("Alan Turing", "Introdução à Computação")
prof_ada = Professor("Ada Lovelace", "Programação de Computadores")

# 2. O objeto 'Departamento' é criado.
depto_computacao = Departamento("Departamento de Computação")

# 3. O departamento AGREGA os professores.
depto_computacao.adicionar_professor(prof_alan)
depto_computacao.adicionar_professor(prof_ada)

# Se o 'depto_computacao' for deletado, 'prof_alan' e 'prof_ada' continuam existindo.
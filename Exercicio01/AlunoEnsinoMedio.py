from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo=None, nome=None, matricula=None, ano=None):
        super().__init__(codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        super().imprimir()
        print("Ano: ", self.ano)
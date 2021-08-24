from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, codigo=None, nome=None, matricula=None, semestre=None):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre
    
    def imprimir(self):
        super().imprimir()
        print("Semestre: ", self.semestre)
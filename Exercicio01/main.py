from AlunoGraduacao import AlunoGraduacao
from AlunoEnsinoMedio import AlunoEnsinoMedio
from Aluno import Aluno

print("----Aluno----")
aluno = Aluno(100, "Fernanda", "1234")
aluno.imprimir()

print("----Aluno Ensino Médio----")
alunoEnsinoMedio = AlunoEnsinoMedio(101, "Pedrinho", "2345", 2021)
alunoEnsinoMedio.imprimir()

print("----Aluno Graduação----")
alunoGraduacao = AlunoGraduacao(102, "Laura", "5643", 6)
alunoGraduacao.imprimir()
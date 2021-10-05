from Computador import Computador

class Notebook(Computador):

    __tempoDeBateria = None

    def __init__(self, modelo, cor, preco, tempoDeBateria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.tempoDeBateria = tempoDeBateria
    
    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria
    
    @tempoDeBateria.setter
    def tempoDeBateria(self, valor):
        if valor <= 0: print('Tempo de Bateria: Valor inválido, só são aceitos valores positivos.')
        else: self.__tempoDeBateria = valor
    
    def getInformacoes(self):
        super().getInformacoes()
        print('Tempo de Bateria: ', self.__tempoDeBateria)
    
    def cadastrar(self):
        print('Notebook Cadastrado: ')
        self.getInformacoes()
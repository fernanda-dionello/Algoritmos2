from abc import ABCMeta, abstractmethod, abstractproperty

class Computador(metaclass=ABCMeta):

    modelo = None
    cor = None
    __preco = None

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0: print('Preço: Valor inválido, só são aceitos valores positivos.')
        else: self.__preco = valor

    def getInformacoes(self):
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Preco: ", self.__preco)
    
    @abstractmethod
    def cadastrar(self):
        pass

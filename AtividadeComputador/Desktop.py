from Computador import Computador

class Desktop(Computador):
    _potenciaDaFonte = None
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.potenciaDaFonte = potenciaDaFonte
    
    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte
    
    @potenciaDaFonte.setter
    def potenciaDaFonte(self, valor):
        if valor <= 0: print('Potencia da Fonte: Valor inválido, só são aceitos valores positivos.')
        else: self._potenciaDaFonte = valor
    
    def getInformacoes(self):
        super().getInformacoes()
        print('Potencia da Fonte: ', self._potenciaDaFonte)
    
    def cadastrar(self):
        print('Desktop Cadastrado: ')
        self.getInformacoes()


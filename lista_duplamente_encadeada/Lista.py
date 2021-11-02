from Nodo import Nodo

class Lista:

	def __init__(self):
	    self.inicio = None
	    self.tamanho = 0

	def adicionar(self, valor):
		nodo = Nodo(valor)
		if self.inicio:
			aux = self.inicio
			while( aux.proximo ):
				aux = aux.proximo
			aux.proximo = nodo
			nodo.anterior = aux
		else:
			self.inicio = nodo
		self.tamanho += 1
		self.imprimir()

	def imprimir(self):
		if  self.inicio == None:
			print( "A lista está vazia!")
		else:
			aux = self.inicio
			while( aux ):
				print( aux.dado )
				aux = aux.proximo
			print("Tamanho da Lista: ", self.tamanho )
			print("--------------------")
	
	def imprimir_inversamente(self):
		if  self.inicio == None:
			print( "A lista está vazia!")
		else:
			aux = self.inicio
			if self.tamanho == 1:
				print(aux.dado)
			else:
				while( aux.proximo != None ):
					aux = aux.proximo
				while(aux != None):
					print(aux.dado)
					aux = aux.anterior
			print("Tamanho da Lista: ", self.tamanho )
			print("--------------------")

	def excluir( self, valor ):
		if self.tamanho == 0:
			print("A lista está vazia!")
		elif self.tamanho == 1:
			if self.inicio.dado == valor:
				self.inicio = None
				self.tamanho = 0 
			else:
				print("Valor não encontrado")
		else:
			tamanhoAnterior = self.tamanho
			if self.inicio.dado == valor:
				self.inicio = self.inicio.proximo
				self.inicio.anterior = None
				self.tamanho -= 1
			else:
				anterior = self.inicio
				aux = self.inicio.proximo
				while( aux ):
					if aux.dado == valor:
						anterior.proximo = aux.proximo
						prox = anterior.proximo
						prox.anterior = anterior
						self.tamanho -= 1
					else: 
						anterior = aux
					aux = aux.proximo
			if tamanhoAnterior == self.tamanho:
				print("Valor não encontrado!")

		self.imprimir()
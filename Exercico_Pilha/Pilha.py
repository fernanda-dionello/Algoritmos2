from No import No

class Pilha:

	def __init__(self):
	    self.topo = None
	    self.tamanho = 0

	def adicionar(self, valor):
		no = No( valor )
		if self.tamanho == 0:
			self.topo = no
		else:
			aux = self.topo
			self.topo = no
			self.topo.proximo = aux
		self.tamanho += 1
		self.imprimir()


	def imprimir(self):
		texto = ""
		if self.topo == None :
			texto = "Pilha Vazia!"
		else:
			aux = self.topo
			while ( aux ) :
				texto = texto + str( aux.dado ) + "  -  "
				aux = aux.proximo
		print( texto )
		print(" ---------------------------------------------------")


	def remover(self):
		if self.tamanho == 0:
			print( "Pilha Vazia!")
		elif self.tamanho == 1:
			self.topo = None
			self.tamanho = 0
		else:
			self.topo = self.topo.proximo
			self.tamanho -= 1
		self.imprimir()

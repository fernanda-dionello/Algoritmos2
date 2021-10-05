from Notebook import Notebook
from Desktop import Desktop

print('--------DESKTOP-----------------')
d1 = Desktop('hp', 'preto', 5000, 110)
d1.getInformacoes()
print('------------')
d1.cadastrar()

print('--------NOTEBOOK-----------------')
n1 = Notebook('lenovo', 'branco', 7000, 80)
n1.getInformacoes()
print('------------')
n1.cadastrar()
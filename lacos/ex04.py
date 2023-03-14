import random

#__init__ é um dos métodos reservados em Python. 
# O método __init__ pode ser chamado quando um objeto é criado a 
# partir da classe e o acesso é necessário para inicializar os 
# atributos da classe.

#def é usada para criar (ou definir) uma função.

class CaraCoroa:
    def __init__(self):
        self.lado = 'Cara'

    def lancar(self):
        if (random.randint(0, 1)) % 2 == 0:
            self.lado = 'Cara'
        else:
            self.lado = 'Coroa'
        return self.lado

moeda = CaraCoroa()
op = 1

while op:
    op = int(input("0.Sair\n"
                   "1.Jogar de novo\n"))

    if op:
        print(moeda.lancar())

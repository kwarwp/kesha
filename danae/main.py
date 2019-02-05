# kesha.danae.main.py
#from _spy.meredith import Componente

class Componente:
    def __init__(self, nome):
        self.nome = nome

class Aresta(Componente):
    def __init__(self, nome, noh1, noh2):
        super().__init__(nome)
        self.nome = nome
        
class Noh(Componente):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome

if __name__ == "__main__":
    n = Noh("nn")
    print(n.nome)
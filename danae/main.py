# kesha.danae.main.py
from meredith import Componente

class Aresta(Componente):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        
class Noh(Componente):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome

if __name__ == "__main__":
    n = Noh("nn")
    print(n.nome)
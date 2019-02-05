# kesha.danae.main.py
from meredith import Componente

class Aresta(Componente):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        
class noh(Componente):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
   
if __name__ == "__main__":
    n = noh("nn")
    print(n.nome)
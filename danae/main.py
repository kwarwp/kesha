# kesha.danae.main.py
#from _spy.meredith import Componente

class Componente:
    def __init__(self, nome):
        self.nome = nome

class Aresta(Componente):
    def __init__(self, nome, noh1, noh2):
        super().__init__(nome)
        self.nome = nome
        self.noh1, self.noh2 = noh1, noh2
        noh1.adicionar(self)
        noh2.adicionar(self)
        
class Noh(Componente):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        self.aresta = []
    def adicionar(self,aresta):
        self.aresta.append(aresta)

if __name__ == "__main__":
    n = Noh("nn")
    n2 = Noh("Mari")
    a = Aresta("Desg", n, n2)
    print(a.nome, a.noh1.nome, a.noh2.nome)
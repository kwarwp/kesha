# kesha.morgan.main.py
# sarah.roxanne.main.py
__autor__ = "Isabel Hortencia Garnica"
__version__ = "05.12.2019"
from _spy.vitollino.main import Cena, Texto, Elemento, INVENTARIO, STYLE, Musica

STYLE ["width"] = 1320
STYLE ["height"] = "600px"
IGR = "https://i.imgur.com/"
CEST, DOG, BASE, CENA, PRED = f"{IGR}qtw6IoO.png", f"{IGR}ZQ9SSMz.png", f"{IGR}7Wh2Px0.png", f"{IGR}zRGdYRp.gif", f"{IGR}vL9kR9Y.png"

class Predio(Elemento): #predio que  inicia bom e no fim fica queimado
     def __init__(self, imagem, cena):
        super().__init__(imagem, x= 350, y=180, w=650, h=300)
        self.nome = "casa"


class Plataforma(Elemento): #retangulo azul
    def __init__(self, imagem, cena, x=400, y=0):
        super().__init__(imagem, cena=cena, w=200, x=x, y=y)
        self.destino = self
        self.nome = "base"
        
    def movimenta(self, destino):
        destino.move(self.destino)


class Personagem(Elemento): #dog
    def __init__(self, imagem, destino, cena, x=600, y=0):
        super().__init__(imagem, cena=cena, x=x, y=y, w=100, h=70)
        self.destino = destino
        self.vai = self.move
        
    def move(self, evento=None):
        self.entra(self.destino)


class Veiculo(Elemento):
    def __init__(self, imagem, destino, cena, x=100, y=0):
        super().__init__(imagem, cena=cena, x=x, y=y)
        self.nome = "veiculo"
        self.destino = destino
        self.vai = self._move
        
    def _move(self, evento=None):
        self.destino.movimenta(self)
        
    def move(self, destino):
        self.entra(destino)
        self.destino = destino
        
    def movimenta(self, destino):
        destino.move(self)


class Basico:
    def __init__(self):
        self.cena = cena = Cena(CENA)
        self.casa = Predio(PRED, cena=cena)
        self.casa.entra(self.cena)
        self.base0 = Plataforma(BASE, y=100, cena=cena)
        self.base1 = Plataforma(BASE, y=500, cena=cena)
        self.base0.destino, self.base1.destino = self.base1, self.base0 
        self.cesta = Veiculo(CEST, destino=self.base1, cena=cena)
        self.cesta.entra(self.base0)
        self.doggie = Personagem(DOG, destino=self.cesta, cena=cena)
        cena.vai()
        
        
if __name__ == "__main__":
    Basico()
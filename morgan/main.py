# kesha.morgan.main.py
# sarah.roxanne.main.py
__autor__ = "Isabel Hortencia Garnica"
__version__ = "05.12.2019"
from _spy.vitollino.main import Cena, Texto, Elemento, INVENTARIO, STYLE, Musica

STYLE ["width"] = 1320
STYLE ["height"] = "600px"
IGR = "https://i.imgur.com/"
CEST, DOG, BASE, CENA, PRED = f"{IGR}qtw6IoO.png", f"{IGR}ZQ9SSMz.png", f"{IGR}7Wh2Px0.png", f"{IGR}zRGdYRp.gif", f"{IGR}vL9kR9Y.png"
#CEST, DOG, RET, CENAINICIO  = f"{IGR}qtw6IoO.png", f"{IGR}ZQ9SSMz.png", f"{IGR}HUkZFHm.png", f"{IGR}zRGdYRp.gif"
#FUNDODIA, BILHETE, BOTAO, LOGO, PLAY = f"{IGR}zRGdYRp.gif", f"{IGR}p9SteRs.png", f"{IGR}kTocYiF.png", f"{IGR}JflnamW.png",f"{IGR}Jcnz4vj.png"
#TRACK = "https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3"
#SOMA, SOMB, PRED = f"{IGR}Rpo5MDy.png", f"{IGR}Hysq98H.png",  
#CART, CAT, BASE, CENA = f"{IGR}m2k5sv6.png", f"{IGR}ek8oINR.png", f"{IGR}DAUyvBP.jpg", f"{IGR}nkwZCrR.jpg"

#predio que  inicia bom e no fim fica queimado
class Predio(Elemento): 
     def __init__(self, imagem, cena, x=600, y=180):
        super().__init__(imagem, cena=cena,w=650, h=300)
        self.nome = "casa"

#retangulo azul
class Plataforma(Elemento): 
    def __init__(self, imagem, cena, x=400, y=100):
        super().__init__(imagem, cena=cena, w=200, x=x, y=y)
        self.destino = self
        self.nome = "base"
        
    def movimenta(self, destino):
        destino.move(self.destino)

#dog, menino e menina (futuramente)
class Personagem(Elemento): 
    def __init__(self, imagem, destino, cena, x=600, y=0):
        super().__init__(imagem, cena=cena, x=x, y=y, w=100, h=70)
        self.destino = destino
        self.vai = self.move
        
    def move(self, evento=None):
        self.entra(self.destino)

#Cestas que os personagens entrarão
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
"""
class gameInicio:
    def __init__(self):
        gameInicio = Cena(CENAINICIO)
        gameInicio.vai()
        dark= Elemento("",style=dict(width="1345px",height="600px",backgroundColor="black",opacity=0.7),cena=gameInicio)
        self.logotipo = Elemento(LOGO, x=370, y=30,w=650,h=400, cena=gameInicio)
        self.play = Elemento(PLAY, x=570, y=470,w=180,h=120, cena=gameInicio, vai = self.mostradia)

    def mostradia(self,ev=0):
        fake = Cena()
        fake.vai = self.elevador
        dia = Cena(FUNDODIA, direita=fake )
        dia.vai()
        self.bil = Elemento(BILHETE, x=200, y=20,w=900,h=600, cena=dia, vai = self.elevador)
        self.boton = Elemento(BOTAO, x=820, y=470,w=70,h=70, cena=dia, vai = self.elevador)

    def toca(self, ev=0):
        self.musica.sound.play()
        self.musA.x= -1200
        self.musB.x= 1200

    def pause(self, ev=0):
        self.musica.sound.pause()
        self.musA.x= 1200
        self.musB.x= -1200
    
    def elevador(self, ev=0):
        todos = Cena(FUNDODIA)
        todos.vai()
        self.musica = Musica(TRACK)
        self.musica.sound.pause()
        self.musA = Elemento(SOMA, x=1200, y=500,w=80,h=80, cena=todos, vai=self.toca)
        self.musB = Elemento(SOMB, x=-1200, y=500,w=80,h=80, cena=todos, vai=self.pause)


class Plataforma(Elemento): #são as bases fantasmas
    def __init__(self, imagem, cena, x=400, y=0):
        super().__init__(imagem, cena=cena, w=100, x=x, y=y)
        self.destino = self
        self.nome = "base"
        
    def movimenta(self, destino):
        destino.move(self.destino)


class Personagem(Elemento): # dog
    def __init__(self, imagem, destino, cena, x=540, y=130):
        super().__init__(imagem, cena=cena, x=x, y=y, w=100, h=70)
        self.destino = destino
        self.vai = self.move
        
    def move(self, evento=None):
        self.entra(self.destino)


class Veiculo(Elemento): #é a cesta
    def __init__(self, imagem, destino, cena, x=180, y=120):
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
        self.cena = cena = Cena(FUNDODIA)
        self.base0 = Plataforma(RET, y= 100, cena=cena)
        self.base1 = Plataforma(RET, y= 500, cena=cena)
        self.base0.destino, self.base1.destino = self.base1, self.base0 
        self.cesta = Veiculo(CEST, destino=self.base1, cena=cena)
        self.cesta.entra(self.base0)
        self.doggie = Personagem(DOG, destino=self.cesta, cena=cena)
        cena.vai()


if __name__ == "__main__":
    Basico()




gameInicio()
"""


# kesha.morgan.main.py
# sarah.roxanne.main.py
__autor__ = "Isabel Hortencia Garnica"
__version__ = "05.12.2019"
from _spy.vitollino.main import Cena, Texto, Elemento, INVENTARIO, STYLE, Musica

STYLE ["width"] = 1320
STYLE ["height"] = "600px"
IGR = "https://i.imgur.com/"
CEST, DOG, BASE, CENA, CENAINICIO  = f"{IGR}qtw6IoO.png", f"{IGR}ZQ9SSMz.png", f"", f"{IGR}zRGdYRp.gif", f"{IGR}3qdowNm.jpg"
FUNDODIA, BILHETE, BOTAO, LOGO = f"{IGR}zRGdYRp.gif", f"{IGR}p9SteRs.png", f"{IGR}kTocYiF.png", f"{IGR}JflnamW.png"
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

gameInicio()
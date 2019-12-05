# kesha.morgan.main.py
# sarah.roxanne.main.py
__autor__ = "Isabel Hortencia Garnica"
__version__ = "05.12.2019"
from _spy.vitollino.main import Cena, Texto, Elemento, INVENTARIO, STYLE, Musica

STYLE ["width"] = 1320
STYLE ["height"] = "600px"
IGR = "https://i.imgur.com/"
CEST, DOG, BASE, CENA, CENAINICIO = f"{IGR}qtw6IoO.png", f"{IGR}ZQ9SSMz.png", f"", f"{IGR}zRGdYRp.gif", f"{IGR}3qdowNm.jpg"

class gameInicio:
    def __init__(self):
        
        gameInicio = Cena(CENAINICIO)
        gameInicio.vai()
        dark= Elemento("",style=dict(width="1345px",height="600px",backgroundColor="black",opacity=0.7),cena=gameInicio)
        self.logotipo = Elemento(LOGO, x=370, y=30,w=650,h=400, cena=gameInicio)
        self.play = Elemento(PLAY, x=570, y=470,w=180,h=120, cena=gameInicio, vai = self.mostradia)

gameInicio()
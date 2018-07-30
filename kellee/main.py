# kesha.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from browser import html, document, alert, doc
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
doc['py3d'].html=''
_gs=Glow('py3d')
scene=canvas()
#scene.background= color.white
#scene.width = 800
#scene.height = 600

STYLE["width"]=800
STYLE["height"]="600px"
FUNDO = "https://i.imgur.com/EzWk7Jl.jpg" 
#FUNDO_BRANCO = "https://i.imgur.com/UXD0mzp.png"
QAZUL = "https://i.imgur.com/lWDGIvc.jpg"
QVERMELHO = "https://i.imgur.com/K0YpYsi.png"
QVERDE = "https://i.imgur.com/hd3ofzP.png"

class Tabuleiro:
    def __init__(self):
        self.fase1 = Cena(img = FASE1)
        self.linhaA1 = Elemento(QBRANCO, style = dict(tit = "py3d",
            left= 160, 
            top= "127px", 
            width=101, 
            height="74px"))
        self.fase1.linhaA1(self.entra) 
        self.fase1.vai()
Tabuleiro()
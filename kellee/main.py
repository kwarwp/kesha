# kesha.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from browser import html, document, alert, doc
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
#scene.background= color.white
#scene.width = 800
#scene.height = 600

STYLE["width"]=800
STYLE["height"]="600px"
FUNDO = "https://i.imgur.com/EzWk7Jl.jpg" 
#FUNDO_BRANCO = "https://i.imgur.com/UXD0mzp.png"
QAZUL = "https://i.imgur.com/lWDGIvc.jpg"
#QVERMELHO = "https://i.imgur.com/K0YpYsi.png"
#QVERDE = "https://i.imgur.com/hd3ofzP.png"

class Tabuleiro:
    def _3d_(self):
        doc['py3d'].html=''
        _gs=Glow('py3d')
        scene=canvas()

        bloco = dict(color=color.blue)
        simetria1=box(pos=(4.2, -2, 0), size=(1,1,1) , **bloco)
        simetria2=box(pos=(1.8, 1.6, 0), size=(1,1,1) , **bloco)
        simetria = [box(pos=(3, x*(1.2)-2, 0), size=(1,1,1), **bloco) for x in range(4)]
        pts = [simetria1, simetria2]+simetria
        sup = compound(pts, pos=vec(2,0,0), axis=vec(4,0,-1))

    def __init__(self):
            self.fase1 = Cena(img = FUNDO)
            self.linhaA1 = Elemento(FUNDO, tit = "py3d", style = dict(
                left= 800, 
                top= "10px", 
                width=600, 
                height="600px"))
            self.linhaA1.entra(self.fase1) 
            self.fase1.vai()
            self._3d_()


Tabuleiro()
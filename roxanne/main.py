# kesha.roxanne.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"] = 1150
STYLE ["height"] = "600px"

NOITE = "https://i.imgur.com/Cfqvyhg.png"
FASE1 = "https://i.imgur.com/kZw8TRw.png"
FASE2 = "https://i.imgur.com/wmDD3Ix.png"
FASE3 = "https://i.imgur.com/83YrIHh.png"
FASE4 = "https://i.imgur.com/ibovjJ1.png"
FASE5 = "https://i.imgur.com/EBTCiQP.png"
FASE6 = "https://i.imgur.com/NyPMdqD.png"
FASE7 = "https://i.imgur.com/4dK7L1A.png"
FASE8 = "https://i.imgur.com/Aw6x1kC.png"
FASE9 = "https://i.imgur.com/uqRq6nc.png"
QBRANCO ="https://i.imgur.com/9PMJ1tD.png"
QAZUL = "https://i.imgur.com/HUkZFHm.png"
QVERDE = "https://i.imgur.com/hd3ofzP.png"
QVERMELHO = "https://i.imgur.com/K0YpYsi.png"
QSIMBOLO = "https://i.imgur.com/XnMRw3u.png"

class Tabuleiro:
    def __init__(self):
        self.noite = Cena(img = NOITE)
        #noite.vai()
        self.fase1 = Elemento(img = FASE1, tit = "SIMETRICO 3 X 4", style = dict(left=200, top="100px", width=540, height="320px"))
        self.fase1.entra(self.noite)
Tabuleiro ()



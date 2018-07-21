# kesha.roxanne.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"] = 1150
STYLE ["height"] = "600px"

NOITE = "https://i.imgur.com/Cfqvyhg.png"
FASE1 = "https://i.imgur.com/ayIr0WV.png"
FASE2 = "https://i.imgur.com/UvM5aa6.png"
FASE3 = "https://i.imgur.com/4nhx2A6.png"
FASE4 = "https://i.imgur.com/jUrqxIe.png"
FASE5 = "https://i.imgur.com/oVW6HwU.png"
FASE6 = "https://i.imgur.com/dkM5AIW.png"
FASE7 = "https://i.imgur.com/yjQaCPU.png"
FASE8 = "https://i.imgur.com/V10xkZP.png"
FASE9 = "https://i.imgur.com/tdOSHCw.png"

def tela1():
    noite = Cena(img = NOITE)
    noite.vai()
    fase1 = Elemento(img = FASE1, tit = "SIMETRICO 3 X 4", style = dict(left=500, top="100px", width=240, height="320px"))
    fase1.entra (noite)
      
tela1 ()



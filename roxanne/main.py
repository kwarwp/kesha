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

def tela1():
    noite = Cena(img = NOITE)
    noite.vai()
    fase1 = Elemento(img = FASE1, tit = "SIMETRICO 3 X 4", style = dict(left=200, top="100px", width=540, height="320px"))
    fase1.entra (noite)
      
tela1 ()



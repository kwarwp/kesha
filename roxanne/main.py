# kesha.roxanne.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900
#STYLE ["min-hight"] = 600

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
    fase1 = Elemento(img = FASE1, tit = "SIMETRICO 3 X 4", style = dict(left=120, top="100px", width=60, height="80px"))
    #eu = Elemento (img = EU, tit = "I", style = dict(left=40, top="450px", width=100, height="100px"))
    #mae_text= Texto(arvore, "Mother")
    #eu_text= Texto(arvore, "I")
    #mae.vai = mae_text.vai
    #eu.vai = eu_text.vai
    #eu.entra (arvore)
    #mae.entra(arvore)
    
tela1 ()



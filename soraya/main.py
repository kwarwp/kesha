# kesha.soraya.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
fundo = "https://i.imgur.com/F3E6Lv4.jpg"
quadrado = "https://i.imgur.com/C8Wwcse.png"
piramide = "https://i.imgur.com/Bvjihxr.gif"
prisma = "https://i.imgur.com/EYe69dg.png"
losango3d = "https://i.imgur.com/WTNCinT.png"
estrelabugadona = "https://i.imgur.com/Yq2K158.png"
circunferecia = "https://i.imgur.com/fI39ptw.png"
torre = "https://i.imgur.com/a7GrJH8.png"
STYLE ["width"] = 1150
STYLE ["height"] = "600px"

def geometria():
    fundogeo = Cena(img = fundo)
    
    square = Elemento(img = quadrado,
                      tit = "Adivinhe quem eu sou?",
                      style = dict (top = 300, left = 300, hight = 300, width = 300))
    square.entra (fundogeo)
    textosquare = Texto(fundogeo,"Pesquisa no google kakakajota")
    square.vai =textosquare.vai 
    
    fundogeo.vai()   
geometria()
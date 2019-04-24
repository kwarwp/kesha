# kesha.rachel.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
ciencia = "https://i.imgur.com/7xC9bET.jpg"
urso = "https://i.imgur.com/UvNnOfq.png"
indio ="https://i.imgur.com/acNsNoO.png"
indios ="https://i.imgur.com/RMc3y2v.png"

STYLE ["width"] = 1150
STYLE ["height"] = "600px"

def cicloagua():
    cenaAgua = Cena(img = ciencia)
    
    elementourso = Elemento(img = urso, 
                     tit = "Urso Marrom", 
                     style = dict (top = 250, left = 25, height = 100, width = 75))
    elementourso.entra(cenaAgua)
    textourso = Texto(cenaAgua,
                      "Urso marrom das montanhas do Alasca")
    elementourso.vai = textourso.vai
    
    cenaAgua.vai()
cicloagua()


# kesha.rachel.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from browser import html
ciencia = "https://i.imgur.com/7xC9bET.jpg"
urso = "https://i.imgur.com/UvNnOfq.png"
indio ="https://i.imgur.com/acNsNoO.png"
indios ="https://i.imgur.com/RMc3y2v.png"
interroga = "https://imgur.com/vHTik0T"
STYLE ["width"] = 1150
STYLE ["height"] = "600px"

def cicloagua():
    cenaAgua = Cena(img = ciencia)
#CHAMA O ELEMENTO URSO E O TEXTO 
    elementourso = Elemento(img = urso, 
                     tit = "Urso Marrom", 
                     style = dict (top = 420, left = 25, height = 60, width = 55, bottom = 100))
    
    elementourso.entra(cenaAgua)
    textourso = Texto(cenaAgua,
                      "Urso marrom das montanhas do Alasca")
    elementourso.vai = textourso.vai
    
#CHAMA O ELEMENTO INDIO E O TEXTO 
    elementoindio = Elemento(img = indio, 
                     tit = "Indio", 
                     style = dict (top = 400, left = 190, height = 80, width = 100))
    elementoindio.entra(cenaAgua)
    textoindio = Texto(cenaAgua,
                      "Indio Pele vermelha")
    elementoindio.vai = textoindio.vai
    
    #CHAMA O ELEMENTO INDIOS E O TEXTO 
    elementoindios = Elemento(img = indios, 
                     tit = "Indio", 
                     style = dict (top = 420, left = 300, height = 60, width = 80))
    elementoindios.entra(cenaAgua)
    textoindios = Texto(cenaAgua,
                      "Familia de indios")
    elementoindios.vai = textoindios.vai

    #CHAMA O PONTO DE INTERROGAÇÃO
    elementoponto = Elemento(img = interroga, 
                     tit = "DUVIDA", 
                     style = dict (top = 420, left = 25, height = 60, width = 55, bottom = 100))
    
    elementoponto.entra(cenaAgua)
    textoponto = Texto(cenaAgua,
                      "EVAPORAÇÃO")
    elementoponto.vai = textoponto.vai


cenaAgua.vai()
cicloagua()


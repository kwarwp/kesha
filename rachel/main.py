# kesha.rachel.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
#from browser import html
ciencia = "https://i.imgur.com/OMOPgC7.png"
urso = "https://i.imgur.com/UvNnOfq.png"
indio ="https://i.imgur.com/acNsNoO.png"
indios ="https://i.imgur.com/RMc3y2v.png"
interrogav = "https://i.imgur.com/vHTik0T.png"
interrogab = "https://i.imgur.com/hHMFVSy.png"
interrogap ="https://i.imgur.com/3DBAXnK.png"
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

    #CHAMA O PONTO DE INTERROGAÇÃO VERMELHO
    elementopontov = Elemento(img = interrogav, 
                     tit = "DUVIDA", 
                     style = dict (top = 500, left = 530, height = 60, width = 55, bottom = 100))
    
    elementopontov.entra(cenaAgua)
    textopontov = Texto(cenaAgua,
                      "EVAPORAÇÃO")
    elementopontov.vai = textopontov.vai
    
    #CHAMA O PONTO DE INTERROGAÇÃO AZUL
    elementopontob = Elemento(img = interrogab, 
                     tit = "DUVIDA", 
                     style = dict (top = 220, left = 370, height = 60, width = 55, bottom = 100))
    
    elementopontob.entra(cenaAgua)
    textopontob = Texto(cenaAgua,
                      "PRECIPITAÇÃO")
    elementopontob.vai = textopontob.vai

#CHAMA O PONTO DE INTERROGAÇÃO PRETO
    elementopontop = Elemento(img = interrogap, 
                     tit = "DUVIDA", 
                     style = dict (top = 30, left = 800, height = 60, width = 55, bottom = 100))
    
    elementopontop.entra(cenaAgua)
    textopontop = Texto(cenaAgua,
                      "CONDENSAÇÃO")
    elementopontop.vai = textopontop.vai

    cenaAgua.vai()
cicloagua()


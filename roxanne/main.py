# kesha.roxanne.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"] = 1200
STYLE ["height"] = "600px"

FASE1 = "https://i.imgur.com/pmlIiGt.png"
FASE2 = "https://i.imgur.com/DailNDQ.png"
FASE3 = "https://i.imgur.com/XWPxvYy.png"
FASE4 = "https://i.imgur.com/KN4hH9Z.png"
FASE5 = "https://i.imgur.com/mlBejyP.png"
FASE6 = "https://i.imgur.com/VgB7jA0.png"
FASE7 = "https://i.imgur.com/BKbYEGn.png"
FASE8 = "https://i.imgur.com/zFlVIXy.png"
FASE9 = "https://i.imgur.com/HyW0l5d.png"
QBRANCO ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMjng-YnBM1AQEgWHVPG5qMq77HU8CYGBlEkaF60eOOBV1CuN1"
QAZUL = "https://i.imgur.com/HUkZFHm.png"
QVERDE = "https://i.imgur.com/hd3ofzP.png"
QVERMELHO = "https://i.imgur.com/K0YpYsi.png"
QSIMBOLO = "https://i.imgur.com/XnMRw3u.png"


class Tabuleiro:
    def __init__(self):
        self.fase1 = Cena(img = FASE1)
        self.linhaA1 = Elemento(QBRANCO, style = dict(
            left= 160, 
            top= "127px", 
            width=101, 
            height="74px"))
        self.linhaB1 = Elemento(QBRANCO, style = dict(
            left= 261, 
            top= "127px", 
            width=101, 
            height="74px"))
        self.linhaC1 = Elemento(QBRANCO, style = dict(
            left= 362, 
            top= "127px", 
            width=101, 
            height="74px"))
        self.linhaA1.entra(self.fase1)
        self.linhaB1.entra(self.fase1)
        self.linhaC1.entra(self.fase1)
        
        self.linhaA2 = Elemento(QBRANCO, style = dict(
            left= 160, 
            top= "201px", 
            width=101, 
            height="74px"))
        self.linhaB2 = Elemento(QBRANCO, style = dict(
            left= 261, 
            top= "201px", 
            width=101, 
            height="74px"))
        self.linhaC2 = Elemento(QBRANCO, style = dict(
            left= 362, 
            top= "201px", 
            width=101, 
            height="74px"))
        self.linhaA2.entra(self.fase1)
        self.linhaB2.entra(self.fase1)
        self.linhaC2.entra(self.fase1)
        
        
        self.linhaA3 = Elemento(QBRANCO, style = dict(
            left= 160, 
            top= "275px", 
            width=101, 
            height="74px"))
        self.linhaB3 = Elemento(QBRANCO, style = dict(
            left= 261, 
            top= "275px", 
            width=101, 
            height="74px"))
        self.linhaC3 = Elemento(QBRANCO, style = dict(
            left= 362, 
            top= "275px", 
            width=101, 
            height="74px"))
        self.linhaA3.entra(self.fase1)
        self.linhaB3.entra(self.fase1)
        self.linhaC3.entra(self.fase1)
        
        self.linhaA4 = Elemento(QBRANCO, style = dict(
            left= 160, 
            top= "349px", 
            width=101, 
            height="74px"))
        self.linhaB4 = Elemento(QBRANCO, style = dict(
            left= 261, 
            top= "349px", 
            width=101, 
            height="74px"))
        self.linhaC4 = Elemento(QBRANCO, style = dict(
            left= 362, 
            top= "349px", 
            width=101, 
            height="74px"))
            
        self.linhaA4.entra(self.fase1)
        self.linhaB4.entra(self.fase1)
        self.linhaC4.entra(self.fase1)
        self.fase1.vai()


"""
self.fase2 = Cena(img = Fase2)
        self.fase2.vai()
        self.fase3 = Cena(img = Fase3)
        self.fase3.vai()
        self.fase4 = Cena(img = Fase4)
        self.fase4.vai()
        self.fase5 = Cena(img = Fase5)
        self.fase5.vai()
        self.fase6 = Cena(img = Fase6)
        self.fase6.vai()
        self.fase7 = Cena(img = Fase7)
        self.fase7.vai()
        self.fase8 = Cena(img = Fase8)
        self.fase8.vai()
        self.fase9 = Cena(img = Fase9)
        self.fase9.vai()
        
              
        self.fase1 = Elemento(img = FASE1, tit = "SIMETRICO 3 X 4", style = dict(left=200, top="100px", width=540, height="320px"))
        self.fase1.entra(self.noite)
        self.qsimbolo = Elemento(img = QSIMBOLO, style = dict(for  simbol in range(4):
        	left=100+ simbol, 
            top="50px",
            width=40, 
            height="40px"))
     self.qsimbolo.entra(self.fase1)

### TABULEIRO RESPOSTA ####
        TBRX, TBRY = 200, 100
        self.r0= Elemento(QBRANCO,style=dict(width=TBRX, height=TBRY, left=751, top=55))
        self.r = Elemento(QAZUL,style=dict(width=TBRX, height=TBRY, left=800, top=55))
        for qbranco in range(3):
        for qbranco in range(4):
        self.tabuleiro_respostas = {}
        
inicio_resp_x, inicio_resp_y = 754, 62
for coluna in range(3):
for linha in range(4):
nome = "{}_{}".format(linha, coluna)
self.tabuleiro_respostas[nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
width=TBRX-11, height="{}px".format(TBRY-52), left=inicio_resp_x+coluna*TBRX, top=inicio_resp_y+linha*TBRY))
self.tabuleiro_respostas[nome].entra(tabelafase1)
self.tabuleiro_respostas[nome].img.id = nome
self.tabuleiro_respostas[nome].elt.onclick = move_carta
"""

Tabuleiro ()



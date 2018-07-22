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
QBRANCO ="https://i.imgur.com/9PMJ1tD.png"
QAZUL = "https://i.imgur.com/HUkZFHm.png"
QVERDE = "https://i.imgur.com/hd3ofzP.png"
QVERMELHO = "https://i.imgur.com/K0YpYsi.png"
QSIMBOLO = "https://i.imgur.com/XnMRw3u.png"


class Tabuleiro:
    def __init__(self):
        self.fase1 = Cena(img = FASE1)
        self.linha = Elemento(QBRANCO, style = dict(
            left= 165, 
            top= "127px", 
            width=95, 
            height="72px"))
        self.linha1 = Elemento(QBRANCO, style = dict(
            left= 265, 
            top= "127px", 
            width=95, 
            height="72px"))
        self.linha2 = Elemento(QBRANCO, style = dict(
            left= 3*165, 
            top= "127px", 
            width=95, 
            height="72px"))
             
        self.linha.entra(self.fase1)
        self.linha1.entra(self.fase1)
        self.linha2.entra(self.fase1)
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



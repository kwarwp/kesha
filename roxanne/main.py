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
        self.noite.vai()
        self.fase1 = Elemento(img = FASE1, tit = "SIMETRICO 3 X 4", style = dict(left=200, top="100px", width=540, height="320px"))
        self.fase1.entra(self.noite)
        self.qsimbolo = Elemento(img = QSIMBOLO, style = dict(left=100, top="50px", width=40, height="40px"))
        self.qsimbolo.entra(self.fase1)
HELLO 
"""### TABULEIRO RESPOSTA ####
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


Tabuleiro ()



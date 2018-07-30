# kesha.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from browser import html, document, alert, doc
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
#scene.background= color.white
#scene.width = 800
#scene.height = 600

STYLE["width"]=800
STYLE["height"]="600px"
FUNDO = "https://i.imgur.com/EzWk7Jl.jpg" 
#FUNDO_BRANCO = "https://i.imgur.com/UXD0mzp.png"
QAZUL = "https://i.imgur.com/lWDGIvc.jpg"
#QVERMELHO = "https://i.imgur.com/K0YpYsi.png"
#QVERDE = "https://i.imgur.com/hd3ofzP.png"
Pilha_Cartas_top = 30
Pilha_Cartas_left = 30

class Tabuleiro:
    def _3d_(self):
        doc['py3d'].html=''
        _gs=Glow('py3d')
        scene=canvas()

        bloco = dict(color=color.blue)
        simetria1=box(pos=(4.2, -2, 0), size=(1,1,1) , **bloco)
        simetria2=box(pos=(1.8, 1.6, 0), size=(1,1,1) , **bloco)
        simetria = [box(pos=(3, x*(1.2)-2, 0), size=(1,1,1), **bloco) for x in range(4)]
        pts = [simetria1, simetria2]+simetria
        sup = compound(pts, pos=vec(2,0,0), axis=vec(4,0,-1))

    def __init__(self):
            self.linhaA1 = Elemento(FUNDO, tit = "py3d", style = dict(
                left= 800, 
                top= "10px", 
                width=600, 
                height="600px"))
    
            def remover_carta(ev):
                carta_elt = ev.target.parent_id
                doc[carta_elt].remove()
                cria_carta(carta_elt)
                ev.stopPropagation()
                return False
            
            def move_carta(casa):
                casa_destino = casa.target.id
                tabuleiro_target = "esquerda" #casa.target.tabuleiro
                carta_a_mover = self.lista_de_cartas.pop()
                self.cartas_no_tabuleiro.append(carta_a_mover)
                elemento_casa_do_tabuleiro = self.tabuleiro[tabuleiro_target][casa_destino].elt
                carta_a_mover.elt.style.left  = elemento_casa_do_tabuleiro.style.left
                carta_a_mover.elt.style.top  = elemento_casa_do_tabuleiro.style.top
                carta_a_mover.elt.onclick = remover_carta
            self.tabela_fase1 = tabelafase1 = Cena(img=FUNDO)
            self.lista_de_cartas =[]
            self.cartas_no_tabuleiro = []
            ### TABULEIRO DA ESQUERDA E DA DIREITA####
            TBX, TBY = 80, 80
            self.tabuleiro = dict(esquerda = {}, direita = {})
            inicio_x, inicio_y = 390, 128 
            for coluna_ in range(3): 
                for linha_ in range(4): 
                    nome = "{}_{}".format(linha_, coluna_)
                    self.tabuleiro["esquerda"][nome] = Elemento(FUNDO, tit=nome+"_", style=dict(
                        width=TBX-15, height="{}px".format(TBY-8), left=inicio_x - coluna_*TBX - (TBX-15), top=inicio_y+linha_*TBY))#-15 o quadradinho diminui na largura
                    self.tabuleiro["esquerda"][nome].entra(tabelafase1)
                    self.tabuleiro["esquerda"][nome].img.id = nome
                    self.tabuleiro["esquerda"][nome].elt.onclick = move_carta
                ###PILHA DE CARTAS###
            #self.lista_de_cartas = [Elemento (QAZUL, tit= "carta%d"%i, cena=tabelafase1, style=dict(
                #width="65px", height="70px", left=Pilha_Cartas_left, top=Pilha_Cartas_top)) for i in range(12)]
            def cria_carta(carta_id):
                a_carta_a_ser_empilhada = Elemento (QAZUL, tit= carta_id, style=dict(
                width="65px", height="70px", left=Pilha_Cartas_left, top=Pilha_Cartas_top)) 

                self.lista_de_cartas.append(a_carta_a_ser_empilhada)
                a_carta_a_ser_empilhada.img.parent_id = carta_id
                a_carta_a_ser_empilhada.entra(tabelafase1)
            for i in range(12) : #carta in Pilha_Cartas:
                cria_carta("carta%d"%i)

            def recoloca_clique_aqui(_):
                self.cliqueaqui.entra(tabelafase1)
            
            tabelafase1.vai()
            self.linhaA1.entra(tabelafase1) 
            self._3d_()

Tabuleiro()
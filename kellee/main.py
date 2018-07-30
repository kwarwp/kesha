# kesha.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, INVENTARIO
from browser import html, document, alert, doc
from _spy.vpython.main import *

STYLE["width"] = 800
STYLE["height"] = "600px"
FUNDO = "https://i.imgur.com/EzWk7Jl.jpg"
# FUNDO_BRANCO = "https://i.imgur.com/UXD0mzp.png"
QAZUL = "https://i.imgur.com/lWDGIvc.jpg"
# QVERMELHO = "https://i.imgur.com/K0YpYsi.png"
# QVERDE = "https://i.imgur.com/hd3ofzP.png"
Pilha_Cartas_top = 30
Pilha_Cartas_left = 30
TBX, TBY = 80, 80
inicio_x, inicio_y = 390, 128


class Tabuleiro:
    def _3d_(self):
        doc['py3d'].html = ''
        _gs = Glow('py3d')
        scene = canvas()

        bloco = dict(color=color.blue)
        simetria1 = box(pos=(4.2, -2, 0), size=(1, 1, 1), **bloco)
        simetria2 = box(pos=(1.8, 1.6, 0), size=(1, 1, 1), **bloco)
        simetria = [box(pos=(3, x * (1.2) - 2, 0), size=(1, 1, 1), **bloco) for x in range(4)]
        pts = [simetria1, simetria2] + simetria
        sup = compound(pts, pos=vec(2, 0, 0), axis=vec(4, 0, -1))

    def __init__(self, nome="esquerda"):
        self.casa = {}
        self.nome = nome
        self.elemento = tabuleiro_construido = Cena(img=FUNDO)
        self.pilha_de_cartas = []
        self.display_do_3D = Elemento(FUNDO, tit="py3d", style=dict(
            left=800,
            top="10px",
            width=600,
            height="600px"))
        ### TABULEIRO DA ESQUERDA E DA DIREITA####
        self.cria_tabuleiro(col=3, lin=4)

        ###PILHA DE CARTAS###

        for i in range(12):
            Carta(self, "carta_{}".format(i))


        tabuleiro_construido.vai()
        self.display_do_3D.entra(tabuleiro_construido)
        self._3d_()

    def cria_tabuleiro(self, col=3, lin=4):
        INVENTARIO.score(casa="centro_9_9", carta="carta_99", move="INICIA", ponto=0, valor="N", _level=1)
        self.casa["esquerda"] = {}
        for coluna_ in range(col):
            for linha_ in range(lin):
                nome = "{}_{}".format(linha_, coluna_)
                self.casa["esquerda"][nome] = Casa(self, nome=nome, linha=linha_, coluna=coluna_)

    def _entra(self, parte):
        self.elemento.entra(parte)

    def empilha(self, parte):
        self.pilha_de_cartas.append(parte)

    def proxima_carta(self):
        return self.pilha_de_cartas.pop()


class Carta:
    def __init__(self, tabuleiro, carta_id):
        self.tabuleiro = tabuleiro
        self.elemento = None
        self.nome = carta_id
        self.casa = None
        self.cria_carta(carta_id)

    def cria_carta(self, carta_id):
        self.elemento = a_carta_a_ser_empilhada = Elemento(QAZUL, tit=carta_id, style=dict(
            width="65px", height="70px", left=Pilha_Cartas_left, top=Pilha_Cartas_top))
        self.tabuleiro.empilha(self)
        a_carta_a_ser_empilhada.img.parent_id = carta_id
        a_carta_a_ser_empilhada.entra(self.tabuleiro.elemento)
        a_carta_a_ser_empilhada.elt.onclick = self.remover_carta

    @classmethod
    def move_carta(cls, tabuleiro, casa_destino):
        carta_a_mover = tabuleiro.proxima_carta()
        carta_a_mover.move(casa_destino)

    def crivo(self):
        return 10

    def move(self, casa_destino):
        self.elemento.elt.style.left, self.elemento.elt.style.top = casa_destino.local()
        self.casa = casa_destino.nome
        INVENTARIO.score(casa=casa_destino.nome, carta=self.nome, move="MOVE", ponto=self.crivo(), valor="N", _level=3)


    def remover_carta(self, ev):
        carta_elt = ev.target.parent_id
        doc[carta_elt].remove()
        self.cria_carta(carta_elt)
        ev.stopPropagation()
        INVENTARIO.score(casa=self.casa.nome, carta=carta_elt, move="REMOVE", ponto=-1, valor="N", _level=3)
        return False


class Casa:
    CASA = {}
    def __init__(self, tabuleiro, nome='0_0', linha=0, coluna=0):
        self.nome = nome_elemento = "{}_{}".format(tabuleiro.nome, nome)
        self.elemento = Elemento(FUNDO, tit=nome_elemento + "_", style=dict(
                width=TBX - 15, height="{}px".format(TBY - 8), left=inicio_x - coluna * TBX - (TBX - 15),
                top=inicio_y + linha * TBY))  # -15 o quadradinho diminui na largura
        self.tabuleiro = tabuleiro
        self.elemento.entra(tabuleiro.elemento)
        self.elemento.img.id = nome_elemento
        Casa.CASA[nome_elemento] = self

        self.elemento.elt.onclick = self.move_carta


    def local(self):
        return self.elemento.elt.style.left, self.elemento.elt.style.top

    def move_carta(self, casa):
        casa_destino = casa.target.id
        Carta.move_carta(self.tabuleiro, Casa.CASA[casa_destino])


Tabuleiro()
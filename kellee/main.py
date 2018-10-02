# kesha.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, INVENTARIO
from browser import html, document, alert, doc
from _spy.vpython.main import *
STYLE["width"] = 700
STYLE["height"] = "600px"
FUNDO = "https://i.imgur.com/EzWk7Jl.jpg"
QAZUL = "https://i.imgur.com/lWDGIvc.jpg"

TENTAR = "https://i.imgur.com/PRjuqrZ.png"
DESISTO = "https://i.imgur.com/GkqfWc3.png"
NAOQUEROJOGAR = "https://i.imgur.com/8JGhyAA.png"
TERMINEI = "https://i.imgur.com/9dtdzcP.png"
JATERMINEI = "https://i.imgur.com/2OIhpY3.png"
BUTTONS = [TENTAR, DESISTO, NAOQUEROJOGAR, TERMINEI, JATERMINEI]

Pilha_Cartas_top = 30
Pilha_Cartas_left = 30
TBX, TBY = 80, 80
inicio_x, inicio_y = 290, 128
FASE0 = dict(numcartas=12, lado="e")
FASE1 = dict(numcartas=24, lado="ed")
FASE2 = dict(numcartas=30, lado="ed", linha=5)
FASE3 = dict(numcartas=12, lado="e", _3d=1)
FASE4 = dict(numcartas=15, lado="e", _3d=2)
offset = dict(e=0, d=300)


class Tabuleiro:
    # Cria figura fase 3 em 3d
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
        
    # Cria figura fase 4 em 3d        
    def _3da_(self):
        doc['py3d'].html = ''
        _gs = Glow('py3d')
        scene = canvas()
        bloco = dict(color=color.blue)
        bloco1 = dict(color=color.white)

        cubo1=box(pos=(1, -1.2, 0), size=(1,1,1) , **bloco)
        cubo2=box(pos=(1, 0, 0), size=(1,1,1) , **bloco)
        cubo3=box(pos=(-0.2, 0, 0), size=(1,1,1) , **bloco)
        cubo4=box(pos=(-0.2, 1.2, 0), size=(1,1,1) , **bloco)
        cubo5=box(pos=(-0.2, 1.2, 1.2), size=(1,1,1) , **bloco)
        cubo5=box(pos=(-0.2, 0, -1.2), size=(1,1,1) , **bloco)
        cubo6=box(pos=(-1.4, 0, 0), size=(1,1,1) , **bloco1)
        cubo7=box(pos=(0, -2.4, 1.2), size=(1,1,1) , **bloco1)
        cubo8=box(pos=(-1.2, -2.4, -1.2), size=(1,1,1) , **bloco1)
        cubo9=box(pos=(-1.2, -3.6, -1.2), size=(1,1,1) , **bloco1)


        
    # Cria os botoes  embaixo e nome das casas          
    def __init__(self, nome="esquerda", numcartas=12, lado="e", linha=4, _3d=False):
        self.casa = {}
        self.numcartas, self.lado, self.linha = numcartas, lado, linha
        self.eventos = dict(button_0=lambda:self.score("replay", vai=True), 
            button_1=lambda:self.score("recusa"), 
            button_2=lambda:self.score("Desiste"), 
            button_3=lambda:self.score("errado"), 
            button_4=lambda:self.score("certo")) 
        
        self.nome, self._3d = nome, _3d
        self.elemento = tabuleiro_construido = Cena(img=FUNDO)
        self.pilha_de_cartas = []
        for i,button in enumerate(BUTTONS):
            elem = Elemento(button, cena=self.elemento, vai=self.buttonapertado,tit="button_{}_".format(i), style=dict(
                        left=100 + 110*i,
                        top="540px",
                        width=100,
                        height="30px"))
            elem.img.id = "button_{}".format(i)
        self.inicia_fase()
        
    # Cria as grades        
    def inicia_fase(self):
        [self.cria_tabuleiro(col=3, lin=self.linha, lado=l) for l in self.lado]
        for i in range(self.numcartas):
            Carta(self, "carta_{}".format(i))
    
    def score(self, valor, vai=False):
        INVENTARIO.score(casa="centro_9_9", carta="carta_99", move="INICIA", ponto=0, valor=valor, _level=2)
        if vai:
            self.inicia_fase()
        else:
            Jogo.JOGO.reset()
        
    def buttonapertado(self, env):
        print(env.target.id)
        if "button" not in env.target.id:
            return True
        self.eventos[env.target.id]()
        
    def vai(self):
        self.elemento.vai()
        print(self._3d, len(self.pilha_de_cartas))
        if self._3d:
            self.display_do_3D = Elemento(FUNDO, tit="py3d", style=dict(
                left=700,
                top="10px",
                width=300,
                height="600px"))
            self.display_do_3D.entra(self.elemento)
            if self._3d == 1:
                self._3d_()
            else:
                self._3da_()

    def proximafase(self, tabuleiro):
        self.elemento.direita = tabuleiro #.elemento

    def cria_tabuleiro(self, col=3, lin=4, lado="e"):
        INVENTARIO.score(casa="centro_9_9", carta="carta_99", move="INICIA", ponto=0, valor="N", _level=1)
        self.casa["esquerda"] = {}
        for coluna_ in range(col):
            for linha_ in range(lin):
                nome = "{}_{}_{}".format(linha_, coluna_, lado)
                self.casa["esquerda"][nome] = Casa(self, nome=nome, linha=linha_, coluna=coluna_, lado=lado)

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
        INVENTARIO.score(casa=self.casa, carta=carta_elt, move="REMOVE", ponto=-1, valor="N", _level=3)
        ev.stopPropagation()
        return False

class Casa:
    CASA = {}
    def __init__(self, tabuleiro, nome='0_0', linha=0, coluna=0, lado="e"):
        inicio_x_ = inicio_x + offset[lado]
        self.nome = nome_elemento = "{}_{}".format(tabuleiro.nome, nome)
        self.elemento = Elemento(FUNDO, tit=nome_elemento + "_", style=dict(
                width=TBX - 15, height="{}px".format(TBY - 8), left=inicio_x_ - coluna * TBX - (TBX - 15),
                top=inicio_y + linha * TBY))  
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

class Jogo:
    JOGO = None
    def __init__(self):
        Jogo.JOGO = self
        self.reset()
        
    def reset(self):
        self.tabuleiro =  Tabuleiro()
        proximafase = Tabuleiro(**FASE1)
        self.tabuleiro.proximafase(proximafase)
        proximafase2 = Tabuleiro(**FASE2)
        proximafase.proximafase(proximafase2)        
        proximafase3 = Tabuleiro(**FASE3)
        proximafase2.proximafase(proximafase3)
        #proximafase4 = Tabuleiro(**FASE4)
        #proximafase3.proximafase(proximafase4)
        self.tabuleiro.vai()
Jogo()
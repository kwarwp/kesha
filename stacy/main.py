# kesha.stacy.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from browser import html, document, alert

STYLE["width"]=800
STYLE["height"]="600px"
FUNDO = "https://i.imgur.com/EzWk7Jl.jpg" 
FUNDO_BRANCO = "https://i.imgur.com/UXD0mzp.png"
QAZUL = "https://i.imgur.com/lWDGIvc.jpg"
#crivo#
pontos_altos = ""
pontos_medios = ""
pontos_fracos = ""
#deixar errar
TABELAFASE2 ="https://i.imgur.com/EzWk7Jl.jpg"
tabelafase2 = Cena(img=TABELAFASE2)
class Tabuleiro:

    def __init__ (self):
        """def remover_carta(carta):
            self.lista_de_cartas.append(carta)
            carta.elt.style.left = Pilha_cartas_left
            carta.elt.style.top = Pilha_cartas_top
            self.tabuleiro[carta.img.tabuleiro][casa.img.casa].img.ocupado = 0
            carta.img.tabuleiro = "null"
            carta.img.casa = "null"
           """ 
        def move_carta(casa):
            casa_destino = casa.target.id
            tabuleiro_target = casa.target.tabuleiro
            #if(casa.target.ocupado == 0):
             #   if((tabuleiro_target == "esquerda" and self.tabuleiro["direita"][casa_destino].img.ocupado == 1)
                #  or tabuleiro_target == "direita"):
                #     casa.target.ocupado = 1
                    
            carta_a_mover = self.lista_de_cartas.pop()
            self.cartas_no_tabuleiro.append(carta_a_mover)
            elemento_casa_do_tabuleiro = self.tabuleiro[tabuleiro_target][casa_destino].elt
            
            carta_a_mover.elt.style.left  = elemento_casa_do_tabuleiro.style.left
            carta_a_mover.elt.style.top  = elemento_casa_do_tabuleiro.style.top
            carta_a_mover.elt.onclick = remover_carta
            carta_a_mover.img.casa = casa_destino
            carta_a_mover.img.tabuleiro = tabuleiro_target
        
            
        
        self.tabela_fase1 = tabelafase1 = Cena(img=FUNDO)
        
            
        self.lista_de_cartas =[]
        self.cartas_no_tabuleiro = []
        Pilha_Cartas = []
        for f in range (24):
            Pilha_Cartas.append(QAZUL)
        
                
        
        ### TABULEIRO DA ESQUERDA E DA DIREITA####
        TBX, TBY = 80, 80
        self.tabuleiro = dict(esquerda = {}, direita = {})
        inicio_x, inicio_y = 390, 128 
        
        for coluna_ in range(3): 
            for linha_ in range(4): 
                nome = "{}_{}".format(linha_, coluna_)
                self.tabuleiro["esquerda"][nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                    width=TBX-15, height="{}px".format(TBY-8), left=inicio_x - coluna_*TBX - (TBX-15), top=inicio_y+linha_*TBY))#-15 o quadradinho diminui na largura
                self.tabuleiro["esquerda"][nome].entra(tabelafase1)
                self.tabuleiro["esquerda"][nome].img.id = nome
                self.tabuleiro["esquerda"][nome].img.tabuleiro = "esquerda"
                self.tabuleiro["esquerda"][nome].img.ocupado = 0
                self.tabuleiro["esquerda"][nome].elt.onclick = move_carta   

        inicio_x, inicio_y = 430, 128  
        
        for coluna_ in range(3): 
            for linha_ in range(4):
                nome = "{}_{}".format(linha_, coluna_)
                self.tabuleiro["direita"][nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                    width=TBX-15, height="{}px".format(TBY-8), left=inicio_x+coluna_*TBX, top=inicio_y+linha_*TBY))

                self.tabuleiro["direita"][nome].entra(tabelafase1)
                self.tabuleiro["direita"][nome].img.id = nome
                self.tabuleiro["direita"][nome].img.tabuleiro = "direita"
                self.tabuleiro["direita"][nome].img.ocupado = 0
                self.tabuleiro["direita"][nome].elt.onclick = move_carta    
        
        ###PILHA DE CARTAS###
        Pilha_Cartas_top = 30
        Pilha_Cartas_left = 30
        for carta in Pilha_Cartas:
            a_carta_a_ser_empilhada = Elemento (carta, tit= "carta", style=dict(
            width="65px", height="70px", left=Pilha_Cartas_left, top=Pilha_Cartas_top)) 
            a_carta_a_ser_empilhada.img.casa = "null"
            a_carta_a_ser_empilhada.img.tabuleiro = "null"
        
            self.lista_de_cartas.append(a_carta_a_ser_empilhada)
            a_carta_a_ser_empilhada.entra(tabelafase1)

        def recoloca_clique_aqui(_):
            self.cliqueaqui.entra(tabelafase1)
            
        for nome in self.tabuleiro["direita"]:
            self.tabuleiro["direita"][nome].elt.onclick = recoloca_clique_aqui
        for nome in self.tabuleiro["esquerda"]:
            self.tabuleiro["esquerda"][nome].elt.onclick = recoloca_clique_aqui

        def segunda_fase(self)
            
            class Tabuleiro2:

                def __init__ (self):
        """def remover_carta(carta):
            self.lista_de_cartas.append(carta)
            carta.elt.style.left = Pilha_cartas_left
            carta.elt.style.top = Pilha_cartas_top
            self.tabuleiro[carta.img.tabuleiro][casa.img.casa].img.ocupado = 0
            carta.img.tabuleiro = "null"
            carta.img.casa = "null"
           """ 
                   def move_carta(casa):
                       casa_destino = casa.target.id
                       tabuleiro_target = casa.target.tabuleiro
            #if(casa.target.ocupado == 0):
             #   if((tabuleiro_target == "esquerda" and self.tabuleiro["direita"][casa_destino].img.ocupado == 1)
                #  or tabuleiro_target == "direita"):
                #     casa.target.ocupado = 1
                    
                        carta_a_mover = self.lista_de_cartas.pop()
                        self.cartas_no_tabuleiro.append(carta_a_mover)
                        elemento_casa_do_tabuleiro = self.tabuleiro[tabuleiro_target][casa_destino].elt
            
                        carta_a_mover.elt.style.left  = elemento_casa_do_tabuleiro.style.left
                        carta_a_mover.elt.style.top  = elemento_casa_do_tabuleiro.style.top
                        carta_a_mover.elt.onclick = remover_carta
                        carta_a_mover.img.casa = casa_destino
                        carta_a_mover.img.tabuleiro = tabuleiro_target
        
                self.tabela_fase2 = tabelafase2 = Cena(img=FUNDO)
                self.lista_de_cartas =[]
                self.cartas_no_tabuleiro = []
                Pilha_Cartas = []
                for f in range (36):
                    Pilha_Cartas.append(QAZUL)
        
                
        
        ### TABULEIRO DA ESQUERDA E DA DIREITA####
                TBX, TBY = 80, 80
                self.tabuleiro = dict(esquerda = {}, direita = {})
                inicio_x, inicio_y = 390, 128 
        
                for coluna_ in range(3): 
                    for linha_ in range(6): 
                        nome = "{}_{}".format(linha_, coluna_)
                        self.tabuleiro["esquerda"][nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                            width=TBX-15, height="{}px".format(TBY-8), left=inicio_x - coluna_*TBX - (TBX-15), top=inicio_y+linha_*TBY))#-15 o quadradinho diminui na largura
                        self.tabuleiro["esquerda"][nome].entra(tabelafase1)
                        self.tabuleiro["esquerda"][nome].img.id = nome
                        self.tabuleiro["esquerda"][nome].img.tabuleiro = "esquerda"
                        self.tabuleiro["esquerda"][nome].img.ocupado = 0
                        self.tabuleiro["esquerda"][nome].elt.onclick = move_carta   

                inicio_x, inicio_y = 430, 128  
        
                for coluna_ in range(3): 
                   for linha_ in range(6):
                        nome = "{}_{}".format(linha_, coluna_)
                        self.tabuleiro["direita"][nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                            width=TBX-15, height="{}px".format(TBY-8), left=inicio_x+coluna_*TBX, top=inicio_y+linha_*TBY))

                        self.tabuleiro["direita"][nome].entra(tabelafase1)
                        self.tabuleiro["direita"][nome].img.id = nome
                        self.tabuleiro["direita"][nome].img.tabuleiro = "direita"
                        self.tabuleiro["direita"][nome].img.ocupado = 0
                        self.tabuleiro["direita"][nome].elt.onclick = move_carta    
        
        ###PILHA DE CARTAS###
                Pilha_Cartas_top = 30
                Pilha_Cartas_left = 30
                for carta in Pilha_Cartas:
                    a_carta_a_ser_empilhada = Elemento (carta, tit= "carta", style=dict(
                    width="65px", height="70px", left=Pilha_Cartas_left, top=Pilha_Cartas_top)) 
                    a_carta_a_ser_empilhada.img.casa = "null"
                    a_carta_a_ser_empilhada.img.tabuleiro = "null"
        
                self.lista_de_cartas.append(a_carta_a_ser_empilhada)
                   a_carta_a_ser_empilhada.entra(tabelafase1)

                def recoloca_clique_aqui(_):
                    self.cliqueaqui.entra(tabelafase2)
            
                for nome in self.tabuleiro["direita"]:
                    self.tabuleiro["direita"][nome].elt.onclick = recoloca_clique_aqui
                for nome in self.tabuleiro["esquerda"]:
                    self.tabuleiro["esquerda"][nome].elt.onclick = recoloca_clique_aqui


            #tabelafase1.direita = segunda_fase.vai()
            #if tabelafase1.direita(self):
                #self.segunda_fase()        
            #Tabuleiro2()   
            
        tabelafase1.vai()

Tabuleiro()

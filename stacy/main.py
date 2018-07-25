# kesha.stacy.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from browser import html, document

STYLE["width"]=800
STYLE["height"]="600px"
FUNDO = "https://i.imgur.com/EzWk7Jl.jpg" #quadradinho branco
FUNDO_BRANCO = "https://i.imgur.com/UXD0mzp.png"
#FASE1 = "https://i.imgur.com/X3oxHIz.png" #imagem estrelas
#FASE2 = "https://i.imgur.com/DailNDQ.png"
#FASE3 = "https://i.imgur.com/XWPxvYy.png"
#FASE4 = "https://i.imgur.com/KN4hH9Z.png"
#FASE5 = "https://i.imgur.com/mlBejyP.png"
#FASE6 = "https://i.imgur.com/VgB7jA0.png"
#FASE7 = "https://i.imgur.com/BKbYEGn.png"
#FASE8 = "https://i.imgur.com/zFlVIXy.png"
#FASE9 = "https://i.imgur.com/HyW0l5d.png"
#QBRANCO ="https://i.imgur.com/EzWk7Jl.jpg"
QAZUL = "https://i.imgur.com/lWDGIvc.jpg"
#QVERDE = "https://i.imgur.com/hd3ofzP.png"
#QVERMELHO = "https://i.imgur.com/K0YpYsi.png"
#QSIMBOLO = "https://i.imgur.com/XnMRw3u.png"
#TRANSP = "https://i.imgur.com/UXD0mzp.png"
#cliques_altos = [""] 
#cliques_altos ==  3
#cliques_medios = ["bat", "gir", "colo", "manipul", "mov", "surg", "peg", "levant", "bat"]
#cliques_medios ==  2

#cliques_fracos = ["rod", "bot", "sub", "pux", "form", "tent", "cli", "abaix", "mex", "encost", "rel"] 
#cliques_fracos ==  1
#cliques = [ (3,verbos_altos),(2,verbos_medios),(1,verbos_fracos)]


class Tabuleiro:

    def __init__ (self):
        def move_carta(casa):
            carta_a_mover = self.lista_de_cartas.pop()
            casa_destino = casa.target.id
            tabuleiro_target = casa.target.tabuleiro
            self.cliqueaqui.elt.style.left=40
            elemento_casa_do_tabuleiro = self.tabuleiro[tabuleiro_target][casa_destino].elt
            cx, cy =  carta_a_mover.posicao_certa
            tx, ty =  self.tabuleiro[tabuleiro_target][casa_destino].posicao_certa
            
            carta_a_mover.elt.style.left = x = elemento_casa_do_tabuleiro.style.left
            carta_a_mover.elt.style.top = y = elemento_casa_do_tabuleiro.style.top
            pos = elemento_casa_do_tabuleiro.title
            
        
        self.tabela_fase1 = tabelafase1 = Cena(img=FUNDO)
        
            
        self.lista_de_cartas =[]
        Pilha_Cartas = [QAZUL, QAZUL, QAZUL, QAZUL,\
        QAZUL, QAZUL, QAZUL,QAZUL,\
        QAZUL, QAZUL, QAZUL, QAZUL] #lista das cartas
        
        Resposta_Cartas = [(QAZUL,"0_1","0_2 0_3 0_0"), (QAZUL, "3_0","0_2 0_3 0_0"),\
        (QAZUL, "2_2","0_2 0_3 0_0"), (QAZUL, "1_3","0_2 0_3 0_0")]
        
        respostas= "1_3,2_2,3_0,0_1,1_3,2_2,3_0,0_1,1_3,2_2,3_0,0_1,1_3,2_2,3_0,0_1"
        self.resposta_certa = {nome:pos.split("_") for nome,pos in zip(Pilha_Cartas,respostas.split(","))}
                                 
        
        ### PILHA DE CARTAS ###
        for carta in Pilha_Cartas:
            a_carta_a_ser_empilhada = Elemento (carta, tit= "carta", style=dict(
            width="65px", height="70px", left=30, top="30px")) #formatação cartinha azul da pilha
            a_carta_a_ser_empilhada.posicao_certa = self.resposta_certa[carta]
            self.lista_de_cartas.append(a_carta_a_ser_empilhada)
            a_carta_a_ser_empilhada.entra(tabelafase1)
        self.cliqueaqui = Elemento (QAZUL, style=dict(width="1px", height="1px", left=0, top=0))
        self.cliqueaqui.entra (tabelafase1)
        
        ### TABULEIRO DA ESQUERDA E DA DIREITA####
        TBX, TBY = 80, 80
        #self.casa0 = Elemento(QAZUL, tit='0_0', style=dict(width=TBX, height=TBY, left=220, top=120))
        #self.casa = Elemento(QAZUL, tit='0_1', style=dict(width=TBX, height=TBY, left=400, top=140))
        self.tabuleiro = dict(esquerda = {}, direita = {})
        inicio_x, inicio_y = 120, 128 #o tabuleiro inteiro anda em x ou y
        
        for coluna_ in range(3): #3 colunas da tabela da esquerda
            for linha_ in range(4): #4 linhas
                nome = "{}_{}".format(linha_, coluna_)
                self.tabuleiro["esquerda"][nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                    width=TBX-15, height="{}px".format(TBY-8), left=inicio_x+coluna_*TBX, top=inicio_y+linha_*TBY))#-15 o quadradinho diminui na largura
                self.tabuleiro["esquerda"][nome].entra(tabelafase1)
                self.tabuleiro["esquerda"][nome].posicao_certa = nome.split("_")
                self.tabuleiro["esquerda"][nome].img.id = nome
                self.tabuleiro["esquerda"][nome].img.tabuleiro = "esquerda"
                self.tabuleiro["esquerda"][nome].elt.onclick = move_carta   
        #self.tabuleiro = {}        
        inicio_x, inicio_y = 420, 128  
        
        for coluna_ in range(3): #3 colunas da tabela da direita
            for linha_ in range(4):
                nome = "{}_{}".format(linha_, coluna_)
                self.tabuleiro["direita"][nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                    width=TBX-15, height="{}px".format(TBY-8), left=inicio_x+coluna_*TBX, top=inicio_y+linha_*TBY))
         
                self.tabuleiro["direita"][nome].entra(tabelafase1)
                self.tabuleiro["direita"][nome].posicao_certa = nome.split("_")
                self.tabuleiro["direita"][nome].img.id = nome
                self.tabuleiro["direita"][nome].img.tabuleiro = "direita"
                self.tabuleiro["direita"][nome].elt.onclick = move_carta    
                 
        def remove_clique_aqui(_):
            self.cliqueaqui.elt.style.left = -1000
            alert ("OK SERÁ REMOVIDO")
        self.cliqueaqui.elt.onclick = remove_clique_aqui        
               
        def recoloca_clique_aqui(_):
            self.cliqueaqui.entra(tabelafase1)
            
        for nome in self.tabuleiro["direita"]:
        	self.tabuleiro["direita"][nome].elt.onclick = recoloca_clique_aqui
        for nome in self.tabuleiro["esquerda"]:
        	self.tabuleiro["esquerda"][nome].elt.onclick = recoloca_clique_aqui

        
        
        tabelafase1.vai()

Tabuleiro()

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

class Tabuleiro:

    def __init__ (self):
        def move_carta(casa):
            print(casa.target.id)
            print(list(self.tabuleiro.keys()))
            carta_a_mover = self.lista_de_cartas.pop()
            casa_destino = casa.target.id
            self.cliqueaqui.elt.style.left=40
            elemento_casa_do_tabuleiro = self.tabuleiro[casa_destino].elt
            cx, cy =  carta_a_mover.posicao_certa
            tx, ty =  self.tabuleiro[casa_destino].posicao_certa
            pontos = (1 if cx == tx else 0) + (1 if ty == cy else 0)
         
            #alert(pontos)
            
            carta_a_mover.elt.style.left = x = elemento_casa_do_tabuleiro.style.left
            carta_a_mover.elt.style.top = y = elemento_casa_do_tabuleiro.style.top
            pos = elemento_casa_do_tabuleiro.title
            print(elemento_casa_do_tabuleiro.style.left, elemento_casa_do_tabuleiro.style.top)
            print(carta_a_mover.elt.style.left, carta_a_mover.elt.style.top)
            ordem_da_carta = 15 - len(self.lista_de_cartas)
            dica_do_valor = Elemento(RESPOSTA[pontos], style=dict(
               width="80px", height="80px", left= TBRESPX+(ordem_da_carta%4)*TBRX, top= TBRESPY+(ordem_da_carta//4)*TBRY ))            
            dica_do_valor.entra(self.tabela_fase1)
            alert ("Dependendo da carta e da posição escolhida, você receberá uma resposta na tabela numerada.")
            
        
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
        self.tabuleiro = {}
        inicio_x, inicio_y = 120, 218 #o tabuleiro inteiro anda em x ou y
        for coluna_ in range(3): #3 colunas da tabela da esquerda
            for linha_ in range(4): #4 linhas
                nome = "{}_{}".format(linha_, coluna_)
                self.tabuleiro[nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                    width=TBX-15, height="{}px".format(TBY-8), left=inicio_x+coluna_*TBX, top=inicio_y+linha_*TBY-90))#-15 o quadradinho diminui na largura
                self.tabuleiro[nome].entra(tabelafase1)
                self.tabuleiro[nome].posicao_certa = nome.split("_")
                self.tabuleiro[nome].img.id = nome
                
                
            for coluna in range(3): #3 colunas da tabela da direita
                for linha in range(4):
                    nome = "{}_{}".format(linha, coluna)
                    self.tabuleiro[nome] = Elemento(FUNDO_BRANCO, tit=nome+"_", style=dict(
                        width=TBX-15, height="{}px".format(TBY-8), left=inicio_x+coluna*TBX+300, top=inicio_y+linha*TBY-90))
                    self.tabuleiro[nome].entra(tabelafase1)
                    self.tabuleiro[nome].posicao_certa = nome.split("_")
                    self.tabuleiro[nome].img.id = nome
                    self.tabuleiro[nome].elt.onclick = move_carta     

                 
        def remove_clique_aqui(_):
            self.cliqueaqui.elt.style.left = -1000
            alert ("OK SERÁ REMOVIDO")
        self.cliqueaqui.elt.onclick = remove_clique_aqui        
               
        def recoloca_clique_aqui(_):
            self.cliqueaqui.entra(tabelafase1)
        self.tabuleiro[nome].elt.onclick = recoloca_clique_aqui
        
        
        
        tabelafase1.vai()

Tabuleiro()

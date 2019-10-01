# kesha.tracy.main.py
# margaret.lisa.main.py
__author__ = "Carlo E. T. Oliveira carlo@ufrj.br"
from _spy.vitollino.main import Cena, Elemento, INVENTARIO
from ruzwana.main import DI as RDI
from random import shuffle
#from stacy.main import fogo
#from natalia.main import sereiamonstro
IMAGENS = ["FOGO", "PEDRAS", "ARANHA", "MUMIA", "DESMORONAMENTO"]*5
shuffle(IMAGENS)
PERIGOS = {}
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/7GZetDn.jpg"
DI["TESOURO"] = "https://i.imgur.com/h8MfuRD.jpg"
TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]


class Acampamento:
    def __init__(self):
        """ o que tem que ter no acampamento?"""
        self.cena = Cena("https://i.imgur.com/dmSDeDF.jpg")
        
    def vai(self):
        self.cena.vai()
    


class Jogador:
    def __init__(self, acampamento):
        """ o que tem que ter no jogador?
            o jogador ganha uma turquesa para cada camara
        """
        self.turquesa = 0
        self.acampamento = acampamento
        #aparato para capturar a ação clica na direita
        self.cena_continua = Cena() #chupa-cabra ele captura a cena d adireita
        self.cena_continua.vai = self.continua
        #aparato para capturar a ação clica na esquerda
        self.cena_desiste = Cena()
        self.cena_desiste.vai = self.desiste

        
    def continua(self):
        """ entra em nova camara e acumula turquesas """
        self.turquesa = self.turquesa + 1
        self.ganha_uma_turquesa()
        pass
    
    def ganha_uma_turquesa(self):
        """
        ouro = trurquesa //10
        sobra_ouro =ouro%10
        obsidiana = sobra_ouro //5
        tur =sobra_ouro % 5
        """
        
        lugar =  60*self.turquesa
        tur = Elemento(TURQUESA,  tit="Turquesa",
            style=dict(left="50px", top="350px", width="50px",
            height="30px"),
                       cena=self.acampamento.cena)

        #desafio pegar o numero de turquesas, pegar o tanto de ouro
        #numero de obsidianas dividio por 5
        #quero desenhar na cabana usando pepitas de ouro e obsidianas
        #vai ter que desenhar um conjunto de turquesas e um conjunto de obsidianas
        
        
    def desiste(self): #quando desiste coleta turquesas e vai pro acampamento
        """ segue para o acampamento"""
        self.coleta_tesouro()
        self.acampamento.vai()
        
class Tesouro:


class Perigo:
    def __init__(self, imagem, tipo, jogador):
        self.jogador = jogador
        self.cena = Cena(imagem)
        self.tipo = tipo
        # chupa cabra -- aparato
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        self.acampamento = jogador.acampamento
        self.set_esquerda(jogador.cena_desiste)

    def set_direita(self, direita):
        self.cena.direita = direita

    def set_esquerda(self, esquerda):
        self.cena.esquerda = esquerda
    
        
    def vai(self):
        if self.tipo in PERIGOS:
            # deu ruim, já tinha aperecido um perigo
            self.cena.direita = self.acampamento
        else:
            PERIGOS[self.tipo] = 1
        self.jogador.continua()
        self.cena_vai()
        
class Carta:
    def __init__(self, jogador):
        self.jogador = jogador
        self.cartas = [Perigo(
                              RDI[uma_imagem],
                              uma_imagem,
                              jogador) 
            for uma_imagem in IMAGENS]
        for ordem, carta in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                carta.set_direita(self.cartas[ordem+1])
    def baralho(self):
        return self.cartas
        
class Jogo:
    def __init__(self):
        global PERIGOS
        PERIGOS ={}
        INVENTARIO.inicia()
        #INVENTARIO.bota(tur)
        self.acampamento = Acampamento()
        self.jogador = Jogador(self.acampamento)
        self.baralho = Carta(self.jogador).baralho()
        self.templo = Cena(DI["TEMPLO"])
        #self.templo = Perigo(tipo="TEMPLO", imagem=DI["TEMPLO"])
        self.templo.direita = self.baralho[1]
    def inicia(self):
        self.templo.vai()
        

inca = Jogo()  # Inca()

if __name__ == "__main__":
    inca.inicia()
    
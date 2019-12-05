# kesha.morgan.main.py
# sarah.roxanne.main.py
#Autor: Isabel Hortencia Garnica
from _spy.vitollino.main import Cena, Elemento, INVENTARIO, STYLE, Musica
from texto.main import Texto

#STYLE.update(width=1300, height=500)
TRACK = "https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3"
SOMA = "https://i.imgur.com/Rpo5MDy.png"
SOMB = "https://i.imgur.com/Hysq98H.png"
CENAINICIO = "https://i.imgur.com/3qdowNm.jpg"
PREDIO= "https://i.imgur.com/vL9kR9Y.png"
CESTA = "https://i.imgur.com/qtw6IoO.png"
DOG = "https://i.imgur.com/ZQ9SSMz.png"
MENINOHAPPY = "https://i.imgur.com/LsinOyd.png"
MENINOSAD = "https://i.imgur.com/x3JZ93M.png"
IRMAHAPPY = "https://i.imgur.com/XZJuxnZ.png"
IRMASAD = "https://i.imgur.com/Iv9gWTD.png"
PLAY = "https://i.imgur.com/Jcnz4vj.png"
SAIR = "https://i.imgur.com/PISMKLy.png"
FUNDODIA = "https://i.imgur.com/zRGdYRp.gif"
FUNDONOITE = "https://i.imgur.com/2Vff3L0.png"
FOGOLARGO = "https://i.imgur.com/S1AyGFi.png"
FOGOESTREITO = "https://i.imgur.com/N93X5s1.png"
ROLDANA = "https://i.imgur.com/FvD7tcb.png"
CONFETES = "https://i.imgur.com/SIV1CTm.png"
CORDA="https://i.imgur.com/cUf3qAv.png"
CORDANO= "https://i.imgur.com/qyAtbdK.png"
BILHETE = "https://i.imgur.com/p9SteRs.png"
LOGO = "https://i.imgur.com/JflnamW.png"
BOTAO = "https://i.imgur.com/kTocYiF.png"
STYLE ["width"] = 1320
STYLE ["height"] = "600px"
# Musica("https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3")
#INICIO DO JOGO
class gameInicio:
    def __init__(self):
        
        gameInicio = Cena(CENAINICIO)
        gameInicio.vai()
        dark= Elemento("",style=dict(width="1345px",height="600px",backgroundColor="black",opacity=0.7),cena=gameInicio)
        self.logotipo = Elemento(LOGO, x=370, y=30,w=650,h=400, cena=gameInicio)
        self.play = Elemento(PLAY, x=570, y=470,w=180,h=120, cena=gameInicio, vai = self.mostradia)
        
    
    def mostradia(self,ev=0):
        fake = Cena()
        fake.vai = self.elevador
        dia = Cena(FUNDODIA, direita=fake )
        dia.vai()
        self.bil = Elemento(BILHETE, x=200, y=20,w=900,h=600, cena=dia, vai = self.elevador)
        self.boton = Elemento(BOTAO, x=820, y=470,w=70,h=70, cena=dia, vai = self.elevador)
    
    def toca(self, ev=0):
        self.musica.sound.play()
        self.musA.x= -1200
        self.musB.x= 1200
    
    def pause(self, ev=0):
        self.musica.sound.pause()
        self.musA.x= 1200
        self.musB.x= -1200
    
    def elevador(self, ev=0):
        todos = Cena(FUNDODIA)
        todos.vai()
        self.musica = Musica(TRACK)
        self.musica.sound.pause()
        self.musA = Elemento(SOMA, x=1200, y=500,w=80,h=80, cena=todos, vai=self.toca)
        self.musB = Elemento(SOMB, x=-1200, y=500,w=80,h=80, cena=todos, vai=self.pause)
        
        self.predio = Elemento(PREDIO, x=350, y=180,w=600,h=300, cena=todos, vai=self.sobe_desce)
        self.girl = Elemento(IRMASAD, x=550, y=80,w=200,h=130, cena=todos, vai=self.sobe_desce)
        self.boy = Elemento(MENINOSAD, x=600, y=60,w=250,h=150, cena=todos, vai=self.sobe_desce)
        self.linhaA = Elemento(CORDA, x=520, y=-12,w=270,h=150, cena=todos, vai=self.sobe_desce)
        
        #Roldana, corda e cesta       
        self.linhaB = Elemento(CORDA, x=445, y=80,w=150,h=140, cena=todos, vai=self.sobe_desce)
        self.linhaB.elt.style.transform = "rotate(90deg)"
        self.roldB = Elemento(ROLDANA, x=340, y=33,w=380,h=180, cena=todos, vai=self.sobe_desce)
        self.cestinhaA = Elemento(CESTA, x=420, y=220,w=180,h=120, cena=todos, vai=self.sobe_desce)
       
        #Roldana, corda e cesta        
        self.linhaC = Elemento(CORDA, x=660, y=130,w=280,h=180, cena=todos, vai=self.sobe_desce)
        self.linhaC.elt.style.transform = "rotate(90deg)"
        self.roldA = Elemento(ROLDANA, x=580, y=33,w=380,h=180, cena=todos, vai=self.sobe_desce)
        self.cestinhaB = Elemento(CESTA, x=700, y=350,w=180,h=120, cena=todos, vai=self.sobe_desce)
        
        
        self._sobe_desce = self._desce
        self._entra_sai = self._entra
        self._doggie_sobe_desce = lambda *_:None
        self._doggie_desce = lambda *_:None
        self._doggie_sobe = lambda *_:None
        self.na_cesta = "nada"
         
        self.doggie = Elemento(DOG, x=540, y=130,w=100,h=70, cena=todos, vai=self.entra_sai)         
        #INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=0)
    
    #SIDE A               
    def sobe_desce(self, *_):#*_ serve para criar estados para poder detrminar quando está dentro, fora, sobe, desce
        self.cestinhaA.y = 400
        self._sobe_desce()
        
    def _desce(self, *_):
        self._sobe_desce = self._sobe
        self._doggie_desce()
        self.cestinhaA.elt.style.top = 400
        #INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _sobe(self, *_):
        self._sobe_desce = self._desce
        self._doggie_sobe()
        self.cestinhaA.elt.style.top = 220
        #INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="sobe", ponto=0, valor=0, _level=1)
        
    def entra_sai(self, *_):
        self._entra_sai()
        
    def _move_doggie(self, tanto):
        self.doggie.elt.style.top = tanto
        
    def _entra(self, *_): #_ serve para
        self._entra_sai= self._sai
        self._doggie_sobe = lambda:self._move_doggie(100)
        self._doggie_desce = lambda:self._move_doggie(400)
        self.na_cesta="doggie"
        self.doggie.elt.style.left = 510
        #INVENTARIO.score(casa="doggie", carta=self.na_cesta, move="entra", ponto=0, valor=0, _level=1)
        
    def _sai(self, *_):
        self._entra_sai= self._entra
        self._doggie_sobe = lambda:None
        self._doggie_desce = lambda:None
        self.na_cesta="nada"
        self.doggie.elt.style.left = 350
        #INVENTARIO.score(casa="doggie", carta=self.na_cesta, move="sai", ponto=0, valor=0, _level=1)
    
    #SIDE B 
    def sobe_desce(self, *_):#*_ serve para criar estados para poder detrminar quando está dentro, fora, sobe, desce
        self.cestinhaB.y = 400
        self._sobe_desce()
        
    def _desce(self, *_):
        self._sobe_desce = self._sobe
        self._doggie_desce()
        self.cestinhaB.elt.style.top = 400
        #INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _sobe(self, *_):
        self._sobe_desce = self._desce
        self._doggie_sobe()
        self.cestinhaB.elt.style.top = 220
        #INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="sobe", ponto=0, valor=0, _level=1)
        
    def entra_sai(self, *_):
        self._entra_sai()
        
    def _move_doggie(self, tanto):
        self.doggie.elt.style.top = tanto
        
    def _entra(self, *_): #_ serve para
        self._entra_sai= self._sai
        self._doggie_sobe = lambda:self._move_doggie(100)
        self._doggie_desce = lambda:self._move_doggie(400)
        self.na_cesta="doggie"
        self.doggie.elt.style.left = 510
        #INVENTARIO.score(casa="doggie", carta=self.na_cesta, move="entra", ponto=0, valor=0, _level=1)
        
    def _sai(self, *_):
        self._entra_sai= self._entra
        self._doggie_sobe = lambda:None
        self._doggie_desce = lambda:None
        self.na_cesta="nada"
        self.doggie.elt.style.left = 350
    
gameInicio()


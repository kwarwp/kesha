# kesha.grace.main.py
from _spy.vitollino.main import Cena, Texto, Elemento

linkBackdropcena = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkmarilyn = "https://activufrj.nce.ufrj.br/file/pedropeclat/WhatsApp_Image_2018-05-22_at_11.54.54.jpeg?disp=inline"


def Defumado():
    galaxia = Cena(img = linkBackdropcena)
    marilyn = Elemento(img = linkmarilyn,tit = "marilyn")
    marilyn.entra(galaxia)
    txtmarilyn = Texto(galaxia,"Ola, eu sou a ideia do bem e do mal.Esse e um jogo de escolhas, sobre a breve historia da humanidade.Para prosseguir, clique no universo.")
    marilyn.vai=txtmarilyn.vai
    galaxia.vai()
    
Defumado()
    
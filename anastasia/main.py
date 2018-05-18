from _spy.vitollino.main import Cena,Elemento,STYLE

STYLE["width"]=700

gatoecachorro = "https://s1.static.brasilescola.uol.com.br/artigos/Ra%C3%A7as-de-cachorros.jpg?i=https://brasilescola.uol.com.br/upload/e/Ra%C3%A7as-de-cachorros.jpg"
rato = "https://vignette.wikia.nocookie.net/webarebears/images/3/3a/Hamster_png.png"

def historia():
   cena1 = Cena(img=gatoecachorro)
   rato1 = Elemento(img=rato, txt="RATO",style=dict(top=100,left=100,width=200))
   SOS= Texto("voce")
   input=("Cachorro fala: Vou comer você!)
   rato1.entra(cena1)
   rato1.vai=SOS.vai
   cena1.vai()

    
historia()

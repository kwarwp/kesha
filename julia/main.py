"""
#mary_shaw.roxanne.main.py
"""
   # Tesouro Inca
"""
__author__ = "Carlo"

#1º MOMENTO
class JogoTesouroInca:
    # Representa o Jogo principal
    def inicia(self):
        # Inicia a construção do Jogo 
        self.cena_do_templo = "Templo do tesouro Inca"
        print("Descrição:", self.cena_do_templo)


if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoTesouroInca()
    
2º MOMENTO

# mary_shaw.roxanne.main.py
from adda.main import JogoTesouroInca as JogoMarilia
"""
    #Tesouro Inca
"""
class JogoTesouroInca:
    # Representa o Jogo principal
    def inicia(self):
        # Inicia a construção do Jogo 
        #self.cena_do_templo = "Templo do tesouro Inca"
        #print("Descrição:", self.cena_do_templo)
        self.cena_do_templo = "Templo perdido do tesouro Inca"
        print("Descrição:", self.cena_do_templo, __name__)


if __name__ == "__main__":
    jogo = JogoTesouroInca()
    #outro_jogo = JogoTesouroInca() 
    outro_jogo = JogoMarilia()
    jogo.inicia()
    outro_jogo.inicia() 
    
3º MOMENTO
"""
# mary_shaw.roxanne.main.py
#from adda.main import JogoTesouroInca as JogoMarilia
# from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"

__author__ = "Carlo"


class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena"""
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)

    def inicia(self):
        """ Inicia a construção do Jogo """
        #self.cena_do_templo = "Templo perdido do tesouro Inca"
        #print("Descrição:", self.cena_do_templo, __name__)
        #pass
        self.cena_do_templo.vai()

if __name__ == "__main__":
    jogo = JogoTesouroInca()
    #outro_jogo = JogoMarilia()
    jogo.inicia()
    #outro_jogo.inicia() 
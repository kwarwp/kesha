# kesha.sarah.main.py
# mary_shaw.samantha.main.py

"""
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
"""
from random import randint
__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"
__version__ = "19.11.06"

class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara?
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        input(f"Você coloca {quantidade} tesouro na mochila ")
        self.mochila += quantidade
        input(f"Você fica com {self.mochila} tesouros na mochila ")
        camara.entra(self)
                    
    def sai(self):
        """ sai do templo """
        self.cabana, self.mochila = self.mochila, 0
        input(f"Você sai do templo e guarda {self.cabana} tesouros na cabana!")


class Camara:
    """
    Uma camara do templo
    O explorador usa o método entra para ter acesso aos tesouros
    """
    def __init__(self):
        self.quantidade = 3
        #self.explorador = explorador
        
    def entra(self, explorador):
        """ entra em uma câmara"""
        input("Você entra em uma câmara com tesouros!")
        if input("Continua?").lower() == "s":
            if self.quantidade:
                self.quantidade -= 1        
                explorador.pega(randint(1, 4), self)
            else:
                input("Não havia mais tesouros!")
                explorador.sai()
        else:
            self.sai()
        


class TemploInca:
    """
    O jogo do Templo Inca
    O jogo incia quando se chama o inicia
    """
    def __init__(self):
        self.explorador = Explorador()
        self.camara = Camara()
        
    def inicia(self):
        """ inicia a exploração """
        input("Uma expedição para coletar os tesouros do Templo Inca")
        self.camara.entra(self.explorador)
        
        
    


if __name__ == "__main__":
    TemploInca().inicia()


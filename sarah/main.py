# kesha.sarah.main.py
# mary_shaw.samantha.main.py

"""
proposito do jupyter acompanhar o processamento de um dado
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
 19.11.06b - usa defaultdict na camara também
 19.11.06a - usa defaultdict como uma forma de switch
 19.11.06 - troca print por input
"""
from random import randint
from collections import defaultdict #o defaultdict se vc der uma chave que não existe ele vai dar um valor que será especificado
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
        self.mochila += quantidade
        input(f"Você coloca {quantidade} na mochila e fica com {self.mochila} tesouros na mochila ")
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
        self.decide_entrar = defaultdict(lambda: self.entra) #a sintaxe do defaultdict exige o lambda
        self.decide_entrar["s"] = self.entra #qualquer outra desição ele sai
        
    def entra(self, explorador):#referência efemera só dura enquanto está executando
        """ entra em uma câmara"""
        #input("Você entra em uma câmara com tesouros!")
        entrando= input("Você entra em uma câmara com tesouros!. Vai entrar (s/n)?")
        self.decide_entrar[entrando]()
        """
        if input("Continua?").lower() == "s":
        """
            if self.quantidade:
                self.quantidade -= 1        
                explorador.pega(randint(1, 4), self)
            else:
                input("Não havia mais tesouros!")
                explorador.sai()
        """
        else:
            explorador.sai()
        """

class TemploInca:
    """
    O jogo do Templo Inca
    O jogo incia quando se chama o inicia
    """
    def __init__(self):
        self.explorador = Explorador()
        self.camara = Camara()
        self.decide = defaultdict(lambda: self.desiste) #a sintaxe do defaultdict exige o lambda
        self.decide["s"] = self.encara #qualquer outra desição ele sai
        """
        lambda adia a execução até execute o que esta depois do :
        self.decide = defaultdict(lambda: input(self.desiste) #a sintaxe do defaultdict exige o lambda
        self.decide["s"] = self.encara #qualquer outra desição ele sai
        
        """
    def inicia(self):
        """ inicia a exploração """
        o_que_decidiu =input("Uma expedição para saquear os tesouros do Templo Inca. Vai encarar (s/n)?")
        self.decide[o_que_decidiu]() #esta linha já é o swhith
        
        """
        if encara == "s":
            self.camara.entra(self.explorador)
        else:
            input("sabia decisão, vamos evitar este templo macabro!")
        """

    def encara(self):
        """ decide iniciar a exploração"""
        self.camara.entra(self.explorador)
    
    def desiste(self):
        """ desiste da exploração"""
        input("sabia decisão, vamos evitar este templo macabro!")
    
          
        
if __name__ == "__main__":
    TemploInca().inicia()


# kesha.meredith.main.py

# margaret.danae.main.py
""" Tesouro Inca - versão texto
Uma aventura de exploração

v 19.11.05h - o jogador foge se encontra dois perigos do mesmo tipo
v 19.11.05g - o jogador foge se encontra dois perigos quaisquer
v 19.11.05f - alterna aleatoriamente entre tesouros e perigos
"""
__author__ = "Carlo Oliveira <carlo at ufrj br>"
__version__ = "19.11.05h"
from random import randint, choice, shuffle

#criar uma classe baralho para:
#geranciar a consturção de um baralho vai introduzir um mix correto de cartas perigo e tesouro
#temos 3 tipos de carta, perigo, tesouro e vamos criar uma carta artefato
#1º misturar as cartas
class Baralho:
"""
"""
    def __init__(self):
        self.baralho = [] #lugar para colocar todas as cartas aqui []
        #cria os perigos
        perigos = ["aranha", "fogo", "mumia", "cobra", "desabamento"]*5
        self.perigos = {tipo :0 for tipo in self.tipos} #dict compreension ele já sabe o que colocar no perigo
        for perigo in perigos:
            self.baralho.append(CamaraPerigosa(baralho=self, tipo=perigo))
    def quantos_perigos:
        

class CamaraPerigosa:
    """ Uma camara contendo um perigos mortais. 
    O jogador entra nela quando se invoca o método vai
    """
    def __init__(self, baralho, tipo):
        self.camara = "Você entrou numa câmara com {}."
        self.perigos = {tipo :0 for tipo in self.tipos}
        self.baralho = None
        self.outra = outra
        
    def sai(self):
        per_m = self.perigo_mortal
        quantos = self.perigos[per_m] if per_m != None else 0
        per_m = per_m if per_m != None else "perigo"
        input(f"Você sai do templo mas encontrou {quantos} {per_m}s")

    def vai(self):
        continua = " Segue para outra câmara? (s/N)"
        tipo_do_perigo = self.tipos[randint(0,4)]
        if input(self.camara.format(tipo_do_perigo)+continua) == "s":
            self.perigos[tipo_do_perigo] = self.perigos[tipo_do_perigo] + 1
            if self.perigos[tipo_do_perigo] > 1 :
                self.perigo_mortal = tipo_do_perigo
                input("Você foge assustado para a entrada do templo")
                self.sai()
                self.outra.perde()
                return self.perigos
            
            if randint(0,9) > 3:
                return self.outra.vai()
            else:
                return self.vai()
        else:
            input("Você volta para a entrada do templo")
            self.sai()
            self.outra.sai()
            return self.perigos

class CamaraSecreta:
    """ Uma camara contendo um conteúdo misterioso. 
    O jogador entra nela quando se invoca o método vai
    """
    def __init__(self, outra):
        self.camara = "Você entrou numa câmara com {} tesouros."
        self.tesouros = 0
        self.tesouro_aqui (0,17))
        shuffle(self.tesouro_aqui)
        self.outra = outra
        
    def perde(self):
        input(f"Você fugiu do templo e perdeu {self.tesouros} tesouros:")
        
    def sai(self):
        input(f"Você sai do templo com {self.tesouros} tesouros:")
        #cada camara está somente com um tesouro 
        #encontrar uma maneira de botar mais de um teosuro na camara 
        # avisar para o jogador quantos tesourose ele pegou outra melhoria 
        #dizer quantos tesouros totais ele tem na mochila
        #modificar o codigo para te rmais de um tesouro na camara de touro, 
        # avisar quantos ele tem na mochila
    def vai(self):
        continua = " Segue para outra câmara? (s/N)"
        tesouros_aqui = self.tesouros_aqui.pop()
        #tesouro_aqui = randint(1,17) #criou um numero aleatorio de tesouro
        if input(self.camara.format(tesouro_aqui) +continua)+continua) == "s": #deixou de usar a proxima linha para usar esta
        #agora ele consegue usar o format e mostrar a quantidade de tesouros
        #ele teve que mudar o self.camara utilizanod {}
        #if input(self.camara+continua) == "s":
            self.tesouros = self.tesouros + 1 #tesouro é a mochila do cara
            if randint(0,9) > 6:
            #de 0 a 9 é pra enfiar uma camara de perigo
                return self.outra.vai()
            else:
                return self.vai()

        else:
            input("Você volta para a entrada do templo")
            self.sai()
            self.outra.sai()
            return self.tesouros
            input(f"Por enquanto você tem {self.tesouros} tesouros:") #mostra quantidade de tesouros

class JogoDoTesouroInca:
    """ O jogo do tesouro inca. 
    O jogo começa quando se invoca o método vai
    """
    def __init__(self):
        self.templo = "Você está diante de um templo Inca."
        tesouro = CamaraSecreta(None)
        self.camara = CamaraPerigosa(tesouro)
        tesouro.outra = self.camara
        
    def vai(self):
        continua = " Você vai entrar? (s/N)"
        if input(self.templo+continua) == "s":
            input("Você se embrenha no templo, e explora")
            muitos = self.camara.vai()
        else:
            input("Você sabiamente desiste desta loucura")


if __name__ == "__main__":
    tesouro = JogoDoTesouroInca()
    tesouro.vai()
# kesha.alexa.main.py
# kesha.amanda.main.py
#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Vittolino Copyright 2011-2017 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__, `GPL <http://is.gd/3Udt>`__.
# Vittolino é um software livre, você pode redistribuí-lo e/ou modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF), na versão 2 da Licença.
# Este programa é distribuído na esperança de que possa ser útil, mas SEM NENHUMA GARANTIA, sem uma garantia implícita 
# de ADEQUAÇÃO a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a Licença Pública Geral GNU para maiores detalhes.
# Você deve ter recebido uma cópia da Licença Pública Geral GNU junto com este programa, se não, 
#veja em <http://www.gnu.org/licenses/>
"""
Gerador de labirintos e jogos tipo 'novel  https://github.com/carlotolla/vitollino
"""
from _spy.vitollino.main import STYLE, INVENTARIO, Cena, Elemento, Texto, JOGO
from browser import window, html, document
document["pydiv"].style.width="800px"
document["pydiv"].style.minHeight="600px"
Cena._cria_divs = lambda *_: None
STYLE['width'] = 800
STYLE['min-height'] = "600px"
INVENTARIO.elt.style.width = 800
ACTIV = "http://activufrj.nce.ufrj.br/file/GamesInteligentesII/Cena_{}_Quadro_{}_Momento_{}.png"
QUADROS = [ # cena [ quadro(momento) ]
        [ list(range(1,3)), list(range(1,9)), [1] ],
        [ [1], list(range(1,3)) ],
        [ list(range(1,3)) ]
    ]
MOMENTOS = [
    [i+1] + list((quadro+1, momento))
        for i in range(0, len(QUADROS),1)
        for quadro, quadros in enumerate(QUADROS[i]) 
        for momento in quadros 
    ]
LEGENDAS = "vestiário abriu_o_armário o_asseio acionou_a_pia molhando_as_mãos usando_sabão" \
           " as_bactérias enxaguando secando descontaminando saindo teste".split()

class Config:

class PreviaDoMomento:
    def __init__(self, jogo, destino):
        self.destino, self.jogo = destino, jogo
        self._destino = getattr(JOGO.c, destino)
        self.nome = self._destino.nome
    def vai(self, *_, **__):
        self.jogo.configura_momentos(self.destino)
        self._destino.vai(*_, **__)

class JogoMarcela:
    def __init__(self, legendas=LEGENDAS, momentos=MOMENTOS):
        self.quadros = momentos
        telas = {nome: ACTIV.format(cena, quadro, momento) 
            for nome, [cena, quadro, momento] in zip(legendas, momentos)
        }
        print({te: ur[-18:] for te, ur in telas.items()})
        JOGO.musica("http://activufrj.nce.ufrj.br/file/GamesInteligentesII/Fundo_musical_marcella.mp3?disp=inline")
        self._cria_cenas(telas)
        self._inicia_jogo()

    def configura_momentos(self, cena):
        origem_destino_titulo_texto, com_texto, hot = Config.CONFIGURA[cena]
        origem, destino, titulo, texto = origem_destino_titulo_texto.split("#")
        origem = getattr(JOGO.c, origem)
        debug = False
        #Config.debug = debug

        @JOGO.n.texto(titulo, texto)
        def configura_portal_com_texto(origem_, destino_, hot_spot=hot):
            return origem_.portal(L=destino_, style=hot_spot, debug_=debug)

        def configura_portal_sem_texto(origem_, destino_, hot_spot=hot):
            return origem_.portal(L=destino_, style=hot_spot)
        previo_destino = PreviaDoMomento(self, destino)
        if com_texto:
            portal_decorado = configura_portal_com_texto(origem, previo_destino)
        else:
            portal_decorado = configura_portal_sem_texto(origem, previo_destino)

        if debug:
            self._decorador_do_vai_do_texto(portal_decorado)

        return previo_destino

    @staticmethod
    def _decorador_do_vai_do_texto(port):
        formato_do_texto_no_popup = "dict(left={left}, top={top}, width={width}, height={height})"
        metodo_vai_original = port.texto.vai

        def decorador_do_metodo_vai_do_texto(*a):
            port.texto.txt = formato_do_texto_no_popup.format(
                **{k: v[:-2] for k, v in dict(left=port.elt.style.left, top=port.elt.style.top,
                                              width=port.elt.style.width, height=port.elt.style.minHeight).items()})
            metodo_vai_original(*a)

        port.texto.vai = lambda *a: decorador_do_metodo_vai_do_texto(*a)

    def _inicia_jogo(self):
        self.configura_momentos("origem").vai()

    @staticmethod
    def _cria_cenas(cenas):
        JOGO.c.c(**cenas)


def main(*_):
    JogoMarcela()
main();
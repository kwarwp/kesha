
{'date': 'Tue Sep 04 2018 21:19:14.26 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 202
    Jogo()
  module <module> line 191
    self.reset()
  module <module> line 194
    self.tabuleiro =  Tabuleiro()
  module <module> line 74
    self.inicia_fase()
  module <module> line 78
    [self.cria_tabuleiro(col=3, lin=self.linha, lado=l) for l in self.lado]
  module <module> line 117
    self.casa["esquerda"][nome] = Casa(self, nome=nome, linha=linha_, coluna=coluna_, lado=lado)
  module <module> line 168
    inicio_x_ = inicio_x + offset[lado]
NameError: name 'offset' is not defined
'''},
{'date': 'Tue Sep 04 2018 21:36:30.485 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 14
    BUTTONS = [TENTAR, DESISTO, NAOQUEROJOGAR, TERMINEI, JATERMINEI]
NameError: name 'JATERMINEI' is not defined
'''},
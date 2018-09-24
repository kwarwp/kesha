
{'date': 'Tue Sep 04 2018 21:07:31.235 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
    cubo2=box(pos=(1, 0, 0), size=(1,1,1) , **bloco)
TypeError: box() got multiple values for argument 'size'
'''},
{'date': 'Tue Sep 04 2018 21:07:47.918 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
    cubo2=box(pos=(1, 0, 0), size=(1,1,1) , **bloco)
TypeError: box() got multiple values for argument 'size'
'''},
{'date': 'Mon Sep 24 2018 15:10:26.937 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  cubos1 = [box(pos = (-0.2, 1.2, 0 + 1.2*x),size(1, 1, 1),**bloco1)for x in range(2)]  # Os da primeira em cima
                                                          ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Mon Sep 24 2018 15:10:59.355 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  cubos1 = [box(pos = (-0.2, 1.2, 0.0 + 1.2*x),size(1, 1, 1),**bloco1)for x in range(2)]  # Os da primeira em cima
                                                            ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Mon Sep 24 2018 15:11:29.888 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  cubos1 = [box(pos = (-0.2, 1.2, 1.2*x),size(1, 1, 1),**bloco1)for x in range(2)]  # Os da primeira em cima
                                                      ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Mon Sep 24 2018 15:12:51.401 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  cubos1 = [box(pos = (-0.2, 1.2, (1.2)*x),size(1, 1, 1),**bloco1)for x in range(2)]  # Os da primeira em cima
                                                        ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Mon Sep 24 2018 15:13:18.263 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  cubos1 = [box(pos = (-0.2, 1.2, 0.0 + (1.2)*x),size(1, 1, 1),**bloco1)for x in range(2)]  # Os da primeira em cima
                                                              ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Mon Sep 24 2018 15:14:33.810 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  cubos1 = [box(pos = (-0.2, 1.2,(1.2)*x + 0),size(1, 1, 1),**bloco1)for x in range(2)]  # Os da primeira em cima
                                                           ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Mon Sep 24 2018 15:15:59.767 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  cubos1 = [box(pos = (-0.2, 1.2,x*(1.2)),size(1, 1, 1),**bloco1)for x in range(2)]  # Os da primeira em cima
                                                       ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Mon Sep 24 2018 15:16:30.501 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  cubos1 = [box(pos = (-0.2, 1.2, x * (1.2)),size(1, 1, 1),**bloco1)for x in range(2)]  # Os da primeira em cima
                                                          ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Mon Sep 24 2018 15:17:00.693 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 39
  cubos2 = [box(pos = (-1.4 + (1.2)*y, 0, 0),size(1, 1, 1),**bloco)for y in range(3)] #Os da segunda linha
                                                          ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Mon Sep 24 2018 15:20:18.228 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 37
  cubos2 = [box(pos=(y * (1.2) -1.4, 0, 0),size(1, 1, 1),**bloco)for y in range(3)] #Os da segunda linha
                                                        ^
SyntaxError: non-keyword arg after keyword arg
'''},
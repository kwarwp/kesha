
{'date': 'Mon Sep 24 2018 17:31:03.431 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 14
  list1 = [(0,1.2),(0,-1.2),(-1.2,0),(1.2,0)
                                              ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:31:30.84 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 14
  list1 = [(0,1.2),(0,-1.2),(-1.2,0),(1.2,0)
                                              ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:31:52.980 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 15
  cubos1 = [box(pos=(x[0],x[1], 0), size=(1, 1, 1), **bloco) for x in list 1] 
                                                                            ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:32:30.234 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 15
  cubos1 = [box(pos=(x[0],x[1], 0), size=(1, 1, 1), **bloco) for x in enumerate(list 1)] 
                                                                                      ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:33:01.494 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 15
  cubos1 = [box(pos=(x[0], x[1], 0), size=(1, 1, 1), **bloco) for x in enumerate(list 1)] 
                                                                                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:43:28.54 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 18
  sphere =[(pos=(x[0], x[1], 0), size=(1, 1, 1), **bloco1) for x in list2] 
                                                  ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:48:50.18 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  ball = sphere[(pos=x[0], x[1], 0),, radius=0.3, **bloco1) for x in list2]
                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:49:54.218 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 18
  ball = sphere[(pos=x[0], x[1], 0), radius=0.3, **bloco1) for x in list2]
                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:53:00.429 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 18
  ball = sphere[(pos=x[0], x[1], 0), radius=0.3, **bloco1) for x in list2]
                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:53:42.777 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 18
  ball = sphere[(pos=x[0], x[1], 0), radius=0.3, **bloco1) for y in list1]
                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 24 2018 17:54:32.832 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '__class__' of undefined>
'''},
{'date': 'Mon Sep 24 2018 17:56:13.300 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '__class__' of undefined>
'''},
{'date': 'Mon Sep 24 2018 17:57:06.530 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '__class__' of undefined>
'''},
{'date': 'Mon Sep 24 2018 17:57:13.583 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '__class__' of undefined>
'''},
{'date': 'Mon Sep 24 2018 17:57:15.816 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read property '__class__' of undefined>
'''},
{'date': 'Mon Sep 24 2018 18:13:22.724 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 30
    rate(1/dt)
TypeError: rate() missing 1 positional argument: ['func']
'''},
{'date': 'Mon Sep 24 2018 18:15:32.505 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 24
    rate(1/dt)
TypeError: rate() missing 1 positional argument: ['func']
'''},
{'date': 'Mon Sep 24 2018 18:16:12.438 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 24
    rate(1/dt)
TypeError: rate() missing 1 positional argument: ['func']
'''},
{'date': 'Mon Sep 24 2018 18:17:53.80 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 24
    rate(1/dt)
TypeError: rate() missing 1 positional argument: ['func']
'''},
{'date': 'Mon Sep 24 2018 18:19:05.291 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 24
    rate(1/dt)
TypeError: rate() missing 1 positional argument: ['func']
'''},
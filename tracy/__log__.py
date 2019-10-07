
{'date': 'Mon Oct 07 2019 14:14:01.810 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 77
  class Perigo:
  ^
IndentationError: expected an indented block
'''},
{'date': 'Mon Oct 07 2019 14:14:54.453 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 5
    from ruzwana.main import DI as RDI
  module ruzwana.main line 24
    rate(1/dt)
TypeError: rate() missing 1 positional argument: ['func']
'''},
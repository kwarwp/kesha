
{'date': 'Mon Feb 04 2019 14:46:15.210 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  from meredith import 
                       ^
SyntaxError: trailing comma not allowed without surrounding parentheses
'''},
{'date': 'Tue Nov 26 2019 10:11:33.586 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 54
    class CamaraSecreta:
  module <module> line 89
    input(f"Por enquanto você tem {self.tesouros} tesouros:") #mostra quantidade de tesouros
  module <module> line 1
    (self.tesouros)
AttributeError: 'GUI' object has no attribute 'tesouros'
'''},
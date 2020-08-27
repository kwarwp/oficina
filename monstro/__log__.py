
{'date': 'Thu Aug 27 2020 18:41:35.499 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 177
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 17
    monstro = Monstro()
  module <module> line 11
    self.monstro = self.jogo.a(UM_MONSTRO, x=100, y=200, cena = self.cenario)
NameError: name 'UM_MONSTRO' is not defined
'''},
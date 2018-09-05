# kesha.libby.main.py
from browser import doc, html
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.black #"rgba(0, 0, 200, 0.5)"
scene.width = 1200
scene.height = 800
bloco = dict(color=color.blue)
bloco1 = dict(color=color.white)

cubo1=box(pos=(1, -1.2, 0), size=(1,1,1) , **bloco)
cubo2=box(pos=(1, 0, 0), size=(1,1,1) , **bloco)
cubo3=box(pos=(-0.2, 0, 0), size=(1,1,1) , **bloco)
cubo4=box(pos=(-0.2, 1.2, 0), size=(1,1,1) , **bloco)
cubo5=box(pos=(-0.2, 1.2, 1.2), size=(1,1,1) , **bloco)
cubo5=box(pos=(-0.2, 0, -1.2), size=(1,1,1) , **bloco)
cubo6=box(pos=(-1.4, 0, 0), size=(1,1,1) , **bloco1)
cubo7=box(pos=(0, -2.4, 1.2), size=(1,1,1) , **bloco1)
cubo8=box(pos=(-1.2, -2.4, -1.2), size=(1,1,1) , **bloco1)
cubo9=box(pos=(-1.2, -3.6, -1.2), size=(1,1,1) , **bloco1)


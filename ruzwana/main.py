# kesha.ruzwana.main.py
# kesha.libby.main.py
from browser import doc, html
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.black #"rgba(0, 0, 200, 0.5)"
scene.width = 1200
scene.height = 800
bloco = dict(color=color.blue, opacity=0.3)
bloco1 = dict(color=color.white)

d = 1
list1 = [(0,1.2 + d),(0,-1.2 - d),(-1.2 - d,0),(1.2 + d,0)]
cubos1 = [box(pos=(x[0], x[1], 0), size=(1, 1, 1), **bloco) for x in list1] 
list2 = [(0,1.2 + d),(0,-1.2 - d),(-1.2 - d,0),(1.2 + d,0)]
ball = sphere[(pos=x[0], x[1], 0), radius=0.3, **bloco1) for x in list2]







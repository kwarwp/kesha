# kesha.libby.main.py
from browser import doc, html
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.black #"rgba(0, 0, 200, 0.5)"
scene.width = 800
scene.height = 600
silv = dict(color=color.blue)

simetria1=box(pos=(3.2, 0, 0), size=(1,1,1) , **silv)
simetria2=box(pos=(0.8, 3.6, 0), size=(1,1,1) , **silv)
simetria = [box(pos=(2, x*(1.2), 0), size=(1,1,1), **silv) for x in range(4)]

#Q1 = [simetria]+simetria1+simetria2
#sup = compound(Q1, pos=(3,1.75,0))
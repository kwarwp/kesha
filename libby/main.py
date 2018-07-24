# kesha.libby.main.py
from browser import doc, html
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.black #"rgba(0, 0, 200, 0.5)"
scene.width = 600
scene.height = 600
silv = dict(color=color.blue)

simetria1=box(pos=(1.7, 0, 0), size=(0.4,0.4,0.4) , color=color.blue)
simetria2=box(pos=(4, 0, 1.5), size=(0.4,0.4,0.4) , color=color.blue)
simetria = [box(pos=(x/2+2.2, 0.15, 0.9), size=(0.4,0.4,0.4), **silv) for x in range(4)]

Q1 = [simetria]+simetria1+simetria2

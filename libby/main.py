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


simetria1=box(pos=(2, 0, 0), size=(2,1,2) , color=color.blue)
simetria2=box(pos=(2, 0, 0), size=(2,1,2) , color=color.blue)
simetria = [box(pos=(x/2+2.2, 0.15, 0.9), size=(0.3,0.3,0.3), **silv) for x in range(4)]

Q1 = [simetria]+simetria1+simetria2
#sup = compound(pts, pos=(-1,0,0))
"""
def sail():
    rate(2, sail)
    sup.pos += vec(0.2,0,0)
    sup.rotate(angle=0.02,
           axis=
"""
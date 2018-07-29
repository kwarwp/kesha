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

simetria1=box(pos=(4.2, -2, 0), size=(1,1,1) , **silv)
simetria2=box(pos=(1.8, 1.6, 0), size=(1,1,1) , **silv)
simetria = [box(pos=(3, x*(1.2)-2, 0), size=(1,1,1), **silv) for x in range(4)]

pts = [simetria1, simetria2]+simetria
sup = compound(pts, pos=(2,0,0), axis=vec(0,0,1) )

#def sail():
    #rate(2, sail)
    #sup.pos += vec(0.2,0,0)
#   sup.rotate(angle=0.02, axis=vec(1,1,0))

#sail()
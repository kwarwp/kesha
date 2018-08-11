# kesha.parisa.main.py
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
bloco = dict(color=color.blue)

simetria1=box(pos=(4.2, -2, 0), size=(1,1,1) , **bloco)
simetria2=box(pos=(1.8, 1.6, 0), size=(1,1,1) , **bloco)
simetria = [box(pos=(3, x*(1.2)-2, 0), size=(1,1,1), **bloco) for x in range(4)]

pts = [simetria1, simetria2]+simetria
sup = compound(pts, pos=vec(2,0,0), axis=vec(4,0,-1))
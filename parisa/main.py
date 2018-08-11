# kesha.parisa.main.py
from browser import doc, html
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.black #"rgba(0, 0, 200, 0.5)"
scene.width = 1200
scene.height = 600
bloco = dict(color=color.blue)


#simetria1=box(pos=(4.2, -2, 0), size=(1,1,1) , **bloco)
#simetria2=box(pos=(1.8, 1.6, 0), size=(1,1,1) , **bloco)
#simetria = [box(pos=(3, x*(1.2)-2, 0), size=(1,1,1), **bloco) for x in range(4)]

#pts = [simetria1, simetria2]+simetria
#sup = compound(pts, pos=vec(2,0,0), axis=vec(4,0,-1))

area1 = box(pos=(-5,0,0), size=(2,6,0.2), color=color.blue)
area2= box(pos=(-3,0,0), size=(2,2,0.2), color=color.yellow)
area3= box(pos=(0,0,0), size=(4,2,0.2), color=color.purple)
area4= box(pos=(3,1,0), size=(2,4,0.2), color=color.white)
area5= box(pos=(-2,2,0), size=(4,2,0.2), color=color.green)
area6= box(pos=(1,2,0), size=(2,2,0.2), color=color.red)
area7= box(pos=(1,-1.5,0), size=(2,1,0.2), color=color.orange)
area8= box(pos=(1,-2.5,0), size=(2,1,0.2), color=color.blue)
area9= box(pos=(4,-2,0), size=(4,2,0.2),color=color.purple)

parede_area1a= box(pos=(-5,-2.9,1.35), size=(2,0.2,2.5), color=color.white)
parede_area1b= box(pos=(-5.9,0,1.35), size=(0.2,6,2.5), color=color.white)

# kesha.parisa.main.py
from browser import doc, html
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.black 
scene.width = 1200
scene.height = 600

#t1 = text(text='MUSEU DA GEODIVERSIDADE', pos=(-5,3,0), depth=0.5, color=color.yellow)

area1 = box(pos=(-5,0,0), size=(2,6,0.2), color=color.blue)
area2= box(pos=(-3,0,0), size=(2,2,0.2), color=color.yellow)
area3= box(pos=(0,0,0), size=(4,2,0.2), color=color.purple)
area4= box(pos=(3,1,0), size=(2,4,0.2), color=color.white)
area5= box(pos=(-2,2,0), size=(4,2,0.2), color=color.green)
area6= box(pos=(1,2,0), size=(2,2,0.2), color=color.red)
area7= box(pos=(1,-1.5,0), size=(2,1,0.2), color=color.orange)
area8= box(pos=(1,-2.5,0), size=(2,1,0.2), color=color.grey)
area9= box(pos=(4,-2,0), size=(4, 2,0.2), color=color.blue))

parede_a= box(pos=(-5,-2.9,1.35), size=(2,0.2,2.5), color=color.white)
parede_b= box(pos=(-5.9,0,1.35), size=(0.2,6,2.5), color=color.white)
parede_c= box(pos=(-1,2.9,1.35), size=(10,0.2,2.5), color=color.white)
parede_d= box(pos=(-4.1,-1.9,1.35), size=(0.2,2.2,2.5), color=color.white, opacity=0.3)
parede_e= box(pos=(-4.1,1.9,1.35), size=(0.2,2.2,2.5), color=color.white, opacity=0.3)
parede_f= box(pos=(3.9,1,1.35), size=(0.2,4,2.5), color=color.white)
parede_g= box(pos=(-2,-0.9,1.35), size=(4,0.2,2.5), color=color.white)
parede_h= box(pos=(2.9,-2.9,1.35), size=(6,0.2,2.5), color=color.white, opacity=0.3)
parede_i= box(pos=(0,-1.8,1.35), size=(0.2,2,2.5), color=color.white)
parede_j= box(pos=(-0.2,1,1.35), size=(4.3,0.1,2.5), color=color.white, opacity=0.5)
parede_k= box(pos=(1.9,0,1.35), size=(0.1,2,2.5), color=color.white)
parede_l= box(pos=(1.9,-2,1.35), size=(0.1,2,2.5), color=color.white, opacity=0.3)
parede_m= box(pos=(1,-2,1.35), size=(2,0.1,2.5), color=color.white, opacity=0.3)

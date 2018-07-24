# kesha.libby.main.py
# ada.parisa.main.py
from browser import doc, html
#doc["glowscript"] <= html.H1('XXXXXXXXX -------------- XXXXXXXXXXX')
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.black #"rgba(0, 0, 200, 0.5)"
scene.width = 600
scene.height = 600
silv = dict(color=color.blue, opacity=0.4)
hull = dict(color=color.yellow)
#s = shapes.rectangle(width=10, height=6)
#h1=box(pos=(1.5, -0.5, 0),size=(1,0.1,0.5), axis=(0,1,0), color=color.blue)
"""
#h2=sphere(pos=(1.5, 0.5, 0),size=(1,0.1,0.5), axis=(0,1,0), color=color.black)
#pyramid(pos=(1, -0.5, 0),size=(0.5,0.1,1), axis=(0,1,0), color=color.black)
# --- hull ---
aft=sphere(pos=(2, 0, 0), size=(1,1,2), color=color.yellow)
fr=sphere(pos=(6, 0, 0), size=(1,1,2), color=color.yellow)
body=cylinder(pos=(2, 0, 0), size=(4,1,2) , color=color.yellow)
# --- cockpit ---
"""
rec0=box(pos=(5, 0.2, 0), size=(1,1,2), **silv)
rec1=box(pos=(6.2, 0.2, 0), size=(1,1,2), **silv)
rec1=box(pos=(6.2, 0.2, 0), size=(1,1,2), **silv)
simetria = [rec0, rec1, rec2]
"""
# --- portholes ---
simetria = [box(pos=(x/2+2.2, 0.15, 0.9), size=(0.3,0.3,0.3), **silv) for x in range(5)]
php = [sphere(pos=(x/2+2.2, 0.15, -0.9), size=(0.3,0.3,0.3), **silv) for x in range(5)]
pts = [h1, h2, aft, fr, body, caft, cfor, cbody]+per+php+phs
sup = compound(pts, pos=(-1,0,0))

def sail():
    rate(2, sail)
    sup.pos += vec(0.2,0,0)
    sup.rotate(angle=0.02,
           axis=

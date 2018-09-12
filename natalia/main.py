# kesha.natalia.main.py
from _spy.vitollino.main import Cena, STYLE, Codigo, Elemento
from _spy.vpython.main import *
from browser import doc
from math import pi
STYLE["width"] = 1200
STYLE["height"] = "650px"
MUSEU = dict(
C0_NORTE = "https://i.imgur.com/PbNGJ2M.jpg",
C0_LESTE = "https://i.imgur.com/6RDjzdv.jpg",
C0_SUL = "https://i.imgur.com/XewJiGv.jpg",
C0_OESTE = "https://i.imgur.com/Rbpudy1.jpg",
C1_NORTE = "https://i.imgur.com/2pdVvqN.jpg",
C1_LESTE = "https://i.imgur.com/3TcuvuA.jpg",
C1_SUL = "https://i.imgur.com/EGLIHmf.jpg",
C1_OESTE = "https://i.imgur.com/648Kqzw.jpg",
C2_NORTE = "https://i.imgur.com/VdzcF4X.jpg",
C2_LESTE = "https://i.imgur.com/w7ORIRk.jpg",
C2_SUL = "https://i.imgur.com/0Nq7Sow.jpg",
C2_OESTE = "https://i.imgur.com/79MV5Ai.jpg",
CA_NORTE = "https://i.imgur.com/usame91.jpg",
CA_LESTE = "https://i.imgur.com/6Sd0NJC.jpg",
CA_SUL = "https://i.imgur.com/Xj8FuaR.jpg",
CA_OESTE = "https://i.imgur.com/o6qbGZw.jpg",
C3_NORTE = "https://i.imgur.com/E3IEnQm.jpg",
C3_LESTE = "https://i.imgur.com/hwq1aEk.jpg",
C3_SUL = "https://i.imgur.com/hwq1aEk.jpg",
C3_OESTE = "https://i.imgur.com/cF5HqYP.jpg",
C4_NORTE = "https://i.imgur.com/thgPVgZ.jpg",
C4_LESTE = "https://i.imgur.com/thgPVgZ.jpg",
C4_SUL = "https://i.imgur.com/0KtKKKd.jpg",
C4_OESTE = "https://i.imgur.com/FT2icyZ.jpg",
C5_NORTE = "https://i.imgur.com/lzWkkM4.jpg",
C5_LESTE =  "https://i.imgur.com/C0vQ6qN.jpg",
C5_SUL = "https://i.imgur.com/YGWcGNI.jpg",
C5_OESTE = "https://i.imgur.com/DVoSsVi.jpg",
C6_NORTE = "https://i.imgur.com/EBtfMb1.jpg",
C6_LESTE = "https://i.imgur.com/DPfoGQi.jpg",
C6_SUL = "https://i.imgur.com/ru8v03c.jpg",
C6_OESTE = "https://i.imgur.com/7nk0WQc.jpg",
CB_NORTE = "https://i.imgur.com/BHq6wqZ.jpg",
CB_LESTE = "https://i.imgur.com/APPNj4C.jpg",
CB_SUL = "https://i.imgur.com/s6pCgnw.jpg",
CB_OESTE = "https://i.imgur.com/IKutZ2E.jpg",
CC_NORTE = "https://i.imgur.com/dHzKv4s.jpg",
CC_LESTE = "https://i.imgur.com/VpZHexT.jpg",
CC_SUL = "https://i.imgur.com/TEePsJw.jpg",
CC_OESTE = "https://i.imgur.com/ZOAEHwy.jpg",
CD_NORTE = "https://i.imgur.com/OQUz4Ea.jpg",
CD_LESTE = "https://i.imgur.com/dtzdhIy.jpg",
CD_SUL = "https://i.imgur.com/BSiJogb.jpg",
CD_OESTE = "https://i.imgur.com/nbnZvuH.jpg",
CE_NORTE = "https://i.imgur.com/aZLRytp.jpg",
CE_LESTE = "https://i.imgur.com/hh8ec7K.jpg",
CE_SUL = "https://i.imgur.com/gs3uvVF.jpg",
CE_OESTE = "https://i.imgur.com/AeJERXr.jpg",
C7_NORTE = "https://i.imgur.com/nbnZvuH.jpg",
C7_LESTE = "https://i.imgur.com/J2a1PPS.jpg",
C7_SUL = "https://i.imgur.com/hh8ec7K.jpg",
C7_OESTE = "https://i.imgur.com/nbnZvuH.jpg",
C8_NORTE = "https://i.imgur.com/GrBqUka.jpg",
C8_LESTE = "https://i.imgur.com/anG0ztT.jpg",
C8_SUL = "https://i.imgur.com/FBS3Yzc.jpg",
C8_OESTE = "https://i.imgur.com/QQlaxLn.jpg",
C9_NORTE = "https://i.imgur.com/YJViqyh.jpg",
C9_LESTE = "https://i.imgur.com/8QcEfJu.jpg",
C9_SUL = "https://i.imgur.com/evAHwNH.jpg",
C9_OESTE = "https://i.imgur.com/SJ5c9tV.jpg")

ROSA = "_NORTE,_LESTE,_SUL,_OESTE".split(",")
IMGS = [[MUSEU["C{:01X}{}".format(sala, rosa)] for rosa in ROSA] for sala in range(15)]

doc['pydiv'].html = ''
_gs = Glow('pydiv')
scene = canvas()
POS=[(-1,0),(0,1),(1,0),(0,-1)]

class Sala3D:
    def __init__(self, img_list, p=(0,0,0)):
        for direcao, parede in enumerate(img_list):
            parede_ = box(pos=(2*POS[direcao][0]+p[0], 0, -2*POS[direcao][1]+p[1]), size=(0.2, 4, 4), texture=dict(file=parede, place=["right"]))
            
            parede_.rotate(angle=direcao*pi/2.0, axis=vec(0,-1,0))

class Sala3Dgrande:
    def __init__(self, img_list, p=(0,0)):
        for direcao, parede in enumerate(img_list):
            parede_ = box(pos=(4*POS[direcao][0]+p[0], 0, -4*POS[direcao][1]+p[1]), size=(0.2, 4, 8), texture=dict(file=parede, place=["right"]))
            
            parede_.rotate(angle=direcao*pi/2.0, axis=vec(0,-1,0))

class Sala3Dlongo:
    def __init__(self, img_list, p=(0,0,0)):
        i = p[2]
        for direcao, parede in enumerate(img_list):
            if i%2 == 0:
                parede_ = box(pos=(4*POS[direcao][0]+p[0], 0, -2*POS[direcao][1]+p[1]), size=(0.2, 4, 4), texture=dict(file=parede, place=["right"]))
            else:    
                parede_ = box(pos=(2*POS[direcao][0]+p[0], 0, -2*POS[direcao][1]+p[1]), size=(0.2, 4, 8), texture=dict(file=parede, place=["right"]))

            parede_.rotate(angle=direcao*pi/2.0, axis=vec(0,-1,0))
            i += 1

class Museu:
    def __init__(self):
        cena = Cena(MUSEU["C9_OESTE"])
        for i, sala in enumerate(IMGS):
            for j, prd in enumerate(sala):
                Elemento(prd, style = dict(left=i*110, top =j*110, width=100, height="80px")).entra(cena)
        cena.vai()
    
# Sala3D(IMG_LIST)    
# Sala3D(IMG_LIST1, p=(4, 0))

#SALA 0
Sala3Dlongo(IMGS[0], p=(6,0,1))
#Sala3D(IMGS[0], p=(8,0))

#SALA 1
Sala3Dgrande(IMGS[1], p=(6,-6.1))
#Sala3D(IMGS[1], p=(4,-8.1))
Sala3D(IMGS[1], p=(4,-12.1))
#Sala3D(IMGS[1], p=(8,-4.1))
#Sala3D(IMGS[1], p=(8,-8.1))
Sala3D(IMGS[1], p=(8,-12.1))

#SALA 9
Sala3D(IMGS[9], p=(0,0))

#SALA 8
Sala3D(IMGS[8], p=(0,-4))

#SALA 2
Sala3D(IMGS[2], p=(0,-8.1))
Sala3D(IMGS[2], p=(0,-12))

#SALA E
Sala3D(IMGS[2], p=(-4,0))
#SALA 7
Sala3D(IMGS[7], p=(-4, -4))
#SALA A
Sala3D(IMGS[0], p=(-4,-8))
Sala3D(IMGS[0], p=(-4,-12))


#SALA D
Sala3D(IMGS[1], p=(-8,-4))
Sala3D(IMGS[1], p=(-8,0))
#SALA 3
Sala3D(IMGS[3], p=(-8,-12))

#SALA  C
Sala3D(IMGS[0], p=(-12,-4))
Sala3D(IMGS[0], p=(-12,0))
Sala3D(IMGS[3], p=(-8,-8))

#SALA 4 longa 2 x 2
#Sala3Dgrande(IMGS[4], p=(-12,-12))
#Sala3Dgrande(IMGS[4], p=(-12,-8))
Sala3Dgrande(IMGS[4], p=(-14,-10))
#Sala3Dgrande(IMGS[4], p=(-16,-8))

#SALA 5 longa 2 x 1
Sala3D(IMGS[5], p=(-16,-4))
Sala3D(IMGS[5], p=(-16,0))

#SALA B longa 2 x 1
Sala3D(IMGS[3], p=(-20,-12))
Sala3D(IMGS[3], p=(-20,-8))

#SALA 6 sala longa 3 x 1
Sala3D(IMGS[6], p=(-20,-4))
Sala3D(IMGS[6], p=(-20,0))
Sala3D(IMGS[6], p=(-20,4))

#Museu()

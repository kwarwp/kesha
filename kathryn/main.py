# kesha.libby.main.py
from browser import doc, html
from _spy.vpython.main import *
doc['pydiv'].html=''
_gs=Glow('pydiv')
scene=canvas()
scene.background= color.black #"rgba(0, 0, 200, 0.5)"
scene.width = 1200
scene.height = 800
bloco = dict(color=color.blue)
bloco1 = dict(color=color.white)







#cubo4=box(pos=(-0.2, 1.2,  0.0), size=(1,1,1) , **bloco)
#cubo5=box(pos=(-0.2, 1.2,  1.2), size=(1,1,1) , **bloco)

#cubo2=box(pos=(1.0,    0,  0.0), size=(1,1,1) , **bloco)
#cubo3=box(pos=(-0.2,   0,  0.0), size=(1,1,1) , **bloco)
#cubo6=box(pos=(-1.4,   0,    0), size=(1,1,1) , **bloco1)

#cubo5=box(pos=(-0.2,   0, -1.2), size=(1,1,1) , **bloco)

#cubo1=box(pos=(1.0, -1.2,  0.0), size=(1,1,1) , **bloco)

#cubo7=box(pos=(-0.2,-2.4,  1.2), size=(1,1,1) , **bloco)

#cubo8=box(pos=(-1.2,-2.4, -1.2), size=(1,1,1) , **bloco1)
#cubo9=box(pos=(-1.2,-3.6, -1.2), size=(1,1,1) , **bloco1)

#cubos1 = [box(pos = (-0.2, 1.2, x * (1.2)),size(1, 1, 1),**bloco1)for x in range(2)]  
cubos1 = [box(pos=(-0.2, 1.2, x * (1.2) - 0), size=(1, 1, 1), **bloco) for x in range(2)] #Os da primeira em cima
cubos2 = [box(pos=(y * (1.2) - 1.4, 0, 0),size=(1, 1, 1),**bloco)for y in range(3)] #Os da segunda linha
cubo = box(pos=(-0.2,   0, -1.2), size=(1,1,1) , **bloco1) #Antigo Cubo 5 na 2 linha
cubo2 = box(pos=(1.0, -1.2, 0.0), size=(1,1,1) , **bloco) #Antigo Cubo 1 na 3 linha
cubo3 = box(pos=(-0.2,-2.4, 1.2), size=(1,1,1) , **bloco) #Antigo Cubo 7 na 4 linha
cubos3 = [box(pos=(-1.2,(-1.2) * z - 2.4, -1.2),size=(1, 1, 1),**bloco1)for z in range(2)]  # Os últimos










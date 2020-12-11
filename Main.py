from Esfera import nPuntosSupEsfera #puntosEsfera
from PuntoInterseccion import pICompleto
from numpy import array
from Rectangulo import estaEnRectangulo
from Pixel import dibujaPixel,cambiaColorFondo
from pygame import Color,quit
from pygame.display import set_mode,update

#esfera
oEsfera=array([0,0,0])
x,y,z=oEsfera
#x=y=z=0
r=180 #esto aumenta considerablemente los calculos 
#psEsfera=nPuntosSupEsfera(r) #puntosEsfera(r,r) #puntos p

"""
#rectangulo
#x=y=0

oRectangulo=array([0,0,0])
x,y,z=oRectangulo
"""

#plano
resRectangulo=array([640,360,0])
resX,resY,resZ=resRectangulo

normal=array([0,0,-1])
dPlano=-360

#camara origen
origen=array([320,180,-720]) #-720

#colores
cBlanco=Color(255, 255, 255, a=255) 
cNegro=Color(0, 0, 0, a=255) 

psIntersecados=[]

for z1 in range(x-r,x+r):
    for y1 in range(y-r,y+r):
        for x1 in range(z-r,z+r):
            if (x1-x)**2+(y1-y)**2+(z1-z)**2==r**2: #==
                p=array([x1,y1,z1])
                x2,y2,z2=pICompleto(normal, p, origen, dPlano)
                p1=[x2,y2,0]

                #if p1 not in psIntersecados: #solo para puntos dentro de esfera
                psIntersecados.append(p1)
                """
                else:
                    print("repe")
                """
            
sc=set_mode(size=[resX, resY])
cambiaColorFondo(sc,cBlanco)

for p in psIntersecados:
    x,y,z=p
    dibujaPixel(sc, round(x), round(y), cNegro)

update()

""" #esto deja el proceso en espera
if input("q para salir\n")=="q":
    quit()

#interseccion
psInterseccion=[]

for p in psEsfera:
    x2,y2,z=p
    x2+=r #traslado esfera
    p=array([x2,y2,z])
    #if estaEnRectangulo(x,x1, y,y1, x2,y2): #proyeccion ortogonal
    psInterseccion.append(pICompleto(normal, p, origen, dPlano))

for p in psInterseccion:
    x2,y2,z=p

    dibujaPixel(sc, round(x2), round(y2), cNegro)
"""




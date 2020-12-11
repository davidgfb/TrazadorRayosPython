#from Esfera import nPuntosSupEsfera
#from Rectangulo import estaEnRectangulo
from PuntoInterseccion import pICompleto
from numpy import array,degrees
from Pixel import dibujaPixel,cambiaColorFondo
from pygame import Color #,quit
from pygame.display import set_mode,update
from math import atan

#esfera
oEsfera=array([0,0,0])
x,y,z=oEsfera
r=18 #180 

#rectangulo
oRectangulo=array([0,0,0])
x,y,z=oRectangulo

"""
TODO:
fijar el plano a la camara 
"""

#plano
resRectangulo=array([640,360,0])
resX,resY,resZ=resRectangulo

normal=array([0,0,-1]) #siempre deberia mirar a camara
dPlano=-36 #-360

#camara origen
origen=array([0,0,-720]) #320,180,-720

#colores
cBlanco=Color(255, 255, 255, a=255) 
cNegro=Color(0, 0, 0, a=255) 

def fov(resX,resY, zPlano,zCam): #debe ser 60º
    return [2*degrees(atan(resX/(2*(zPlano-zCam)))),
            2*degrees(atan(resY/(2*(zPlano-zCam))))]

fovX,fovY=fov(resX,resY, dPlano,origen[2])
print("\nfovX:",fovX,"º\nfovY:",fovY,"º")

psIntersecados=[]

for z1 in range(x-r,x+r):
    for y1 in range(y-r,y+r):
        for x1 in range(z-r,z+r):
            if (x1-x)**2+(y1-y)**2+(z1-z)**2<=r**2: 
                p=array([x1,y1,z1])
                x2,y2,z2=pICompleto(normal, p, origen, dPlano)
                p1=[x2,y2,z1] #z1 es correcto para color

                psIntersecados.append(p1)
                
sc=set_mode(size=[resX, resY])
cambiaColorFondo(sc,cBlanco)

def normalizaZColor(z):
    if z<0:
        z=0
    elif z>255:
        z=255
    return z

for p in psIntersecados:
    x,y,z=p
    gris=normalizaZColor(z)
    dibujaPixel(sc, round(x), round(y), Color(gris,gris,gris))#cNegro)

update()

""" #esto deja el proceso en espera
if input("q para salir\n")=="q":
    quit()

    #if estaEnRectangulo(x,x1, y,y1, x2,y2): #proyeccion ortogonal
"""




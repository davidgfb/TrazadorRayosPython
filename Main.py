from Esfera import puntosEsfera
from PuntoInterseccion import pICompleto
from numpy import array
from Rectangulo import estaEnRectangulo
from Pixel import dibujaPixel,cambiaColorFondo
from pygame import Color
from pygame.display import set_mode,update

r=180 #esto aumenta considerablemente los calculos 
psEsfera=puntosEsfera(r,r) #puntos p

#rectangulo
x=y=0
x1=640 #resX

y1=360 #resY

#normal
normal=array([0,0,-1])

dPlano=-360

#camara origen
origen=array([320,180,-720])

#interseccion
psInterseccion=[]

for p in psEsfera: 
    psInterseccion.append(pICompleto(normal, p, origen, dPlano))

cBlanco=Color(255, 255, 255, a=255) 
cNegro=Color(0, 0, 0, a=255) 
sc=set_mode(size=[640, 360])
cambiaColorFondo(sc,cBlanco)

nPuntosPlano=len(psEsfera) 
nPuntosRectangulo=0 #puntos dentro rectangulo
for p in psEsfera:
    x2,y2,z=p
    
    if estaEnRectangulo(x,x1, y,y1, x2,y2):
        nPuntosRectangulo+=1

        dibujaPixel(sc, round(x2), round(y2), cNegro)

if nPuntosPlano==nPuntosRectangulo:
    print("los",nPuntosPlano,"puntos estan en el rectangulo!!!!!")



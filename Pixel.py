from pygame.gfxdraw import pixel,aacircle,filled_circle
from pygame.display import set_mode,update
from pygame.event import get
from pygame import Color,QUIT,quit
from time import sleep

def cambiaColorFondo(sc, color):
    sc.fill(color)
    update()

def dibujaPixel(sc, x, y, color):
    pixel(sc, x, y, color)
    #print("dibujo pixel en:",x,",",y)
    update()

"""
#colores
#cBlanco=Color(255, 255, 255, a=255) 
#cNegro=Color(0, 0, 0, a=255) 
#sc=set_mode(size=[640, 360]) #,flags = OPENGL,vsync=1)

cambiaColorFondo(sc,cBlanco)
dibujaPixel(sc, 400, 300, cNegro)

def dibujaCirculoAA():
    aacircle(sc, x, y, 100, cBlanco)
    filled_circle(sc, x, y, 100, cBlanco)
    update()

if input("q para salir\n")=="q":
    quit()


abierto=True
while abierto:
    for event in get():
        if event.type == QUIT:
            abierto=False
            quit()

    #sleep(1) #esto reduce totalmente la carga del nucleo cpu
"""

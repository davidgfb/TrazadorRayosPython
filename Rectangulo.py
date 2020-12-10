#plano 2D
def dimensionesRectangulo(x,x1, y,y1):
    """4xint-->lista
    OBJ: Calcula las dimensiones del rectangulo a partir de sus limites
    PRE: 
    """
    return [x1-x, y1-y]

#PROBADOR
"""
x=-2
x1=5

y=-5
y1=5
print(dimensionesRectangulo(x,x1, y,y1),"debe ser [7,10]")
"""

def estaEnRectangulo(x,x1, y,y1, x2,y2): #x,y
    esta=False
    
    if x<=x2<=x1 and y<=y2<=y1:
        esta=True

    return esta

#PROBADOR
"""
x=-2
x1=5

y=-5
y1=5
#print(estaEnRectangulo(x,x1, y,y1, 5,5),"debe ser True") #en (5,5)
#print(estaEnRectangulo(x,x1, y,y1, 7,5),"debe ser False") #en (7,5)
"""




                








    

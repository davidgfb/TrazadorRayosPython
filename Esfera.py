from numpy import array

#volumetrico 3d
def puntosCubo(lado, x=0):
    """int-->array
    OBJ: Calcula los puntos enteros en el interior de un cubo
         a partir de su lado V=lado^3
    """
    L=range(lado)
    puntos=[]
    
    for z in L:
        for y in L:
            for x1 in L:
                puntos.append([x+x1,y,z])

    return array(puntos)

"""
#PROBADOR
print(puntosCubo(10),"debe ser ")
"""

def estaDentroEsfera(x1,y,z, r, x):
    """4xint-->bool
    OBJ: Calcula si un punto esta dentro de una esfera de radio r
    """
    esta=False

    if (x-x1)**2+y**2+z**2<=r**2: 
        esta=True

    return esta

#PROBADOR
"""
x=0
y=0
#print(estaDentroEsfera(x,y,10, 10),"debe ser True")
#print(estaDentroEsfera(x,y,11, 10),"debe ser False")
"""

#no volumetrico
def estaSuperficieEsfera(x1,y,z, r, x):
    """4xint-->bool
    OBJ: Calcula si un punto esta dentro de una esfera de radio r
    """
    esta=False

    if (x-x1)**2+y**2+z**2==r**2:
        esta=True

    return esta

def puntosEsfera(r, x=0):
    """int-->array
    OBJ: Calcula los puntos enteros de una esfera inscrita en un cubo de lado r
    """
    psCubo=puntosCubo(r,x)
    psEsfera=[]

    for p in psCubo:
        x1,y,z=p
        
        if estaDentroEsfera(x1,y,z, r, x): #estaSuperficieEsfera(x1,y,z, r, x)
            psEsfera.append(p)

    return array(psEsfera)

#PROBADOR
"""
print(puntosEsfera(10),"debe ser ") 
""" 

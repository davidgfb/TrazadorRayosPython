from numpy import array

def d(p, origen):
    """2xarray-->array
    OBJ: Calcula el vector director de un rayo a partir de dos puntos
    PRE:
    """
    return p-origen

"""
#PROBADOR

p=array([1,1,4])
origen=array([0,1,3])
d=d(p, origen)
print(d,"debe ser [1,0,1]")
"""

def t(normal, dPlano, origen, director):
    """3xarray,int-->float
    OBJ: Calcula el parametro t a partir de la normal y
         la d del plano y el origen y vector director del rayo
    PRE: 
    """
    return -(origen@normal+dPlano)/(director@normal)

def pI(t, origen, director):
    """float,2xarray-->array
    OBJ: Calcula el punto de interseccion del plano con el rayo a partir de
         su t, origen y vector director 
    PRE: 
    """
    return array(origen+t*director)
    
    
def pICompleto(normal, p, origen, dPlano):
    """float,2xarray-->array
    OBJ: Calcula el punto de interseccion del plano con el rayo a partir de
         su t, origen y vector director 
    PRE: 
    """
    director=d(p, origen)
    return array(origen+t(normal, dPlano, origen, director)*director)

"""
#PROBADOR

#plano
normal=array([2,-3,1])
d=1
#rayo
p=array([1,1,4])
origen=array([0,1,3])

d=d(p, origen)

print(d,"debe ser [1,0,1]")

t=t(normal, d, origen, director)

print(t,"debe ser -1/3")

pI=pI(t, origen, director)

print(pI,"debe ser [-1/3, 1, 8/3]")
"""







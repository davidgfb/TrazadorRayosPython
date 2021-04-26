from numpy import array
from Plano import Plano
from Rayo import Rayo
from Punto import Punto

class Interseccion(Punto):
    def __init__(self,plano,rayo):        
        self.setCoordenadas(self.devuelvePuntoCalculado(plano.getRectaNormal(),
                                                  rayo.getDireccion(),
                                                  rayo.getCoordenadas(),
                                                  plano.getCoordenadas()))      
        Punto.__init__(self,self.getCoordenadas())
             
    def devuelvePuntoCalculado(self,rectaNormalPlano,
                               direccionRayo,coordenadasRayo,
                               coordenadasPlano):
        epsilon=1e-6
        ndotu = rectaNormalPlano.dot(direccionRayo) #numpy.array.dot
        if abs(ndotu) < epsilon:
            raise RuntimeError("no intersection or line is within plane")

        w = coordenadasRayo - coordenadasPlano     
        return -rectaNormalPlano.dot(w) / ndotu * direccionRayo +\
                   coordenadasPlano + w
    
    def toString(self):
        return "Interseccion: punto="+\
               str(self.getCoordenadas())

def main():
    #Define plane
    planeNormal = array([0, 0, 1])
    planePoint = array([0, 0, 5]) #Any point on the plane
    plano = Plano(planePoint,planeNormal)
    #print(plano.toString())

    #Define ray
    rayDirection = array([0, -1, -1])
    rayPoint = array([0, 0, 10]) #Any point along the ray
    rayo=Rayo(rayPoint,rayDirection)
    #print(rayo.toString())

    interseccion=Interseccion(plano,rayo)
    print(interseccion.toString())

main()

'''   
def setPunto(self,punto):
    self.punto=punto
  
def getPunto(self):        
    return self.punto
    
epsilon=1e-6
ndotu = planeNormal.dot(rayDirection) #numpy.array.dot
if abs(ndotu) < epsilon:
    raise RuntimeError("no intersection or line is within plane")

w = rayPoint - planePoint
return -planeNormal.dot(w) / ndotu * rayDirection +\
       planePoint + w

#self.puntoInterseccion=-planeNormal.dot(w) / ndotu * rayDirection +\
#                  planePoint + w
        
def LinePlaneCollision(planeNormal,
                       planePoint,
                       rayDirection,
                       rayPoint,
                       epsilon=1e-6):
    ndotu = planeNormal.dot(rayDirection) #numpy.array.dot
    if abs(ndotu) < epsilon:
        raise RuntimeError("no intersection or line is within plane")

    w = rayPoint - planePoint     
    return -planeNormal.dot(w) / ndotu * rayDirection +\
           planePoint + w 


Psi = LinePlaneCollision(plano.getRectaNormal(),
                         plano.getCoordenadas(),
                         rayo.getDireccion(),
                         rayo.getCoordenadas())

print ("intersection at", Psi)
'''


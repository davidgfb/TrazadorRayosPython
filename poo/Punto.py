class Punto:    
    def __init__(self,coordenadas):
        self.setCoordenadas(coordenadas)

    def setCoordenadas(self,coordenadas):
        self.coordenadas=coordenadas
    
    def getCoordenadas(self):
        return self.coordenadas

    def toString(self):
        return "Punto: coordenadas="+str(self.getCoordenadas())
    
"""
#PROBADOR
punto=Punto(0,1,2)
print(punto.toString())
"""

'''
    def __init__(self,x,y,z):
        self.setX(x)
        self.setY(y)
        self.setZ(z)
    
    def setX(self,x):
        self.x=x
    def setY(self,y):
        self.y=y
    def setZ(self,z):
        self.z=z
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    
    def getCoordenadas(self):
        return [self.getX(),self.getY(),self.getZ()]
    
    def toString(self):
        return "Punto: x="+str(self.getX())+\
               ", y="+str(self.getY())+\
               ", z="+str(self.getZ())
    '''

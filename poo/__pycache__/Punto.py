class Punto:
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

    def toString(self):
        return "Punto: x="+str(self.getX())+\
               ", y="+str(self.getY())+\
               ", z="+str(self.getZ())

"""
#PROBADOR
punto=Punto(0,1,2)
print(punto.toString())
"""        

from Punto import Punto

class Rayo(Punto):
    def __init__(self,coordenadas,direccion):
        Punto.__init__(self,coordenadas)
        self.setDireccion(direccion)
    
    def setDireccion(self,direccion):
        self.direccion=direccion

    def getDireccion(self):
        return self.direccion

    def toString(self):
        return "Rayo: coordenadas="+str(self.getCoordenadas())
    
'''
#PROBADOR
rayo = Rayo(0,1,2)
print(rayo.toString())
'''
'''
def __init__(self,x,y,z):
    Punto.__init__(self,x,y,z)
   
def __init__(self,punto,direccion):
    x,y,z=punto
    Punto.__init__(self,x,y,z)
    self.setDireccion(direccion)

def toString(self):
    return "Rayo: punto="+\
           str([self.getX(),self.getY(),self.getZ()])+\
           ", direccion="+str(self.getDireccion())
'''

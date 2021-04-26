from Punto import Punto

class Plano(Punto):    
    def __init__(self,coordenadas,rectaNormal):
        Punto.__init__(self,coordenadas)
        self.setRectaNormal(rectaNormal)

    def setRectaNormal(self,rectaNormal):
        self.rectaNormal=rectaNormal

    def getRectaNormal(self):
        return self.rectaNormal
    
    def toString(self):
        return "Plano: coordenadas="+str(self.getCoordenadas())
    
'''        
#PROBADOR
plano = Plano(0,1,2)
print(plano.toString())
'''
'''
def __init__(self,x,y,z):
    Punto.__init__(self,x,y,z)

def toString(self):
    return "Plano: punto="+\
           str([self.getX(),self.getY(),self.getZ()])+\
           ", rectaNormal="+str(self.getRectaNormal())
           #"Plano: x="+str(self.getX())+\
           #", y="+str(self.getY())+\
           #", z="+str(self.getZ())+\
'''

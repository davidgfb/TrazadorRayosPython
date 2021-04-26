from Punto import Punto #importa clase desde modulo

class Camara(Punto):
    def __init__(self,x,y,z): 
        Punto.__init__(self,x,y,z)

    def toString(self):
        return "Camara: x="+str(self.getX())+\
               ", y="+str(self.getY())+\
               ", z="+str(self.getZ())

'''
#PROBADOR
camara=Camara(1,2,3)
print(camara.toString())
'''

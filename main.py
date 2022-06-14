from re  import I,S
from abc import ABC, abstractmethod
import sys
# from arma import Arma
# from civil import Civil
# from cov import COV
# from tov import TOV 
# from vto import VTO
# from dron  import Dron
# from militar import Militar

class Dron:
    cuantos=0
    def __init__(self,ide,peso):
        self.ide=ide
        self.peso=peso 
        Dron.cuantos+=1
    #metodo que regresa el valor del atributo cuantos
    def cant_objetos(self):
        return Dron.cuantos

class Arma:
    def __init__(self,nombre,id=None):
        self.id=id
        self.nombre=nombre
#metodo es_del_dron recibe como parametro un objeto de dron y hace una asociacion entre los objetos Arma y militar
    def es_del_dron(self,d):
        if isinstance(d,TOV):
            self.id=d.ide
        elif  isinstance(d,VTO):
            self.id=d.ide

class Militar(Dron):
    def __init__(self, ide, peso,arma=None):
        super().__init__(ide, peso)
        self.arma=[]
#metodo get_armas devuelve el id de militar junto con el nombre de cada arma que posee militar, caso contrario  de tener 0 retorna  "NO"        
    
    def get_armas(self):
        a="NO"
        if self.arma!=[]:
            a=""
            for i in range (len(self.arma)):
                if i==(len(self.arma))-1:
                    a=a+self.ide+" tiene "+self.arma[i]
                else:
                    a=a+self.ide+" tiene "+self.arma[i]+"\n"
        return a
    def set_armas(self,a):
        if isinstance(self,TOV):
            self.arma.append(a.nombre)
        if isinstance(self,VTO) and self.peso >30:
            self.arma.append(a.nombre)
class Civil(ABC):

    @abstractmethod
    def tiene_armas():
        pass

class TOV(Militar):
    def __init__(self,ide,peso,arma=None):
        super().__init__(ide,peso)
    def tiene_armas(self):
        if self.arma!=[]:
            return True
        else:
            return False        

class VTO(Militar,Civil):
    def __init__(self, ide, peso,arma=None):
        super().__init__(ide,peso)
    def tiene_armas(self):
        if self.arma!=[]:
            return True
        else:
            return False

class COV(Dron,Civil):
    def __init__(self, ide, peso):
        super().__init__(ide,peso)
    def tiene_armas(self):
        return False


if __name__ == '__main__':
    d1=TOV("m1",32)
    d2=COV("c1",38)
    d3=VTO("mc1",35)
    d4=TOV("m2",25)
    d5=VTO("mc2",23)
    a1=Arma("misil")
    a2=Arma("cañon")
    a3=Arma("cohete")
    a4=Arma("misil")
    a5=Arma("gas")
    d1.set_armas(a1)
    d1.set_armas(a5)
    d3.set_armas(a2)
    d4.set_armas(a3)
    print(d1.get_armas())
    print(d3.get_armas())
    print(d4.get_armas())
    a1.es_del_dron(d1)
    print(d2.__dict__)
    print(d2.tiene_armas())
    print(d3.tiene_armas())
    print(d2.tiene_armas())
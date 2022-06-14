import unittest
from parameterized import parameterized
from main import Arma
from main import Civil
from main import COV
from main import TOV 
from main import VTO
from main import Dron
from main import Militar

class TestApp(unittest.TestCase):

    @parameterized.expand([('mc1',35,
    {'ide': 'mc1', 'peso': 35}),
    ('m1',32,{'ide': 'm1', 'peso': 32})
    ])
    def test_atributos_dron(self, id, peso, atributos):
        object = Dron(id, peso)
        self.assertDictEqual(object.__dict__, atributos)
    @parameterized.expand([('misil',{'id': None, 'nombre': 'misil'}),
    ('cañon',{'id': None, 'nombre': 'cañon'})
    ])    
    def test_atributos_arma(self,nombre,atributos):
        object = Arma(nombre)
        self.assertDictEqual(object.__dict__, atributos)
    def test_cuantos_drones(self):
        object = Dron(23,"m2")
        self.assertEqual(object.cant_objetos(),5)
    def test_es_del_dron(self):
        d1=VTO("d1",32)
        d2=COV("d4",38)
        a1=Arma("misil")
        a2=Arma("cañon")
        a1.es_del_dron(d1)
        a2.es_del_dron(d2)
        self.assertEqual(str(a1.__dict__),str({'id': 'd1', 'nombre': 'misil'}))
        self.assertEqual(str(a2.__dict__),str({'id': None, 'nombre': 'cañon'}))
    def test_armas(self):
        d1=TOV("dron3",32)
        d2=VTO("dron4",25)
        a1=Arma("misil")
        a2=Arma("cañon")
        d1.set_armas(a1)
        d1.set_armas(a2)
        d2.set_armas(a1)
        self.assertEqual(d1.get_armas(),"dron3 tiene misil\n"+
                                        "dron3 tiene cañon")
        self.assertEqual(d2.get_armas(),"NO")
    def test_tiene_armas(self):
        d1=TOV("dron1",32)
        d2=COV("dron2",25)
        a1=Arma("misil")
        a2=Arma("cañon")
        d1.set_armas(a1)
        self.assertEqual(d1.tiene_armas(),True)
        self.assertEqual(d2.tiene_armas(),False)                       
if __name__ == '__main__':
    unittest.main()
    

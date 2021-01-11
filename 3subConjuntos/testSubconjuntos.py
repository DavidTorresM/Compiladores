import sys,os,re
sys.path.append("../1AFNtoAFD/")
import unittest
from AF import ParserData, AF
from AFN import AFN
from Subconjuntos import Subconjuntos


class TestStringMethods(unittest.TestCase):
    def init(self):


        self.afn_test1 = AFN(None,None,None,None,None)
        self.afn_test1.agregar_transicion(1,2,'E')
        self.afn_test1.agregar_transicion(1,5,'E')
        self.afn_test1.agregar_transicion(2,3,'a')
        self.afn_test1.agregar_transicion(3,4,'b')
        self.afn_test1.agregar_transicion(4,9,'E')
        self.afn_test1.agregar_transicion(5,6,'E')
        self.afn_test1.agregar_transicion(6,7,'a')
        self.afn_test1.agregar_transicion(7,6,'E')
        self.afn_test1.agregar_transicion(7,8,'E')
        self.afn_test1.agregar_transicion(8,9,'E')
        self.afn_test1.establecer_final(9)
        self.afn_test1.establecer_inicial(1)


        self.afn_test2 = AFN(None,None,None,None,None)
        self.afn_test2.agregar_transicion(1,2,'E')
        self.afn_test2.agregar_transicion(2,3,'E')
        self.afn_test2.agregar_transicion(3,4,'E')
        self.afn_test2.agregar_transicion(4,5,'a')
        self.afn_test2.agregar_transicion(5,6,'b')
        self.afn_test2.agregar_transicion(6,4,'E')
        self.afn_test2.agregar_transicion(3,7,'E')
        self.afn_test2.agregar_transicion(7,3,'E')
        self.afn_test2.agregar_transicion(7,8,'E')
        self.afn_test2.agregar_transicion(8,9,'b')


        self.afn_test2.establecer_final(9)
        self.afn_test2.establecer_inicial(1)


        self.afn_test_rs3 = AFN(None,None,None,None,None)
        self.afn_test_rs3.agregar_transicion(1,2,'a')
        self.afn_test_rs3.agregar_transicion(1,3,'b')
        self.afn_test_rs3.agregar_transicion(2,2,'a')
        self.afn_test_rs3.agregar_transicion(2,4,'b')
        self.afn_test_rs3.agregar_transicion(3,3,'b')
        self.afn_test_rs3.agregar_transicion(3,2,'a')
        self.afn_test_rs3.agregar_transicion(4,2,'a')
        self.afn_test_rs3.agregar_transicion(4,5,'b')
        self.afn_test_rs3.agregar_transicion(5,3,'b')
        self.afn_test_rs3.agregar_transicion(5,2,'a')

        self.afn_test_rs3.establecer_final(5)
        self.afn_test_rs3.establecer_inicial(1)


        self.afn_test3 = AFN(None,None,None,None,None)
        self.afn_test3.agregar_transicion(0,1,'E')
        self.afn_test3.agregar_transicion(0,7,'E')
        self.afn_test3.agregar_transicion(1,2,'E')
        self.afn_test3.agregar_transicion(1,4,'E')
        self.afn_test3.agregar_transicion(2,3,'a')
        self.afn_test3.agregar_transicion(3,6,'E')
        self.afn_test3.agregar_transicion(4,5,'b')
        self.afn_test3.agregar_transicion(5,6,'E')
        self.afn_test3.agregar_transicion(6,1,'E')
        self.afn_test3.agregar_transicion(6,7,'E')
        self.afn_test3.agregar_transicion(7,8,'a')
        self.afn_test3.agregar_transicion(8,9,'b')
        self.afn_test3.agregar_transicion(9,10,'b')

        self.afn_test3.establecer_inicial(0)
        self.afn_test3.establecer_final(10)

    def test_convertir(self):
        self.init()
        algo = Subconjuntos(self.afn_test3)
        rs = algo.convertir(self.afn_test3)
        self.assertEqual(rs,afn_test_rs3)



    def test_cerradura1(self):
        self.init()
        algo = Subconjuntos(self.afn_test1)
        rs = algo.cerradura({1})

        setFinal = {1,2,5,6}

        self.assertEqual(rs,setFinal)


    def test_mover1(self):
        self.init()

        algo = Subconjuntos(self.afn_test1)
        rs = algo.mover({1,2,5,6},'a')

        setFinal = {3,7}
        
        self.assertEqual(rs,setFinal)

    def test_cerradura2(self):
        self.init()
        algo = Subconjuntos(self.afn_test1)
        rs = algo.cerradura({7})

        setFinal = {7,6,8,9}
        
        self.assertEqual(rs,setFinal)

    def test_mover2(self):
        self.init()

        algo = Subconjuntos(self.afn_test1)
        rs = algo.mover({1,2,5,6},'b')

        setFinal = set()
        
        self.assertEqual(rs,setFinal)

    def test_cerradura3(self):
        self.init()

        algo = Subconjuntos(self.afn_test2)
        rs = algo.cerradura({3})

        setFinal = {3,7,4,8}
        
        self.assertEqual(rs,setFinal)

    def test_mover3(self):
        self.init()

        algo = Subconjuntos(self.afn_test2)
        rs = algo.mover({2,3,4,7,8},'a')

        setFinal = {5}
        
        self.assertEqual(rs,setFinal)

    def test_cerradura4(self):
        self.init()

        algo = Subconjuntos(self.afn_test2)
        rs = algo.cerradura({2})

        setFinal = {2,3,7,4,8}
        
        self.assertEqual(rs,setFinal)

    def test_mover4(self):
        self.init()

        algo = Subconjuntos(self.afn_test2)
        rs = algo.mover({2,3,4,7,8},'b')

        setFinal = {9}
        
        self.assertEqual(rs,setFinal)

if __name__ == '__main__':
    unittest.main()
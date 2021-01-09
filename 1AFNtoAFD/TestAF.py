import unittest
from AF import ParserData, AF

class TestStringMethods(unittest.TestCase):
    def test_load_data_source_1(self):
        parser = ParserData()
        q0 = 1
        F = [4]
        tra = [
            (1,2,'E'),
            (1,8,'E'),
            (2,3,'E'),
            (2,5,'E'),
            (3,4,'a')
        ]
        self.assertEqual(parser.load_data_source("test1.txt"), (q0,F,tra))
    def test_load_data_source_2(self):
        parser = ParserData()
        q0 = 7
        F = [2,3,5]
        tra = [
            (1,2,'E'),
            (1,8,'E'),
            (2,3,'E'),
            (2,5,'E'),
            (3,1,'a')
        ]
        self.assertEqual(parser.load_data_source("test2.txt"), (q0,F,tra))

    def test_agregar_transicion1(self):
        af = AF(None,None,None,None,None)
        af.agregar_transicion(2,3,'a')
        af.agregar_transicion(5,2,'b')
        af.agregar_transicion(7,3,'b')
        self.assertEqual(af.delta,{'a':{2:{3}},'b':{5:{2},7:{3}}})
    

    def test_eliminar_transicion1(self):
        af = AF(None,None,None,None,None)
        af.agregar_transicion(2,3,'a')
        af.agregar_transicion(5,2,'b')
        af.agregar_transicion(7,3,'b')
        af.eliminar_transicion(6,7,'z')
        af.eliminar_transicion(5,2,'b')
        self.assertEqual(af.delta,{'a':{2:{3}},'b':{7:{3}}})


    def test_esAFN1(self):
        sigma_alfabeto = ['a','b','z']
        delta_mat = {'a':{2:{3}},'b':{5:{2},7:{3},3:{5}}}
        af = AF(None,None,sigma_alfabeto,None,delta_mat)
        rs = af.esAFN()
        self.assertEqual(rs, False)


    def test_esAFN2(self):
        sigma_alfabeto = ['a','b','z']
        delta_mat = {'a':{2:{3}},'b':{5:{2},7:{3},3:{5,7}}}
        af = AF(None,None,sigma_alfabeto,None,delta=delta_mat)
        rs = af.esAFN()
        self.assertEqual(rs, True)


    def test_esAFN3(self):
        sigma_alfabeto = ['a','b','E']
        delta_mat = {'a':{2:{3}},'b':{5:{2},7:{3},3:{7}}}
        af = AF(None,None,sigma_alfabeto,None,delta=delta_mat)
        rs = af.esAFN()
        self.assertEqual(rs, True)


    def test_eliminar_transicion2(self):
        af = AF(None,None,None,None,None)
        af.agregar_transicion(2,3,'a')
        af.agregar_transicion(5,2,'b')

        af.agregar_transicion(7,1,'b')
        af.agregar_transicion(7,3,'b')
        af.agregar_transicion(7,4,'b')
        af.agregar_transicion(7,8,'b')
        
        af.eliminar_transicion(7,1,'b')
        af.eliminar_transicion(7,3,'b')
        af.eliminar_transicion(7,4,'b')
        af.eliminar_transicion(7,8,'b')
        
        self.assertEqual(af.delta,{'a':{2:{3}},'b':{5:{2}}})




if __name__ == '__main__':
    unittest.main()
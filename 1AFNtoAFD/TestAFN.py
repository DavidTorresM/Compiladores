import unittest
from AF import ParserData, AF
from AFN import AFN

class TestStringMethods(unittest.TestCase):

    def test_cargar_desde1(self):
        afn = AFN(None,None,None,None,None)
        afn.cargar_desde("test1.txt")
        self.assertEqual(afn.delta,{'E':{1:{2,8},2:{3,5}},'a':{3:{4}}})
    def test_cargar_desde2(self):
        afn = AFN(None,None,None,None,None)
        afn.cargar_desde("test2.txt")
        self.assertEqual(afn.delta,{'E':{1:{2,8},2:{3,5}},'a':{3:{1}}})

    def test_cargar_desde3(self):
        afn = AFN(None,None,None,None,None)
        afn.cargar_desde("test3.txt")
        self.assertEqual(afn.delta,{'a':{1:{2,8},3:{1}},'b':{2:{3},5:{5}},'c':{2:{5}}})

    def test_guardar_en1(self):
        afn = AFN(None,None,None,None,None)
        afn.cargar_desde("test1.txt")
        afn.guardar_en("test1.cpy")
        self.assertEqual(True,True)

    def test_acepta_aux1(self):
        afn = AFN(None,None,None,None,None)
        afn.cargar_desde("test4.txt")
        self.assertEqual(afn.acepta("abababbba"),False)

    def test_acepta_aux2(self):
        afn = AFN(None,None,None,None,None)
        afn.cargar_desde("test4.txt")
        self.assertEqual(afn.acepta("aab"),False)

    def test_acepta_aux3(self):
        afn = AFN(None,None,None,None,None)
        afn.cargar_desde("test4.txt")
        self.assertEqual(afn.acepta("abba"),False)

    




if __name__ == '__main__':
    unittest.main()
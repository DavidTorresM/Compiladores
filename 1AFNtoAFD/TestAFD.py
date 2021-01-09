import unittest
from AF import ParserData, AF
from AFD import AFD

class TestStringMethods(unittest.TestCase):

    def test_cargar_desde1(self):
        afn = AFD(None,None,None,None,None)
        afn.cargar_desde("test5.txt")
        self.assertEqual(afn.delta,{"a":{1:2,2:4,3:1,4:1},"b":{1:3,4:5},"c":{4:2,3:5}})

    def test_guardar_en1(self):
        afn = AFD(None,None,None,None,None)
        afn.cargar_desde("test5.txt")
        afn.guardar_en("test5.cpy")
        self.assertEqual(True,True)

    def test_acepta_aux1(self):
        afn = AFD(None,None,None,None,None)
        afn.cargar_desde("test5.txt")
        self.assertEqual(afn.acepta("abababbba"),False)


    def test_acepta_aux2(self):
        afn = AFD(None,None,None,None,None)
        afn.cargar_desde("test5.txt")
        self.assertEqual(afn.acepta("aa"),True)

    def test_acepta_aux3(self):
        afn = AFD(None,None,None,None,None)
        afn.cargar_desde("test5.txt")
        self.assertEqual(afn.acepta("bc"),False)

    def test_acepta_aux4(self):
        afn = AFD(None,None,None,None,None)
        afn.cargar_desde("test5.txt")
        self.assertEqual(afn.acepta("babaaacacaca"),True)



    def test_acepta_aux5(self):
        afn = AFD(None,None,None,None,None)
        afn.cargar_desde("test5.txt")
        self.assertEqual(afn.acepta("aaa"),False)
    




if __name__ == '__main__':
    unittest.main()
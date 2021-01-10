import sys,os,re
sys.path.append("../1AFNtoAFD/")
import unittest
from AF import ParserData, AF
from AFN import AFN

class TestStringMethods(unittest.TestCase):
    def test_convertir_posfija1(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("(a|b|c)*")
        self.assertEqual(rs,"ab|c|*")

    def test_convertir_posfija2(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("((a|b|c)*|e+|r)+|a")
        self.assertEqual(rs,"ab|c|*e+|r|+a|")

    def test_convertir_posfija3(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("(((a*|b*|c)*|c)*)+b")
        self.assertEqual(rs,"a*b*|c|*c|*+b.")

    def test_convertir_posfija4(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("(a|c)b")
        self.assertEqual(rs,"ac|b.")

    def test_convertir_posfija5(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("(a|c)*b")
        self.assertEqual(rs,"ac|*b.")

    def test_convertir_posfija6(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("(ab)*b")
        self.assertEqual(rs,"ab.*b.")

    def test_convertir_posfija7(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("(a|b)(ab)")
        self.assertEqual(rs,"ab|ab..")

    def test_convertir_posfija8(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("abcd")
        self.assertEqual(rs,"ab.c.d.")

    def test_convertir_posfija9(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("a|bc|d")
        self.assertEqual(rs,"abc.|d|")
    
    def test_convertir_posfija10(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.convertir_posfija("a|b+c|d")
        self.assertEqual(rs,"ab+c.|d|")

    def test_proces_cadena1(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.proces_cadena("(((a*|b*|c)*|c)*)+b")
        self.assertEqual(rs,"(((a*|b*|c)*|c)*)+.b")

    def test_proces_cadena2(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.proces_cadena("abc")
        self.assertEqual(rs, "a.b.c")

    def test_proces_cadena3(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.proces_cadena("(a|b|c)(a|c)")
        self.assertEqual(rs, "(a|b|c).(a|c)")

    def test_proces_cadena4(self):
        afn = AFN(None,None,None,None,None)
        rs = afn.proces_cadena("(a|b|c)de")
        self.assertEqual(rs, "(a|b|c).d.e")

    def test_agregar_transicion1(self):
        afn = AFN(None,None,None,None,None)
        afn.agregar_transicion(1,2,'a')
        self.assertEqual(afn.Q, {1,2})

    def test_agregar_transicion2(self):
        afn = AFN(None,None,None,None,None)
        afn.agregar_transicion(1,2,'a')
        afn.agregar_transicion(2,1,'c')
        afn.agregar_transicion(2,3,'a')
        self.assertEqual(afn.Q, {1,2,3})

    def test_concatenar1(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.agregar_transicion(2,3,'b')
        af.agregar_transicion(1,3,'b')
        af.agregar_transicion(1,1,'b')
        af.agregar_transicion(4,1,'z')
        af.establecer_inicial(4)
        af.establecer_final(3)
        af2 = AFN(None,None,None,None,None)
        af2.agregar_transicion(1,2,'a')
        af2.agregar_transicion(3,1,'b')
        af2.agregar_transicion(2,1,'b')
        af2.establecer_inicial(3)
        af2.establecer_final(2)
        dic = {"a":{1:{2},5:{6}},"b":{2:{3},1:{3,1},7:{5},6:{5}},"z":{4:{1}}}
        self.assertEqual(af2.concatenar(af,af2),dic)

    def test_concatenar2(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)
        af2 = AFN(None,None,None,None,None)
        af2.agregar_transicion(1,2,'a')
        af2.agregar_transicion(2,3,'b')
        af.establecer_inicial(1)
        af.establecer_final(3)

        dic = {"a":{1:{2},2:{3}},"b":{3:{4}}}
        self.assertEqual(af2.concatenar(af,af2),dic)


    def test_juntar_edos1(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)
        af2 = AFN(None,None,None,None,None)
        af2.agregar_transicion(1,2,'a')
        af2.agregar_transicion(2,3,'b')
        af.establecer_inicial(1)
        af.establecer_final(3)

        dic = {"a":{1:{2},2:{3}},"b":{3:{4}}}
        af2.juntar_edos(af,af2)

        self.assertEqual(af2.delta,dic)


if __name__ == '__main__':
    unittest.main()
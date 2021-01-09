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





if __name__ == '__main__':
    unittest.main()
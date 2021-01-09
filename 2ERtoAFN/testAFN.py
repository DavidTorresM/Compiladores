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
        self.assertEqual(rs,"a*b*|c|*c|*+b")


    




if __name__ == '__main__':
    unittest.main()
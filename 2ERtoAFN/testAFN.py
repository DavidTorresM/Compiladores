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
    
    def test_sumar_offset_grafo1(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)
        af.sumar_offset_grafo(af,5)
        self.assertEqual(af.delta, {"a":{6:{7}}})
    
    def test_sumar_offset_grafo2(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.agregar_transicion(2,3,'b')
        af.agregar_transicion(1,3,'b')
        af.agregar_transicion(1,1,'b')
        af.agregar_transicion(4,1,'z')
        af.establecer_inicial(4)
        af.establecer_final(3)
        af.sumar_offset_grafo(af,5)
        self.assertEqual(af.delta, {"a":{6:{7}},"b":{6:{8,6},7:{8}},"z":{9:{6}}})

    def test_juntar_afns1(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)
        af2 = AFN(None,None,None,None,None)
        af2.agregar_transicion(1,2,'a')
        af2.agregar_transicion(2,3,'b')
        af2.establecer_inicial(1)
        af2.establecer_final(3)

        af.sumar_offset_grafo(af2,max(af.Q))
        af.juntar_afns(af,af2)

        dic = {"a":{1:{2},3:{4}},"b":{4:{5}}}
        self.assertEqual(af.delta,dic)


    def test_juntar_afns2(self):
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


        af.sumar_offset_grafo(af2,max(af.Q))
        af.juntar_afns(af,af2)

        dic = {"a":{1:{2},5:{6}},"b":{2:{3},1:{3,1},7:{5},6:{5}},"z":{4:{1}}}

        self.assertEqual(af.delta,dic)

    def test_cambiar_edos1(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.agregar_transicion(2,3,'b')
        af.agregar_transicion(1,3,'b')
        af.agregar_transicion(1,1,'b')
        af.agregar_transicion(4,1,'z')
        af.establecer_inicial(4)
        af.establecer_final(3)
        af.cambiar_edos(af,2,10)
        af.cambiar_edos(af,3,30)
        self.assertEqual(af.delta, {"a":{1:{10}},"b":{10:{30},1:{30,1}},"z":{4:{1}}})
    def test_cambiar_edos2(self):
        af = AFN(None,None,None,None,None)
        af.delta = {'a': {1: {2}, 5: {6}}, 'b': {2: {3}, 1: {1, 3}, 7: {5}, 6: {5}}, 'z': {4: {1}}}
        af.cambiar_edos(af,3,7)
        dic = {'a': {1: {2}, 5: {6}}, 'b': {2: {7}, 1: {1, 7}, 7: {5}, 6: {5}}, 'z': {4: {1}}}
        self.assertEqual(af.delta, dic)



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
        af.concatenar(af,af2)  

        dic = {"a":{1:{2},5:{6}},"b":{2:{7},1:{7,1},7:{5},6:{5}},"z":{4:{1}}}

        self.assertEqual(af.delta,dic)
        self.assertEqual(af.obtener_inicial(),4)
        self.assertEqual(af.obtener_final(),6)

    def test_concatenar2(self):
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
        af.concatenar(af,af2)  

        dic = {"a":{1:{2},5:{6}},"b":{2:{7},1:{7,1},7:{5},6:{5}},"z":{4:{1}}}

        self.assertEqual(af.delta,dic)

    def test_concatenar3(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)
        af2 = AFN(None,None,None,None,None)
        af2.agregar_transicion(1,2,'a')
        af2.agregar_transicion(2,3,'b')
        af2.establecer_inicial(1)
        af2.establecer_final(3)

        af.concatenar(af,af2)  

        dic = {"a":{1:{3},3:{4}},"b":{4:{5}}}
        self.assertEqual(af.delta, dic)

        self.assertEqual(af.obtener_inicial(),1)
        self.assertEqual(af.obtener_final(),5)

    def test_concatenar4(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(4,1,'E')
        af.agregar_transicion(1,2,'a')
        af.agregar_transicion(2,1,'E')
        af.agregar_transicion(2,3,'E')
        af.establecer_inicial(4)
        af.establecer_final(3)
        af2 = AFN(None,None,None,None,None)
        af2.agregar_transicion(4,1,'E')
        af2.agregar_transicion(1,2,'b')
        af2.agregar_transicion(2,3,'E')
        af2.establecer_inicial(4)
        af2.establecer_final(3)

        af.concatenar(af,af2)  

        dic = {"a":{1:{2}},"b":{5:{6}},"E":{4:{1},2:{1,8},8:{5},6:{7}}}
        self.assertEqual(af.delta, dic)

        self.assertEqual(af.obtener_inicial(),4)
        self.assertEqual(af.obtener_final(),7)

    def test_cerradura_kleen1(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)

        af.cerradura_kleen(af)

        dic = {"a":{1:{2}},"E":{4:{1,3},2:{1,3}}}
        q0 = 4
        qf = 3

        self.assertEqual(af.delta, dic)
        self.assertEqual(af.obtener_inicial(), q0)
        self.assertEqual(af.obtener_final(), qf)
    
    def test_cerradura_kleen2(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(4,1,'E')
        af.agregar_transicion(1,2,'a')
        af.agregar_transicion(2,1,'E')
        af.agregar_transicion(2,3,'E')
        af.establecer_inicial(4)
        af.establecer_final(3)

        af.cerradura_kleen(af)  

        dic = {"a":{1:{2}},"E":{4:{1},2:{1,3},3:{4,5},6:{4,5}}}
        q0 = 6
        qf = 5

        self.assertEqual(af.delta, dic)
        self.assertEqual(af.obtener_inicial(), q0)
        self.assertEqual(af.obtener_final(), qf)

    def test_cerradura_kleen3(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)

        af.cerradura_kleen(af)
        af.cerradura_kleen(af)

        dic = {"a":{1:{2}},"E":{4:{1,3},2:{1,3},3:{4,5},6:{4,5}}}
        q0 = 6
        qf = 5

        self.assertEqual(af.delta, dic)
        self.assertEqual(af.obtener_inicial(), q0)
        self.assertEqual(af.obtener_final(), qf)
    def test_cerradura_positiva1(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)

        af.cerradura_positiva(af)

        dic = {"a":{1:{2}},"E":{4:{1},2:{1,3}}}
        q0 = 4; qf = 3

        self.assertEqual(af.delta, dic)
        self.assertEqual(af.obtener_inicial(), q0)
        self.assertEqual(af.obtener_final(), qf)
    
    def test_cerradura_positiva2(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(4,1,'E')
        af.agregar_transicion(1,2,'a')
        af.agregar_transicion(2,1,'E')
        af.agregar_transicion(2,3,'E')
        af.establecer_inicial(4)
        af.establecer_final(3)

        af.cerradura_positiva(af)  

        dic = {"a":{1:{2}},"E":{4:{1},2:{1,3},3:{4,5},6:{4}}}
        q0 = 6
        qf = 5

        self.assertEqual(af.delta, dic)
        self.assertEqual(af.obtener_inicial(), q0)
        self.assertEqual(af.obtener_final(), qf)

    def test_union1(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)

        af1 = AFN(None,None,None,None,None)
        af1.agregar_transicion(1,2,'b')
        af1.establecer_inicial(1)
        af1.establecer_final(2)

        #print(af.delta)

        af.union(af,af1)

        #print(af.delta)

        dic = {"a":{1:{2}}, "b":{6:{7}},"E":{4:{1,6},7:{3},2:{3}}}
        q0 = 4
        qf = 3

        self.assertEqual(af.delta, dic)
        self.assertEqual(af.obtener_inicial(), q0)
        self.assertEqual(af.obtener_final(), qf)
    

    def test_union2(self):
        af = AFN(None,None,None,None,None)
        af.agregar_transicion(1,2,'a')
        af.establecer_inicial(1)
        af.establecer_final(2)

        af1 = AFN(None,None,None,None,None)
        af1.agregar_transicion(1,2,'b')
        af1.establecer_inicial(1)
        af1.establecer_final(2)


        af2 = AFN(None,None,None,None,None)
        af2.agregar_transicion(1,2,'c')
        af2.establecer_inicial(1)
        af2.establecer_final(2)

        #print(af.delta)

        af.union(af,af1)
        af.union(af,af2)

        #print(af.delta)

        dic = {"a":{1:{2}},"b":{6:{7}},"c":{11:{12}},"E":{2:{3},3:{8},7:{3},4:{1,6},12:{8},9:{11,4}}}
        q0 = 9
        qf = 8

        self.assertEqual(af.delta, dic)
        self.assertEqual(af.obtener_inicial(), q0)
        self.assertEqual(af.obtener_final(), qf)



    def test_convertir1(self):
        afn = AFN(None,None,None,None,None)
        automata = afn.convertir("a|b|c")
        dic = {"a":{1:{2}},"b":{6:{7}},"c":{11:{12}},"E":{2:{3},3:{8},7:{3},4:{1,6},12:{8},9:{11,4}}}
        q0 = 9
        qf = 8
        self.assertEqual(automata.delta, dic)
        self.assertEqual(automata.obtener_inicial(), q0)
        self.assertEqual(automata.obtener_final(), qf)

    def test_convertir2(self):
        afn = AFN(None,None,None,None,None)
        automata = afn.convertir("(a|b|c)")
        dic = {"a":{1:{2}},"b":{6:{7}},"c":{11:{12}},"E":{2:{3},3:{8},7:{3},4:{1,6},12:{8},9:{11,4}}}
        q0 = 9
        qf = 8
        self.assertEqual(automata.delta, dic)
        self.assertEqual(automata.obtener_inicial(), q0)
        self.assertEqual(automata.obtener_final(), qf)
    
    def test_convertir3(self):
        afn = AFN(None,None,None,None,None)
        automata = afn.convertir("(a|b|c)*")
        dic = {"a":{1:{2}},"b":{6:{7}},"c":{11:{12}},"E":{2:{3},3:{8},7:{3},4:{1,6},12:{8},9:{11,4},8:{9,13},14:{13,9}}}
        q0 = 14
        qf = 13
        self.assertEqual(automata.delta, dic)
        self.assertEqual(automata.obtener_inicial(), q0)
        self.assertEqual(automata.obtener_final(), qf)

    def test_convertir4(self):
        afn = AFN(None,None,None,None,None)
        automata = afn.convertir("(a|b|c)*z")
        dic = {"a":{1:{2}},"b":{6:{7}},"c":{11:{12}},"z":{15:{16}},"E":{2:{3},3:{8},7:{3},4:{1,6},12:{8},9:{11,4},8:{9,15},14:{15,9}}}
        q0 = 14
        qf = 16
        self.assertEqual(automata.delta, dic)
        self.assertEqual(automata.obtener_inicial(), q0)
        self.assertEqual(automata.obtener_final(), qf)

    def test_convertir5(self):
        afn = AFN(None,None,None,None,None)
        automata = afn.convertir("(a|b|c)+z")
        dic = {"a":{1:{2}},"b":{6:{7}},"c":{11:{12}},"z":{15:{16}},"E":{2:{3},3:{8},7:{3},4:{1,6},12:{8},9:{11,4},8:{9,15},14:{9}}}
        q0 = 14
        qf = 16
        self.assertEqual(automata.delta, dic)
        self.assertEqual(automata.obtener_inicial(), q0)
        self.assertEqual(automata.obtener_final(), qf)




if __name__ == '__main__':
    unittest.main()
import unittest
import Subconjuntos as s

class TestSubConjuntos(unittest.TestCase):

	def test_elipson1(self):
		aut = s.get_automata()
		respuesta = s.elipson(aut,1)
		self.assertEqual(respuesta, {1,2,3,7})

	def test_elipson2(self):
		aut = s.get_automata()
		respuesta = s.elipson(aut,4)
		self.assertEqual( respuesta, {4})

	def test_elipson3(self):
		aut = s.get_automata()
		respuesta = s.elipson(aut,8)
		print("resultado",respuesta)
		self.assertEqual( respuesta, {2,9,11,3,6,7,8})


	def test_dp_mover(self):
		aut = s.get_automata()
		dic = s.dp_mover(aut)
		self.assertEqual( dic, { 0:{3:{4}}, 1:{4:{5}}, 2:{7:{8}}, 3:{9:{10}} })


	def test_cerradura(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())




if __name__ == '__main__':
	unittest.main()
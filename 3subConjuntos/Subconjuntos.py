import sys,os,re
sys.path.append("../1AFNtoAFD/")

from AF import AF
from AFN import AFN
from AFD import AFD

class Subconjuntos(object):
	"""docstring for Subconjuntos"""
	def __init__(self, afn):
		super(Subconjuntos, self).__init__()
		self.afn = afn

	def cerradura(self, edos):
		return self.cerradura_aux(edos,set())

	def cerradura_aux(self, edos,result):
		delta = self.afn.delta
		for edo_i in edos:
			result.add(edo_i)
			siguientes_edoi = delta["E"][edo_i] if edo_i in delta["E"].keys() else set()
			if len(siguientes_edoi) != 0:#mas estados a visitar
				#quitar estados ya visitados
				siguientes_edoi = set(filter(lambda x:x not in result,siguientes_edoi))
				result.update(self.cerradura_aux(siguientes_edoi,result))
		return result




	def mover(self, conjunto, caracter):
		pass
	def convertir(self, afn: AFN) -> AFD:
		pass

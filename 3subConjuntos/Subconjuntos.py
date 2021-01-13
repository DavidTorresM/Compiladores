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
		siguientes_carac = self.afn.delta[caracter]
		origen_caracter = set(siguientes_carac.keys())
		result_set = set()
		for edo_i in origen_caracter:
			if edo_i in conjunto:
				result_set.update(self.afn.delta[caracter][edo_i])
		return result_set



	def convertir(self, afn: AFN) -> AFD:
		alfabeto = [i for i in afn.sigma if i!='E']
		A = self.cerradura({afn.obtener_inicial()})
		edos_faltante = [A]; edos_final = [A]; transiciones = []

		while len(edos_faltante) > 0:
			edo_i = edos_faltante.pop()
			for caracter in alfabeto:
				edo_next = self.mover(edo_i,caracter)
				edo_next = self.cerradura(edo_next)
				if len(edo_next) > 0:
					transiciones.append((edo_i,caracter,edo_next))
					if edo_next not in edos_final:
						edos_faltante.append(edo_next)
						edos_final.append(edo_next)

		#sacar los finales 
		finales = afn.obtener_finales()
		afd = AFD(None,None,None,None,None)

		for edo_i_set, caracter, edo_f_set in transiciones:
			afd.agregar_transicion(edos_final.index(edo_i_set)+1,edos_final.index(edo_f_set)+1,caracter)

		edos_finales = []
		for edo_i in edos_final:
			for final in finales:
				if final in edo_i:
					edos_finales.append(edos_final.index(edo_i)+1)
		afd.establecer_finales(edos_finales)

		return afd



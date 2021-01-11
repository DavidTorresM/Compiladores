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
		afd = AFD(None,None,None,None,None)
		A = self.cerradura({afn.obtener_inicial()})
		alfabeto = afn.sigma

		sets_generados = {A}; sets_generados_aux = {A}
		transiciones = []

		while len(sets_generados) != 0:
			set_i = list(sets_generados)[0]
			sets_generados_aux.add(set_i)
			for car in alfabeto:
				set_nuevo = self.cerradura(self.mover(set_i,car))
				if len(set_nuevo) != 0:
					sets_generados.add(set_nuevo)
					transiciones.append((set_i,set_nuevo.copy(),caracter))#(origen,destino,caracter)
			sets_generados.remove(set_i)

		sets_generados = list(sets_generados)
		for origen_s, destino_s, caracter in transiciones:
			afd.agregar_transicion(sets_generados.index(origen_s)+1,sets_generados.index(destino_s)+1,caracter)
		#Faltan los finales

		return afd

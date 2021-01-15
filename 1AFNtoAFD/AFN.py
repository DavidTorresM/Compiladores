import functools 
from AF import ParserData, AF

class AFN(AF):
	"""docstring for AFN"""
	def __init__(self, Q, q0, sigma, F, delta ):
		super(AFN, self).__init__(Q, q0, sigma, F, delta)
		
		self.Q = Q
		self.q0 = q0
		if sigma==None:
			self.sigma = set()
		else:
			self.sigma = sigma
		self.F = F
		if delta==None:
			self.delta = {}
		else:
			self.delta = delta
	def cargar_desde(self, nombre:str):
		loader = ParserData()
		(q0, F, tra) = loader.load_data_source(nombre)
		self.q0 = q0; self.F = F
		self.sigma = [z for _,_,z in tra]
		for caracter in self.sigma:
			caract  = [ (qi,qf,z) for qi,qf,z in tra if z == caracter ]
			edosInit = { qi for qi,qf,z in caract }
			edosInit = list( edosInit )
			self.delta[caracter] = {}
			for edoini in edosInit:
				self.delta[caracter][edoini] = { qf for qi,qf,z in caract if qi == edoini }
	
	def guardar_en(self, nombre:str):
		F = [str(i) for i in self.F]
		with open(nombre,"w") as f:
			f.write("inicial:{}\n".format(self.q0))
			f.write("finales:{}\n".format(",".join(F)))
			for kCar,dicQ in self.delta.items():
				for kQi,setQf in dicQ.items():
					for kQf in setQf:
						f.write("{}->{},{}\n".format(kQi,kQf,kCar))


	def siguiente_estado(self,edo_actual, entrada):
		if entrada in self.delta.keys():
			edos_dic = self.delta[entrada]
			return edos_dic[edo_actual] if edo_actual in edos_dic.keys() else set()
		return {}
	def acepta(self, cadena:str) -> bool:
		return self.acepta_aux(cadena, self.q0)

	def acepta_aux(self, cadena, edo):
		if len(cadena) == 0:
			next_edos = self.siguiente_estado(edo, "E")
			if len(next_edos) == 0:
				return edo in self.obtener_finales()
			else:
				ac_elipson  = [self.acepta_aux( cadena, edo_i ) for edo_i in next_edos]
				return True in ac_elipson
		
		caracter = cadena[0]
		next_edos = self.siguiente_estado(edo, caracter)
		ac_caracter = [self.acepta_aux( cadena[1:], edo_i ) for edo_i in next_edos]
		next_edos = self.siguiente_estado(edo, "E")
		ac_elipson  = [self.acepta_aux( cadena, edo_i ) for edo_i in next_edos]
		
		return True in ac_caracter or True in ac_elipson
			


	def generar_cadena(self) -> str:
		pass

		

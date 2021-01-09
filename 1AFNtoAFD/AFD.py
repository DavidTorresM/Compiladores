import functools 
from AF import ParserData, AF

class AFD(AF):
	"""docstring for AFN"""
	def __init__(self, Q, q0, sigma, F, delta ):
		super(AFD, self).__init__(Q, q0, sigma, F, delta)
		self.Q = Q
		self.q0 = q0
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
				self.delta[caracter][edoini] = [ qf for qi,qf,z in caract if qi == edoini ][0]
	
	def guardar_en(self, nombre:str):
		F = [str(i) for i in self.F]
		with open(nombre,"w") as f:
			f.write("inicial:{}\n".format(self.q0))
			f.write("finales:{}\n".format(",".join(F)))
			for kCar,dicQ in self.delta.items():
				for kQi,setQf in dicQ.items():
					f.write("{}->{},{}\n".format(kQi,setQf,kCar))


		
	def acepta(self, cadena:str) -> bool:
		return self.acepta_aux(cadena, self.q0)

	def acepta_aux(self, cadena, edo):
		if len(cadena)==0:
			return edo in self.F
		c = cadena[0]
		if c in self.delta.keys():
			if edo in self.delta[c].keys():
				results = self.acepta_aux(cadena[1:],self.delta[c][edo]) 
				return results
			else:
				return False
		else:
			return False


	def generar_cadena(self) -> str:
		pass

		

import sys
class ParserData:
	def load_data_source(self, file_name: str):
		q0 = -1
		F = [] 
		transiciones = []
		with open(file_name) as f:
			for line in f:
				qi,qf,s = self.extract_info(line)
				if s == "i" and qi==-1:
					q0 = int(line.split(":")[1])
				elif s == "f" and qi==-1:
					F = [int(i) for i in line.split(":")[1].split(',')]
				else:
					transiciones.append((qi,qf,s))

		return (q0,F,transiciones)

	def extract_info(self, line: str) -> (int,int,str):
		inicial = final = -1
		if line.startswith("inicial"):
			simbolo = "i"
		elif line.startswith("final"):
			simbolo = "f"
		else:
			aux = line.split(",")
			inicial, final = aux[0].split("->")
			inicial = int(inicial);final = int(final);
			simbolo = aux[1].replace("\n","")
		return inicial, final, simbolo





class AF(object):
	"""Automata finito"""
	def __init__(self, Q, q0, sigma, F, delta ):
		super(AF, self).__init__()
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
		#loader = ParserData()
		#(q0, F, tra) = loader.load_data_source(nombre)
		pass
		
	def acepta(self, cadena:str) -> bool:
		pass

	def guardar_en(self, nombre:str):
		pass

	def generar_cadena(self) -> str:
		pass

	def agregar_transicion(self, inicio:int, fin:int, simbolo:str):
		self.sigma.add(simbolo)
		if simbolo in self.delta.keys():
			subtabla = self.delta[simbolo]
			if inicio in subtabla.keys():
				subtabla[inicio] |= { fin }
			else:
				subtabla[inicio] = { fin }
		else:
			self.delta[simbolo] = {}

			self.delta[simbolo][inicio] = { fin }

	def eliminar_transicion(self, inicio:int, fin:int, simbolo:str):
		if simbolo in self.delta.keys():
			subtabla = self.delta[simbolo]
			if inicio in subtabla.keys():
				subtabla[inicio].remove( fin )
				if subtabla[inicio] == set():
					del subtabla[inicio]

	def establecer_inicial(self, estado:int):
		self.q0 = estado

	def establecer_final(self, estado:int):
		self.F = [estado]

	def establecer_finales(self, estado:[int]):
		self.F = estado

	def esAFN(self) -> bool:
		for kCar,dicQ in self.delta.items():
			for kQi,dicQf in dicQ.items():
				if len(dicQf) >= 2:
					return True
		return 'E' in self.sigma

	def esAFD(self) -> bool:
		return not self.esAFN()

	def obtener_inicial(self) -> int:
		return self.q0

	def obtener_final(self) -> int:
		return self.F[0]

	def obtener_finales(self) -> [int]:
		return self.F

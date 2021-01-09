
import sys,os,re
sys.path.append("../1AFNtoAFD/")

import functools 
from AF import ParserData, AF

class AFN(AF):
	"""docstring for AFN"""
	def __init__(self, Q, q0, sigma, F, delta ):
		super(AFN, self).__init__(Q, q0, sigma, F, delta)
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


		
	def acepta(self, cadena:str) -> bool:
		return self.acepta_aux(cadena, self.q0)

	def acepta_aux(self, cadena, edo):
		if len(cadena)==0:
			return edo in self.F
		c = cadena[0]
		if c in self.delta.keys():
			if edo in self.delta[c].keys():
				results = [self.acepta_aux(cadena[1:],siguiente) 
				for siguiente in self.delta[c][edo]]
				return functools.reduce(lambda x,y: x or y,results)
			else:
				return False
		else:
			return False


	def generar_cadena(self) -> str:
		pass

	def operar(self,operador,operandos):

	def convertir(self, expresion_regular:str ):
		er_pos = self.convertir_posfija(expresion_regular)
		pila = []
		for car in er_pos:
			if re.match(r"[a-z0-9]$",car) != None: #operando
				pila.append(car)
			else:
				if car == "*" or car == "+" or :#unario
					operando = pila.pop()
					rs = self.operar(car,(operando,))
				else:#binario
					operando1 = pila.pop()
					operando2 = pila.pop()
					rs = self.operar(car,(operando2,operando1))
				pila.append(rs)



	def proces_cadena(self,cadena):
		i = 0; j = 0
		cadFinal = []
		for i in range(1,len(cadena)):
			cadFinal.append(cadena[j])
			cadenita = cadena[j]+cadena[i]
			if re.match(r"[a-z]{2}|[\*\+][a-z\(]|\)[a-z\(]",cadenita) != None: #concatenar
				cadFinal.append(".")
			j += 1
		return "".join(cadFinal)+cadena[-1]
	def convertir_posfija(self, cadena:str) -> str:
		cadena = self.proces_cadena(cadena)
		pila = []; postfija = []
		for c in cadena:
			#print("Pila: ",pila)
			if c == "(":
				pila.append(c)
			else:
				if c == ")":#Parentesis quitar pila 
					while(pila[-1] != '('):
						postfija.append(pila.pop())
					pila.pop()
				elif re.match(r"[a-z0-9]$",c) != None: # operando
					postfija.append(c)
				else:#operador
					desapila = True
					while desapila:
						opeCima = ' '
						if not len(pila) == 0:
							opeCima = pila[-1]
							if len(pila) == 0 or self.prioridad_fuera(c)>self.prioridad_dentro(opeCima): 
								pila.append(c)
								desapila = False
							elif self.prioridad_fuera(c) <= self.prioridad_dentro(opeCima):
								postfija.append(pila.pop())
						else:
							pila.append(c)
							desapila = False
		while(len(pila) > 0):
			postfija.append(pila.pop())
		return "".join(postfija)

	def prioridad_dentro(self,caracter):
		dic = {"*":3,"+":2,".":2,"|":1,"(":0}
		return dic[caracter]
	def prioridad_fuera(self,caracter):
		dic = {"*":4,"+":2,".":2,"|":1,"(":5}
		return dic[caracter]


	def envaluar_posfija(self, cadena:str):
		pass

		





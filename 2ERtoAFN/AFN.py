
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



	def agregar_transicion(self, inicio:int, fin:int, simbolo:str):
		if self.Q == {} or self.Q == []  or self.Q == None:
			self.Q = set()
			self.Q.add(inicio); 
			self.Q.add(fin);
		else:
			if not inicio in self.Q:
				self.Q.add(inicio)
			if not fin in self.Q:
				self.Q.add(fin)
		super().agregar_transicion(inicio,fin,simbolo)






	def operar(self,operador,afns):
		if operador == "*":
			self.cerradura_kleen(afns[0])
		elif operador == "+":
			self.cerradura_positiva(afns[0])
		elif operador == "|":
			self.union(afns[0],afns[1])
		elif operador == ".":
			self.concatenar(afns[0],afns[1])

	def cerradura_kleen(self, afn):
		afn.agregar_transicion(afn.obtener_final,afn.obtener_inicial,'E')
		siguiente1 = max(afn.Q) + 1
		afn.agregar_transicion(afn.obtener_final,siguiente1,'E')
		siguiente2 = max(afn.Q) + 1
		afn.agregar_transicion(siguiente2,afn.obtener_inicial,'E')
		afn.establecer_inicial(siguiente2)
		afn.establecer_final(siguiente1)
		afn.agregar_transicion(afn.obtener_inicial,afn.obtener_final,'E')


	def cerradura_positiva(self, afn):
		afn.agregar_transicion(afn.obtener_final,afn.obtener_inicial,'E')
		siguiente1 = max(afn.Q) + 1
		afn.agregar_transicion(afn.obtener_final,siguiente1,'E')
		siguiente2 = max(afn.Q) + 1
		afn.agregar_transicion(siguiente2,afn.obtener_inicial,'E')
		afn.establecer_inicial(siguiente2)
		afn.establecer_final(siguiente1)

	def union(self, afn1, afn2):
		pass

	def juntar_edos(self, afn1, afn2):
		#change keys 
		qf = afn1.obtener_final()
		qi = afn2.q0

		for carac,Qdic in afn2.delta.items():
			if qi in Qdic.keys():
				diccionario = Qdic[qi].copy()
				del Qdic[qi]
				afn2.delta[carac][qf] = diccionario

		for carac,Qdic in afn2.delta.items():
			for Qik,Qfset in Qdic.items():
				if qi in Qfset:
					Qfset.remove(qi)
					Qfset.add(qf)
		


	def concatenar(self, afn1, afn2):
		#Sumamos un offset a la funcion de transicion del 
		#automata 2
		#cambiar q0 por qf
		self.juntar_edos(afn1,afn2)
		newDelta = self.map_delta(afn2.delta,offset = max(afn1.Q))
		d1Final = self.unir_delta(afn1.delta,newDelta)
		return d1Final

	def unir_delta(self,d1,d2):
		#Unir delta
		s1 = set(d1.keys());s2 = set(d2.keys())
		#Caracteres que hacen falta para copiarlos
		addCars = s2.difference(s1)
		for car in addCars:
			d1[car] = d2[car].copy()
		#caracteres que ya hay solo hay que agregarlos
		intersecCars = s1 & s2
		for car in intersecCars:
			d1[car].update(d2[car])
		return d1


	def map_delta(self, delta, offset):
		#copiar delta con un aumento en el offset
		newDelta = {}
		for Cak,Qdic in delta.items():
			newDelta[Cak] = {}
			for Qik, QfvSet in Qdic.items():
				newDelta[Cak][Qik+offset] = set(map(lambda x: x+offset,QfvSet)) 
		return newDelta





















	def create_afn(self, init, fin, caracter):
		anf = AFN(None,None,None,None,None)
		anf.agregar_transicion(init, fin, caracter)
		anf.establecer_inicial(init)
		anf.establecer_final(fin)
		return anf

	def convertir(self, expresion_regular:str ):
		er_pos = self.convertir_posfija(expresion_regular)
		pila = []
		for car in er_pos:
			if re.match(r"[a-z0-9]$",car) != None: #operando
				pila.append(self.create_afn(1,2,car))
			else:
				if car == "*" or car == "+":#unario
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


		





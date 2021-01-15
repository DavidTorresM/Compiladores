
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
			return edo in self.obtener_finales()
		caracter = cadena[0]
		acepto_caracter = False
		acepto_elipson = False
		next_edo = self.siguiente_estado(edo, caracter)
		for edo_i in next_edo:
			acepto_caracter = self.acepta_aux( cadena[1:], edo_i )
		next_edo = self.siguiente_estado(edo, "E")
		for edo_i in next_edo:
			acepto_elipson  = self.acepta_aux( cadena, edo_i )
		return acepto_caracter or acepto_elipson
			


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
			rs = afns[0]
		elif operador == "+":
			self.cerradura_positiva(afns[0])
			rs = afns[0]
		elif operador == "|":
			self.union(afns[0],afns[1])
			rs = afns[0]
		elif operador == ".":
			self.concatenar(afns[0],afns[1])
			rs = afns[0]
		return rs




	def cerradura_kleen(self, afn):
		afn.agregar_transicion(afn.obtener_final(),afn.obtener_inicial(),'E')
		siguiente1 = max(afn.Q) + 1
		afn.agregar_transicion(afn.obtener_final(),siguiente1,'E')
		siguiente2 = max(afn.Q) + 1
		afn.agregar_transicion(siguiente2,afn.obtener_inicial(),'E')
		afn.establecer_inicial(siguiente2)
		afn.establecer_final(siguiente1)
		afn.agregar_transicion(afn.obtener_inicial(),afn.obtener_final(),'E')


	def cerradura_positiva(self, afn):
		afn.agregar_transicion(afn.obtener_final(),afn.obtener_inicial(),'E')
		siguiente1 = max(afn.Q) + 1
		afn.agregar_transicion(afn.obtener_final(),siguiente1,'E')
		siguiente2 = max(afn.Q) + 1
		afn.agregar_transicion(siguiente2,afn.obtener_inicial(),'E')
		afn.establecer_inicial(siguiente2)
		afn.establecer_final(siguiente1)



	"""Realiza la union de dos afn"""
	def union(self, afn1, afn2):
		siguiente = max(afn1.Q)+1
		afn1.agregar_transicion(afn1.obtener_final(),siguiente,'E')
		afn1.establecer_final(siguiente)
		#print("trnsicion 1",afn1.delta,"q0:",afn1.q0,"qf:",afn1.F[0])

		siguiente = max(afn1.Q)+1
		afn1.agregar_transicion(siguiente,afn1.obtener_inicial(),'E')
		afn1.establecer_inicial(siguiente)
		#print("trnsicion 2",afn1.delta,"q0:",afn1.q0,"qf:",afn1.F[0])


		afn1.agregar_transicion(max(afn1.Q),max(afn1.Q)+1,'E')

		fin_aux = afn1.obtener_final()
		afn1.establecer_final(max(afn1.Q))
		#print("sub trnsicion 2",afn1.delta,"q0:",afn1.q0,"qf:",afn1.F[0])

		afn1.concatenar(afn1,afn2)

		#print(afn1.delta)
		#print("concat:",afn1.delta,"q0:",afn1.q0,"qf:",afn1.F[0])

		afn1.agregar_transicion(afn1.obtener_final(), fin_aux, 'E')
		afn1.establecer_final(fin_aux)


		#print(afn1.delta)
		#print("final:",afn1.delta,"q0:",afn1.q0,"qf:",afn1.F[0])


	def sumar_offset_grafo(self, afn2, offset):
		afn2.establecer_final(afn2.obtener_final() + offset)
		afn2.establecer_inicial(afn2.obtener_inicial() + offset)
		d2 = afn2.delta
		delta = {}
		for car, edosDic in d2.items():
			delta[car] = {}
			for Qi,setQf in edosDic.items():
				setQf_process = set(map(lambda x:x+offset,setQf))
				delta[car][Qi+offset] = setQf_process
		afn2.delta = delta

	def juntar_afns(self, afn1, afn2):
		d1 = afn1.delta
		d2 = afn2.delta
		s1 = set(d1.keys())
		s2 = set(d2.keys())
		#Copiamos Los caracteres que faltan
		caracteres_agregar = s2.difference(s1)
		for caracter in caracteres_agregar:
			d1[caracter] = d2[caracter].copy()
		#Juntamos los caracteres ya repetidos
		caracteres_juntar = s2.intersection(s1)
		for caracter in caracteres_juntar:
			Qi1 = set(d1[caracter].keys())
			Qi2 = set(d2[caracter].keys())
			interseccion = Qi1.intersection(Qi2)
			if len(interseccion) != 0:#intersectan
				for Qi in interseccion:
					d1[caracter][Qi].update(d2[caracter][Qi])
			else:#no interseccion
				d1[caracter].update(d2[caracter])

	def cambiar_edos(self, afn ,val1, val2):
		#Cambiar val1 por val2 de las tablas
		delta = afn.delta
		for car,dicQi in delta.items():
			set_keys_qi = set(dicQi.keys())
			if val1 in set_keys_qi: #Cuando esta en las keys
				valores = delta[car][val1].copy()
				del delta[car][val1]
				if val2 in delta[car].keys():#unimos
					delta[car][val2] |= valores
				else:#creamos
					delta[car][val2] = valores
			else:#Cuando esta en los valores 
				for qi,qfset in dicQi.items():
					if val1 in qfset:
						qfset.remove(val1)
						qfset.add(val2)




	def concatenar(self, afn1, afn2):
		##Sumar offset al afn2
		self.sumar_offset_grafo(afn2, offset = max(afn1.Q))
		##Juntar delta afn2 con afn1
		self.juntar_afns(afn1, afn2)
		##Hacer cambios en en las keys 
		#El final de afn1 = inicial de afn2
		fin_af1 = afn1.obtener_final()
		ini_af2 = afn2.obtener_inicial()
		#print("cambiar: ", afn1.delta)
		#print("af1: ",fin_af1,"af2: ",ini_af2)
		self.cambiar_edos(afn1,fin_af1,ini_af2)
		#print("despues cambiar: ", afn1.delta)
		afn1.establecer_final(afn2.obtener_final())

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
		return pila.pop()

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
			##print("Pila: ",pila)
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


		





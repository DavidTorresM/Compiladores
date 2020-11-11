def get_automata():
	aut = []
	aut.append([None,None,None,None,None]) 
	aut.append([None,None,None,None,{2}]) 
	aut.append([None,None,None,None,{3,7}]) 
	aut.append([{4},None,None,None,None]) 
	aut.append([None,{5},None,None,None]) 
	aut.append([None,None,None,None,{6}])
	aut.append([None,None,None,None,{2}])
	aut.append([None,None,{8},None,None]) 
	aut.append([None,None,None,None,{9,11}]) 
	aut.append([None,None,None,{10},None]) 
	aut.append([None,None,None,None,{9,11}]) 
	aut.append([None,None,None,None,{6}]) 
	return aut

visitados = set()
def elipson(AF,edo):
	global visitados
	visitados = set()
	rs = elipson_aux(AF,edo)
	return rs
def elipson_aux(AF,edo):
	global visitados
	edos = {edo}
	visitados |= {edo}
	aux = AF[edo][len(AF[0])-1]
	if aux == None:
		return edos
	aux = aux - visitados
	for edo_i in aux: #Expandimos los nodos
		edos |= elipson_aux(AF,edo_i)
	return edos


def get_kernel():
	pass

def dp_mover(AF):
	dic = { i:{} for i in range(len(AF[0])-1)}
	for simbolo in range(len(AF[0])-1):
		for edo_i in range(1,len(AF)):
			if AF[edo_i][simbolo] != None:
				dic[simbolo][edo_i] = AF[edo_i][simbolo]
	return dic


def mover(AF,T,a):
	pass
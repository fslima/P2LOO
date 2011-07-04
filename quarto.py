#-*- coding:utf-8 -*-

class Quarto(object):
	vldiaria = 0.00
	lista = []
	def __init__(self, n, t):
		self.num = n
		self.tipo = t
		self.situacao = 'Livre'
		if t == 'Simples':
			self.vldiaria = 90.00
		if t == 'Casal':
			self.vldiaria = 150.00
		if t == 'Master':
			self.vldiaria = 260.00

	def __repr__(self):
		return "Numero: "+str(self.num)+" | Tipo: "+str(self.tipo)+" | Situacao: "+str(self.situacao)+" | Diaria: "+str(self.vldiaria)

	def cadQuarto(self, n, t):
		Quarto.lista.append(Quarto(n, t))

	def buscarQuarto(self, q, n):
		existe = False
		num = 9999
		for i in range(0, len(q.lista)):
			if q.lista[i].num == n:
				existe = True
				num = i
		if existe == True:
			return q.lista[num]
		else:
			return False

	def setSituacao(self, q, n, situacao):
		if self.buscarQuarto(q, n) == False:
			return "Quarto não Cadastrado"
		else:
			self.buscarQuarto(q, n).situacao = situacao

	def listarQuartos(self, q):
		listaDeQuartos = []
		for i in range(0, len(q.lista)):
			listaDeQuartos.append(q.lista[i])
		return listaDeQuartos

	def listarQuartosPorTipo(self, q, tp):
		listaDeQuartos = []
		for i in range(0, len(q.lista)):
			if tp == q.lista[i].tipo:
				listaDeQuartos.append(q.lista[i])
		return listaDeQuartos

	def listarQuartosPorSituacao(self, q, situacao):
		listaDeQuartos = []
		for i in range(0, len(q.lista)):
			if situacao == q.lista[i].situacao:
				listaDeQuartos.append(q.lista[i])
		return listaDeQuartos

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

	def listarQuartos(self, q):
		for i in range(0, len(q.lista)):
			print q.lista[i]

	def listarQuartosPorTipo(self, q, tp):
		for i in range(0, len(q.lista)):
			if tp == q.lista[i].tipo:
				print q.lista[i]

	def listarQuartosPorSituacao(self, q, situacao):
		for i in range(0, len(q.lista)):
			if situacao == q.lista[i].situacao:
				print q.lista[i]

	def buscarQuarto(self, q, n):
		existe = False
		for i in range(0, len(q.lista)):
			if q.lista[i].num == n:
				existe = True
		if existe == True:
			return q.lista[i]
		else:
			return False

	def existeQuarto(self, q, n, t):
		existe = False
		for i in range(0, len(q.lista)):
			if q.lista[i].num == n:
				existe = True
		if existe == True:
			self.cadQuarto(n, t)
		else:
			print ""
			print "Quarto ja Cadastrado"

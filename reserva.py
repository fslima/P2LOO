#-*- coding:utf-8 -*-

from datetime import date
from cliente import Cliente
from quarto import Quarto

class Reserva(object):
	num = 0
	lista = []
	def __init__(self, q, c, di, df):
		Reserva.num += 1
		self.num = Reserva.num
		self.cliente = c
		self.quarto = q
		self.dtinicio = di
		self.dtfim = df

	def __repr__(self):
		return "Nº Reserva: "+str(self.num)+" | Quarto: "+str(self.quarto.num)+" | Cliente: "+str(self.cliente.nome)+" | Data de Chegada: "+str(self.dtinicio)+" | Data de Saida: "+str(self.dtfim)

	def cadReserva(self, q, qn, c, cn, di, df):
		Reserva.lista.append(Reserva(q.buscarQuarto(q, qn), c.buscarCliente(c, cn), di, df))
		
	def existeReserva(self, r, q, qn, c, cn, di, df):
		existe = False
		for i in range(0, len(r.lista)):
			if q.buscarQuarto(q, qn) == False:
				print ""
				print "Quarto nao Cadastrado"
				existe = True
				break
			if c.buscarCliente(c, cn) == False:
				print ""
				print "Cliente nao Cadastrado"
				existe = True
				break
			if df <= di:
				print ""
				print "Data de Saida deve ser maior do que a Inicial"
				existe = True
				break
			if di <= date.today():
				print ""
				print "Data de Entrada deve ser superior a 24h"
				existe = True
				break
			if qn == r.lista[i].quarto.num and di >= r.lista[i].dtinicio and di <= r.lista[i].dtfim:
				print ""
				print "Já existe a seguinte reserva para esse Quarto:"
				print ""
				print r.lista[i]
				existe = True
				break
			if qn == r.lista[i].quarto.num and df >= r.lista[i].dtinicio and df <= r.lista[i].dtfim:
				print ""
				print "Já existe a seguinte reserva para esse Quarto:"
				print ""
				print r.lista[i]
				existe = True
				break
		if existe == True:
			print "Tente novamente"
		else:
			self.cadReserva(q, qn, c, cn, di, df)

	def cancelarReservas(self, r, nr):
		removido = False
		for i in range(0, len(r.lista)):
			if r.lista[i].num == nr:
				r.lista.remove(r.lista[i])
				removido = True
		if removido == True:
			print ""
			print ""
			print "Reserva Cancelada com Sucesso"
		else:
			print "A Reserva informada não Existe"

	def listarReservas(self, r):
		for i in range(0, len(r.lista)):
			print r.lista[i]

	def listarReservasPorData(self, r, di, df):
		for i in range(0, len(r.lista)):
			if di >= r.lista[i].dtinicio and di <= r.lista[i].dtfim:
				print r.lista[i]
			if df >= r.lista[i].dtinicio and df <= r.lista[i].dtfim:
				print r.lista[i]
				

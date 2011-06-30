#-*- coding:utf-8 -*-

from datetime import date
from cliente import Cliente
from quarto import Quarto

class Hospedagem(object):
	num = 0
	vlextra = 0.00
	lista = []
	def __init__(self, c, q, df):
		Hospedagem.num += 1
		self.num = Hospedagem.num
		self.cliente = c
		self.quarto = q
		self.dtinicio = date.today()
		self.dtfim = df
	
	def __repr__(self):
		return "Nº Hospedagem: "+str(self.num)+"Quarto: "+str(self.quarto.num)+" | Cliente: "+str(self.cliente.nome)+" | Data de Chegada: "+str(self.dtinicio)+" | Data de Saida: "+str(self.dtfim)+" | Valor Diaria: "+str(self.quarto.vldiaria)

	def checkIn(self, q, qn, c, cn, di, df):
		Reserva.lista.append(Reserva(q.buscarQuarto(q, qn), c.buscarCliente(c, cn), di, df))
		
	def listarReservas(self, r):
		for i in range(0, len(r.lista)):
			print r.lista[i]

	def numDeDiarias(self, di, df):
		dez = date(2011, 6, 30) - date(2011, 6, 20)
		cem = date(2011, 9, 28) - date(2011, 6, 20)
		diarias = df-di
		if diarias < dez:
			d = str(diarias)
			return int(d[0])
		if diarias >= dez and diarias < cem:
			d = str(diarias)
			return int(d[0]+d[1])
		if diarias >= cem:
			d = str(diarias)
			return int(d[0]+d[1]+d[2])






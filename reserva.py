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
		return "Nº Reserva: "+str(self.num)+" | Quarto: "+str(self.quarto.num)+" | Cliente: "+str(self.cliente.nome)+" | Data de Chegada: "+str(self.dtinicio.day)+"/"+str(self.dtinicio.month)+"/"+str(self.dtinicio.year)+" | Data de Saida: "+str(self.dtfim.day)+"/"+str(self.dtfim.month)+"/"+str(self.dtfim.year)

	def cadReserva(self, q, qn, c, cn, di, df):
		Reserva.lista.append(Reserva(q.buscarQuarto(q, qn), c.buscarCliente(c, cn), di, df))
		
	def validarReserva(self, r, q, qn, c, cn, di, df):
		aviso = ""
		existe = False
		reserva = None
		for i in range(0, len(r.lista)):
			if q.buscarQuarto(q, qn) == False:
				aviso = "Quarto nao Cadastrado"
				existe = True
				break
			if c.buscarCliente(c, cn) == False:
				aviso = "Cliente nao Cadastrado"
				existe = True
				break
			if df <= di:
				aviso = "Data de Saida deve ser maior do que a Inicial"
				existe = True
				break
			if di <= date.today():
				aviso = "Data de Entrada deve ser superior a 24h"
				existe = True
				break
			if qn == r.lista[i].quarto.num and di >= r.lista[i].dtinicio and di <= r.lista[i].dtfim:
				aviso = "Já existe a seguinte reserva para esse Quarto: \n\n"
				reserva = r.lista[i]
				existe = True
				break
			if qn == r.lista[i].quarto.num and df >= r.lista[i].dtinicio and df <= r.lista[i].dtfim:
				aviso = "Já existe a seguinte reserva para esse Quarto: \n\n"
				reserva = r.lista[i]
				existe = True
				break
			if qn == r.lista[i].quarto.num and di < r.lista[i].dtinicio and df > r.lista[i].dtfim:
				aviso = "Já existe a seguinte reserva para esse Quarto: \n\n"
				reserva = r.lista[i]
				existe = True
				break
		if existe == True:
			if reserva == None:
				return aviso
			else:
				return aviso+str(reserva)
		else:
			self.cadReserva(q, qn, c, cn, di, df)
			return "Reserva Cadastrada"

	def cancelarReserva(self, r, nr):
		removido = False
		for i in range(0, len(r.lista)):
			if r.lista[i].num == nr:
				r.lista.remove(r.lista[i])
				removido = True
				break
		if removido == True:
			return "\n\nReserva Cancelada com Sucesso"
		else:
			return "\n\nA Reserva informada não Existe"

	def listarReservas(self, r):
		listaDeReservas = []
		for i in range(0, len(r.lista)):
			listaDeReservas.append(r.lista[i])
		return listaDeReservas

	def listarReservasPorPeriodo(self, r, di, df):
		listaDeReservas = []
		for i in range(0, len(r.lista)):
			if di >= r.lista[i].dtinicio and di <= r.lista[i].dtfim:
				listaDeReservas.append(r.lista[i])
				break
			if df >= r.lista[i].dtinicio and df <= r.lista[i].dtfim:
				listaDeReservas.append(r.lista[i])
				break
			if di < r.lista[i].dtinicio and df > r.lista[i].dtfim:
				listaDeReservas.append(r.lista[i])
				break
		return listaDeReservas

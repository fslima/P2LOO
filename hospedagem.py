#-*- coding:utf-8 -*-

from datetime import date
from cliente import Cliente
from quarto import Quarto

class Hospedagem(object):
	num = 0
	vlextra = 0
	vltotal = 0
	situacao = 'Em Aberto'
	lista = []
	def __init__(self, q, c, df):
		Hospedagem.num += 1
		self.num = Hospedagem.num
		self.cliente = c
		self.quarto = q
		self.dtinicio = date.today()
		self.dtfim = df
	
	def __repr__(self):
		return "Nº Hospedagem: "+str(self.num)+" | Quarto: "+str(self.quarto.num)+" | Cliente: "+str(self.cliente.nome)+" | Data de Chegada: "+str(self.dtinicio.day)+"/"+str(self.dtinicio.month)+"/"+str(self.dtinicio.year)+" | Data de Saida: "+str(self.dtfim.day)+"/"+str(self.dtfim.month)+"/"+str(self.dtfim.year)+" | Valor Diaria do Quarto: "+str(self.quarto.vldiaria)+" | Valor Total: "+str(self.vltotal)

	def checkIn(self, q, qn, c, cn, df):
		c.setQtdHosp(c, cn)
		q.setSituacao(q, qn, 'Ocupado')
		Hospedagem.lista.append(Hospedagem(q.buscarQuarto(q, qn), c.buscarCliente(c, cn), df))
		
	def checkOut(self, h, hn, q, vlextra):
		desconto = 0
		vltotal = 0
		q.setSituacao(q, h.buscarHospedagem(h, hn).quarto.num, 'Livre')
		h.buscarHospedagem(h, hn).situacao = 'Encerrada'
		h.buscarHospedagem(h, hn).dtfim = date.today()
		h.buscarHospedagem(h, hn).vlextra = vlextra
		vltotal = ((self.numDeDiarias(h.buscarHospedagem(h, hn).dtinicio, h.buscarHospedagem(h, hn).dtfim) * h.buscarHospedagem(h, hn).quarto.vldiaria) + vlextra)
		if h.buscarHospedagem(h, hn).cliente.vip == 'S':
			desconto = vltotal / 10
		h.buscarHospedagem(h, hn).vltotal = vltotal - desconto
		return str(h.buscarHospedagem(h, hn)) +"\n\n Valor da(s) Diaria(s): "+str((self.numDeDiarias(h.buscarHospedagem(h, hn).dtinicio, h.buscarHospedagem(h, hn).dtfim) * h.buscarHospedagem(h, hn).quarto.vldiaria))+ " + Valor Frigobar: "+str(vlextra)+" - Desconto: "+str(desconto)+" = Valor Total: "+str(vltotal)
		
	def validarHospedagem(self, h, r, q, qn, c, cn, df):
		di = date.today()
		aviso = ""
		existe = False
		reserva = None
		for i in range(0, len(h.lista)):
			if q.buscarQuarto(q, qn) == False:
				aviso = "Quarto nao Cadastrado"
				existe = True
				break
			if q.buscarQuarto(q, qn).situacao == 'Ocupado':
				aviso = "Quarto Ocupado"
				existe = True
				break
			if c.buscarCliente(c, cn) == False:
				aviso = "Cliente nao Cadastrado"
				existe = True
				break
			if df <= di:
				aviso = "Data de Saida deve ser maior do que a de hoje"
				existe = True
				break
		for i in range(0, len(r.lista)):
			if qn == r.lista[i].quarto.num and di >= r.lista[i].dtinicio and di <= r.lista[i].dtfim:
				aviso = "Existe a seguinte reserva para esse Quarto: \n\n"
				reserva = r.lista[i]
				existe = True
				break
			if qn == r.lista[i].quarto.num and df >= r.lista[i].dtinicio and df <= r.lista[i].dtfim:
				aviso = "Existe a seguinte reserva para esse Quarto: \n\n"
				reserva = r.lista[i]
				existe = True
				break
			if qn == r.lista[i].quarto.num and di < r.lista[i].dtinicio and df > r.lista[i].dtfim:
				aviso = "Existe a seguinte reserva para esse Quarto: \n\n"
				reserva = r.lista[i]
				existe = True
				break
		if existe == True:
			if reserva == None:
				return aviso
			else:
				return aviso+str(reserva)
		else:
			self.checkIn(q, qn, c, cn, df)
			return "Checkin Concluido"
	
	def buscarHospedagem(self, h, n):
		existe = False
		num = 9999
		for i in range(0, len(h.lista)):
			if h.lista[i].num == n:
				existe = True
				num = i
		if existe == True:
			return h.lista[num]
		else:
			return False
	
	def cancelarHospedagem(self, h, n):
		removido = False
		for i in range(0, len(h.lista)):
			if h.lista[i].num == n:
				h.lista.remove(h.lista[i])
				removido = True
				break
		if removido == True:
			return "\n\nHospedagem Cancelada com Sucesso"
		else:
			return "\n\nA Hospedagem informada não Existe"


	def listarHospedagens(self, h):
		listaDeHospedagens = []
		for i in range(0, len(h.lista)):
			listaDeHospedagens.append(h.lista[i])
		return listaDeHospedagens

	def listarHospedagensPorSituacao(self, h, situacao):
		listaDeHospedagens = []
		for i in range(0, len(h.lista)):
			if situacao == h.lista[i].situacao:
				listaDeHospedagens.append(h.lista[i])
		return listaDeHospedagens

	def numDeDiarias(self, di, df):
		zero = date(2011, 6, 30) - date(2011, 6, 30) 
		dez = date(2011, 6, 30) - date(2011, 6, 20)
		cem = date(2011, 9, 28) - date(2011, 6, 20)
		diarias = df-di
		if diarias == zero:
			return 1
		if diarias < dez:
			d = str(diarias)
			return int(d[0])
		if diarias >= dez and diarias < cem:
			d = str(diarias)
			return int(d[0]+d[1])
		if diarias >= cem:
			d = str(diarias)
			return int(d[0]+d[1]+d[2])






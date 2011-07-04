#-*- coding:utf-8 -*-

from datetime import date
from cliente import Cliente
from quarto import Quarto
from reserva import Reserva
from hospedagem import Hospedagem

class Hotel(object):

	def menu(self):	
		self.c = Cliente(None, 0, None)
		self.q = Quarto(0, None)
		self.r = Reserva(None, None, None, None)
		self.h = Hospedagem(None, None, None)
		op=0
		while op != 5:
			print ""
			print ""
			print "Hotel LOO-IFF"
			print ""
			print "1 - Clientes"
			print "2 - Quartos"
			print "3 - Reservas"
			print "4 - Hospedagens"
			print "5 - Sair"
			op = input("Digite sua opção: ")
			if op == 1:
				self.menuClientes()
			if op == 2:
				self.menuQuartos()
			if op == 3:
				self.menuReservas()
			if op == 4:
				self.menuHospedagens()

	def menuClientes(self):
		op=0
		while op != 3:
			print ""
			print ""
			print "Menu de Clientes"
			print ""
			print "1 - Cadastrar Cliente"
			print "2 - Relatórios de Clientes"
			print "3 - Voltar"
			op = input("Digite sua opção: ")
			if op == 1:
				self.cadCli()
			if op == 2:
				self.menuRelCli()

	def cadCli(self):
		print ""
		print ""
		print "Cadastros de Clientes"
		print ""
		nome = raw_input("Nome: ")
		cpf = raw_input("CPF: ")
		tel = raw_input("Telefone: ")
		self.c.cadCli(nome, cpf, tel)
			
	def menuRelCli(self):
		op=0
		while op != 3:
			print ""
			print ""
			print "Relatorios de Clientes"
			print "";
			print "1 - Lista Cliente"
			print "2 - Lista de Clientes VIPs"
			print "3 - Voltar";
			op = input("Digite sua opção: ")
			if op == 1:
				self.relCli()
			if op == 2:
				self.relCliVip()

	def relCli(self):
		print ""
		print "Lista de Clientes"
		print "";
		for i in range(0, len(self.c.lista)):
			print self.c.listarClientes(self.c)[i]

	def relCliVip(self):
		print ""
		print "Lista de Clientes VIP"
		print "";
		for i in range(0, len(self.c.listarClientesVip(self.c))):
			print self.c.listarClientesVip(self.c)[i]

	def menuQuartos(self):
		op=0
		while op != 3:
			print ""
			print ""
			print "Menu de Quartos"
			print ""
			print "1 - Cadastrar Quarto"
			print "2 - Relatórios de Quartos"
			print "3 - Voltar"
			op = input("Digite sua opção: ")
			if op == 1:
				self.cadQuarto()
			if op == 2:
				self.menuRelQuartos()

	def cadQuarto(self):
		tp = 0
		print ""
		print ""
		print "Cadastros de Quartos"
		print ""
		num = input("Numero: ")
		while tp != 1 and tp != 2 and tp != 3:
			print "Tipo do Quarto:"
			print "1 - Simples"
			print "2 - Casal"
			print "3 - Master"
			tp = input("Escolha o Tipo do Quarto: ")
			if tp == 1:
				tipo = 'Simples'
			if tp == 2:
				tipo = 'Casal'
			if tp == 3:
				tipo = 'Master'
		print ""
		print self.q.cadQuarto(num, tipo)

	def menuRelQuartos(self):
		op=0
		while op != 4:
			print ""
			print ""
			print "Relatorios de Quartos"
			print "";
			print "1 - Lista Quartos"
			print "2 - Lista de Quartos por Tipo"
			print "3 - Lista de Quartos por Ocupacao";
			print "4 - Voltar";
			op = input("Digite sua opção: ")
			if op == 1:
				self.relQuartos()
			if op == 2:
				self.relQuartosPorTipo()
			if op == 3:
				self.relQuartosPorSituacao()

	def relQuartos(self):
		print ""
		print "Lista de Quartos"
		print "";
		for i in range(0, len(self.q.lista)):
			print self.q.listarQuartos(self.q)[i]

	def relQuartosPorTipo(self):
		tp = 0
		print ""
		print "Lista de Quartos por Tipo"
		print ""
		while tp != 1 and tp != 2 and tp != 3:
			print "Tipo do Quarto:"
			print "1 - Simples"
			print "2 - Casal"
			print "3 - Master"
			tp = input("Escolha o Tipo do Quarto: ")
			if tp == 1:
				tipo = 'Simples'
			if tp == 2:
				tipo = 'Casal'
			if tp == 3:
				tipo = 'Master'
		print ""
		print "Lista de Quartos (Tipo %s)" %tipo
		print ""
		for i in range(0, len(self.q.listarQuartosPorTipo(self.q, tipo))):
			print self.q.listarQuartosPorTipo(self.q, tipo)[i]

	def relQuartosPorSituacao(self):
		sit = 0
		print ""
		print "Lista de Quartos por Ocupacao"
		print ""
		while sit != 1 and sit != 2:
			print "Tipo do Quarto:"
			print "1 - Livre"
			print "2 - Ocupado"
			sit = input("Livre ou Ocupado? ")
			if sit == 1:
				situacao = 'Livre'
			if sit == 2:
				situacao = 'Ocupado'
		print ""
		print "Lista de Quartos "+situacao+"s"
		print ""
		for i in range(0, len(self.q.listarQuartosPorSituacao(self.q, situacao))):
			print self.q.listarQuartosPorSituacao(self.q, situacao)[i]


	def menuReservas(self):
		op=0
		while op != 4:
			print ""
			print ""
			print "Menu de Reservas"
			print ""
			print "1 - Cadastrar Reserva"
			print "2 - Relatórios de Reservas"
			print "3 - Cancelamento de Reserva"
			print "4 - Voltar"
			op = input("Digite sua opção: ")
			if op == 1:
				self.cadReserva()
			if op == 2:
				self.menuRelReservas()
			if op == 3:
				self.menuCancelarReservas()
	
	def cadReserva(self):
		print ""
		print ""
		print "Cadastros de Reservas"
		print ""
		nq = input("Nº do Quarto: ")
		nc = input("Codigo do Cliente: ")
		chegada = raw_input("Data da Chegada(ddMMaaaa): ")
		saida = raw_input("Data da Saída(ddMMaaaa): ")
		di = date(int(chegada[4:8]), int(chegada[2:4]), int(chegada[:2]))
		df = date(int(saida[4:8]), int(saida[2:4]), int(saida[:2]))
		print ""
		print self.r.validarReserva(self.r, self.q, nq, self.c, nc, di, df)

	def menuCancelarReservas(self):
		print ""
		print ""
		print "Cancelamento de Reservas"
		print ""
		nr = input("Nº da Reserva: ")
		print self.r.cancelarReserva(self.r, nr)

	def menuRelReservas(self):
		op=0
		while op != 3:
			print ""
			print ""
			print "Relatorios de Reservas"
			print "";
			print "1 - Lista Geral de Reservas"
			print "2 - Lista de Reservas por Data"
			print "3 - Voltar";
			op = input("Digite sua opção: ")
			if op == 1:
				self.relReservas()
			if op == 2:
				self.relReservasPorData()

	def relReservas(self):
		print ""
		print "Lista Geral de Reservas"
		print ""
		for i in range(0, len(self.r.listarReservas(self.r))):
			print self.r.listarReservas(self.r)[i]

	def relReservasPorData(self):
		print ""
		print "Lista de Reservas por Periodo"
		print ""
		chegada = raw_input("Data da Chegada(ddMMaaaa): ")
		saida = raw_input("Data da Saída(ddMMaaaa): ")
		di = date(int(chegada[4:8]), int(chegada[2:4]), int(chegada[:2]))
		df = date(int(saida[4:8]), int(saida[2:4]), int(saida[:2]))
		print ""
		print "Lista de Reservas por Periodo"
		print ""
		for i in range(0, len(self.r.listarReservasPorPeriodo(self.r, di, df))):
			print self.r.listarReservasPorPeriodo(self.r, di, df)[i]

	
	def menuHospedagens(self):
		op=0
		while op != 5:
			print ""
			print ""
			print "Menu de Hospedagens"
			print ""
			print "1 - CheckIn"
			print "2 - CheckOut"
			print "3 - Relatórios de Hospedagens"
			print "4 - Cancelamento de Hospedagens"
			print "5 - Voltar"
			op = input("Digite sua opção: ")
			if op == 1:
				self.checkIn()
			if op == 2:
				self.checkOut()
			if op == 3:
				self.menuRelHospedagens()
			if op == 4:
				self.menuCancelarHospedagens()
	
	def checkIn(self):
		print ""
		print ""
		print "CheckIn"
		print "Quartos Livres"
		print self.q.listarQuartosPorSituacao(self.q, 'Livre')
		print ""
		nq = input("Nº do Quarto: ")
		nc = input("Codigo do Cliente: ")
		saida = raw_input("Data da Saída(ddMMaaaa): ")
		df = date(int(saida[4:8]), int(saida[2:4]), int(saida[:2]))
		print ""
		print self.h.validarHospedagem(self.h, self.r, self.q, nq, self.c, nc, df)

	def checkOut(self):
		print ""
		print ""
		print "CheckOut"
		print "Hospedagens Em Aberto"
		print self.h.listarHospedagensPorSituacao(self.h, 'Em Aberto')
		print ""
		n = input("Nº da Hospedagem: ")
		vf = input("Valor Gasto no Frigobar: ")
		print ""
		print self.h.checkOut(self.h, n, self.q, vf)

	def menuCancelarHospedagens(self):
		print ""
		print ""
		print "Cancelamento de Hospedagem"
		print ""
		n = input("Nº da Hospedagem: ")
		print self.h.cancelarReserva(self.h, n)

	def menuRelHospedagens(self):
		op=0
		while op != 3:
			print ""
			print ""
			print "Relatorios de Hospedagens"
			print "";
			print "1 - Lista Geral de Hospedagens"
			print "2 - Lista de Reservas por Situacao"
			print "3 - Voltar";
			op = input("Digite sua opção: ")
			if op == 1:
				self.relHospedagens()
			if op == 2:
				self.relHospedagensPorSituacao()

	def relHospedagens(self):
		print ""
		print "Lista Geral de Hospedagens"
		print ""
		for i in range(0, len(self.h.listarHospedagens(self.h))):
			print self.h.listarHospedagens(self.h)[i]

	def relHospedagensPorSituacao(self):
		sit = 0
		print ""
		print "Lista de Hospedagens por Status"
		print ""
		while sit != 1 and sit != 2:
			print "Status:"
			print "1 - Em Aberto"
			print "2 - Encerrado"
			sit = input("Livre ou Ocupado? ")
			if sit == 1:
				situacao = 'Em Aberto'
			if sit == 2:
				situacao = 'Encerrada'
		print ""
		print "Lista de Hoespedagens "+situacao
		print ""
		for i in range(0, len(self.h.listarHospedagensPorSituacao(self.h, situacao))):
			print self.h.listarHospedagensPorSituacao(self.h, situacao)[i]


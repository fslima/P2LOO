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
		op=0
		while op != 4:
			print ""
			print ""
			print "Hotel LOO-IFF"
			print ""
			print "1 - Cadastro"
			print "2 - Relatorios"
			print "3 - Cancelamentos"
			print "4 - Sair"
			op = input("Digite sua opção: ")
			if op == 1:
				self.cadastro()
			if op == 2:
				self.relatorios()
			if op == 3:
				self.cancelamentos()

	def cadastro(self):
		op=0
		while op != 5:
			print ""
			print ""
			print "Menu de Cadastros"
			print ""
			print "1 - Cliente"
			print "2 - Quarto"
			print "3 - Reserva"
			print "4 - Hospedagem"
			print "5 - Voltar"
			op = input("Digite sua opção: ")
			if op == 1:
				self.cadCli()
			if op == 2:
				self.cadQuarto()
			if op == 3:
				self.cadReserva()

	def relatorios(self):
		op=0
		while op != 5:
			print ""
			print ""
			print "Menu de Relatorios"
			print ""
			print "1 - Cliente"
			print "2 - Quarto"
			print "3 - Reserva"
			print "4 - Hospedagem"
			print "5 - Voltar"
			op = input("Digite sua opção: ")
			if op == 1:
				self.menuRelCli()
			if op == 2:
				self.menuRelQuartos()
			if op == 3:
				self.menuRelReservas()
			if op == 4:
				self.menuRelReservas()

	def cancelamentos(self):
		op=0
		while op != 3:
			print ""
			print ""
			print "Menu de Cancelamentos"
			print ""
			print "1 - Reserva"
			print "2 - Hospedagem"
			print "3 - Voltar"
			op = input("Digite sua opção: ")
			if op == 1:
				self.menuCancelarReservas()
			if op == 2:
				self.menuCancelarHospedagens()

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
		for i in range(0, len(self.c.lista)):
			print self.c.listarClientesVip(self.c)[i]
	
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
		self.q.cadQuarto(num, tipo)

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
		self.q.listarQuartos(self.q)

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
		self.q.listarQuartosPorTipo(self.q, tipo)

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
		self.q.listarQuartosPorSituacao(self.q, situacao)

	def cadReserva(self):
		print ""
		print ""
		print "Cadastros de Reservas"
		print ""
		nq = input("Nº do Quarto: ")
		nc = input("Codigo do Cliente: ")
		diai = input("Dia da Chegada: ")
		mesi = input("Mes da Chegada: ")
		anoi = input("Ano da Chegada: ")
		diaf = input("Dia da Saida: ")
		mesf = input("Mes da Saida: ")
		anof = input("Ano da Saida: ")
		di = date(anoi, mesi, diai)
		df = date(anof, mesf, diaf)
		self.r.existeReserva(self.r, self.q, nq, self.c, nc, di, df)

	def menuCancelarReservas(self):
		print ""
		print ""
		print "Cancelamento de Reservas"
		print ""
		nr = input("Nº da Reserva: ")
		self.r.cancelarReservas(self.r, nr)

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
		self.r.listarReservas(self.r)

	def relReservasPorData(self):
		print ""
		print "Lista de Reservas por Periodo"
		print ""
		diai = input("Dia da Chegada: ")
		mesi = input("Mes da Chegada: ")
		anoi = input("Ano da Chegada: ")
		diaf = input("Dia da Saida: ")
		mesf = input("Mes da Saida: ")
		anof = input("Ano da Saida: ")
		di = date(anoi, mesi, diai)
		df = date(anof, mesf, diaf)
		print ""
		print "Lista de Reservas por Periodo"
		print ""
		self.r.listarReservasPorData(self.r, di, df)

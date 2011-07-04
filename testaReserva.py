#-*- coding:utf-8 -*-

import unittest
from should_dsl import should, should_not

from datetime import date
from cliente import Cliente
from quarto import Quarto
from reserva import Reserva

class TestaReserva(unittest.TestCase):
	
	def setUp(self):
		self.c = Cliente('Thiago Neves', '12369978909', '2299019866')
		self.q = Quarto(202, 'Master')
		self.r = Reserva(self.q, self.c, date(2011, 10, 15), date(2011, 10, 20))

	def testaAinit(self):		
		self.r.num |should| equal_to(1)
		self.r.cliente.nome |should| equal_to('Thiago Neves')
		self.r.quarto.num |should| equal_to(202)
		self.r.dtinicio |should| equal_to(date(2011, 10, 15))
		self.r.dtfim |should| equal_to(date(2011, 10, 20))
		self.r = Reserva(self.q, Cliente('Ronaldinho Gaucho', '98765478909', '2167549876'), date(2011, 10, 22), date(2011, 10, 29))
		self.r.num |should| equal_to(2)
		self.r.cliente.nome |should| equal_to('Ronaldinho Gaucho')
		self.r.quarto.num |should| equal_to(202)
		self.r.dtinicio |should| equal_to(date(2011, 10, 22))
		self.r.dtfim |should| equal_to(date(2011, 10, 29))

	def testaBcadReserva(self):
		self.c.cadCli('Anderson Silva', '12369978909', '2299019866')
		self.q.cadQuarto(203, 'Simples')
		self.r.cadReserva(self.q, 203, self.c, 4, date(2011, 10, 15), date(2011, 10, 20))
		self.r.lista[0].num |should| equal_to(4)
		self.r.lista[0].cliente.nome |should| equal_to('Anderson Silva')
		self.r.lista[0].quarto.num |should| equal_to(203)
		self.r.lista[0].dtinicio |should| equal_to(date(2011, 10, 15))	
		self.r.lista[0].dtfim |should| equal_to(date(2011, 10, 20))
		self.r.lista |should| have(1).itens
		self.c.cadCli('Lionel Messi', '12369978909', '2299019866')
		self.r.cadReserva(self.q, 203, self.c, 5, date(2011, 10, 22), date(2011, 10, 29))
		self.r.lista[1].num |should| equal_to(5)
		self.r.lista[1].cliente.nome |should| equal_to('Lionel Messi')
		self.r.lista[1].quarto.num |should| equal_to(203)
		self.r.lista[1].dtinicio |should| equal_to(date(2011, 10, 22))	
		self.r.lista[1].dtfim |should| equal_to(date(2011, 10, 29))
		self.r.lista |should| have(2).itens
		
	def testaCvalidarReserva(self):
		self.r.validarReserva(self.r, self.q, 203, self.c, 4, date(2011, 11, 12), date(2011, 11, 15)) |should| equal_to("Reserva Cadastrada")
		self.r.validarReserva(self.r, self.q, 203, self.c, 4, date(2011, 11, 12), date(2011, 11, 15)) |should| equal_to("Já existe a seguinte reserva para esse Quarto: \n\n"+str(self.r.lista[2]))
		self.r.validarReserva(self.r, self.q, 203, self.c, 4, date(2011, 11, 13), date(2011, 11, 14)) |should| equal_to("Já existe a seguinte reserva para esse Quarto: \n\n"+str(self.r.lista[2]))
		self.r.validarReserva(self.r, self.q, 203, self.c, 4, date(2011, 11, 11), date(2011, 11, 16)) |should| equal_to("Já existe a seguinte reserva para esse Quarto: \n\n"+str(self.r.lista[2]))
		self.r.validarReserva(self.r, self.q, 203, self.c, 4, date(2011, 11, 11), date(2011, 11, 13)) |should| equal_to("Já existe a seguinte reserva para esse Quarto: \n\n"+str(self.r.lista[2]))
		self.r.validarReserva(self.r, self.q, 203, self.c, 4, date(2011, 11, 14), date(2011, 11, 16)) |should| equal_to("Já existe a seguinte reserva para esse Quarto: \n\n"+str(self.r.lista[2]))
		self.r.validarReserva(self.r, self.q, 210, self.c, 4, date(2011, 11, 12), date(2011, 11, 15)) |should| equal_to("Quarto nao Cadastrado")
		self.r.validarReserva(self.r, self.q, 203, self.c, 20, date(2011, 11, 12), date(2011, 11, 15)) |should| equal_to("Cliente nao Cadastrado")
		self.r.validarReserva(self.r, self.q, 203, self.c, 4, date(2011, 11, 18), date(2011, 11, 15)) |should| equal_to("Data de Saida deve ser maior do que a Inicial")
		
	def testaDcancelarReserva(self):	
		self.r.cancelarReserva(self.r, 9) |should| equal_to("\n\nA Reserva informada não Existe")
		self.r.cancelarReserva(self.r, 4) |should| equal_to("\n\nReserva Cancelada com Sucesso")
		self.r.cancelarReserva(self.r, 4) |should| equal_to("\n\nA Reserva informada não Existe")

	def testaElistarReservas(self):
		self.r.listarReservas(self.r) |should| equal_to([self.r.lista[0], self.r.lista[1]])
		self.r.cancelarReserva(self.r, 7)
		self.r.listarReservas(self.r) |should| equal_to([self.r.lista[0]])

	def testaFlistarReservasPorPeriodo(self):
		self.r.listarReservasPorPeriodo(self.r, date(2011, 10, 20), date(2011, 10, 21)) |should| equal_to([])
		self.r.listarReservasPorPeriodo(self.r, date(2011, 10, 22), date(2011, 10, 29)) |should| equal_to([self.r.lista[0]])
		self.r.listarReservasPorPeriodo(self.r, date(2011, 10, 23), date(2011, 10, 28)) |should| equal_to([self.r.lista[0]])
		self.r.listarReservasPorPeriodo(self.r, date(2011, 10, 21), date(2011, 10, 30)) |should| equal_to([self.r.lista[0]])
		self.r.listarReservasPorPeriodo(self.r, date(2011, 10, 21), date(2011, 10, 28)) |should| equal_to([self.r.lista[0]])
		self.r.listarReservasPorPeriodo(self.r, date(2011, 10, 22), date(2011, 10, 30)) |should| equal_to([self.r.lista[0]])


if __name__ == '__main__':
    unittest.main()

#-*- coding:utf-8 -*-

import unittest
from should_dsl import should, should_not

from datetime import date
from cliente import Cliente
from quarto import Quarto
from hospedagem import Hospedagem
from reserva import Reserva

class TestaHospedagem(unittest.TestCase):
	
	def setUp(self):
		self.c = Cliente('Thiago Neves', '12369978909', '2299019866')
		self.q = Quarto(202, 'Master')
		self.h = Hospedagem(self.q, self.c, date(2011, 07, 10))
		self.r = Reserva(None, None, None, None)

	def testaAinit(self):		
		self.h.num |should| equal_to(1)
		self.h.cliente.nome |should| equal_to('Thiago Neves')
		self.h.quarto.num |should| equal_to(202)
		self.h.dtinicio |should| equal_to(date.today())
		self.h.dtfim |should| equal_to(date(2011, 07, 10))
		self.h.vlextra |should| equal_to(0.00)
		self.h.situacao |should| equal_to('Em Aberto')
		self.h = Hospedagem(self.q, Cliente('Ronaldinho Gaucho', '98765478909', '2167549876'), date(2011, 7, 11))
		self.h.num |should| equal_to(2)
		self.h.cliente.nome |should| equal_to('Ronaldinho Gaucho')
		self.h.quarto.num |should| equal_to(202)
		self.h.dtinicio |should| equal_to(date.today())
		self.h.dtfim |should| equal_to(date(2011, 07, 11))
		self.h.vlextra |should| equal_to(0.00)
		self.h.situacao |should| equal_to('Em Aberto')

	def testaBcheckIn(self):
		self.c.cadCli('Anderson Silva', '12369978909', '2299019866')
		self.q.cadQuarto(203, 'Simples')
		self.h.checkIn(self.q, 203, self.c, 4, date(2011, 07, 10))
		self.h.lista[0].num |should| equal_to(4)
		self.h.lista[0].quarto.num |should| equal_to(203)
		self.q.lista[0].situacao |should| equal_to('Ocupado')
		self.c.lista[0].qtdHosp |should| equal_to(1)
		self.h.lista[0].cliente.nome |should| equal_to('Anderson Silva')
		self.h.lista[0].dtinicio |should| equal_to(date.today())
		self.h.lista[0].dtfim |should| equal_to(date(2011, 07, 10))
		self.h.lista[0].situacao |should| equal_to('Em Aberto')
		self.h.lista[0].vlextra |should| equal_to(0.00)
		self.c.cadCli('Lionel Messi', '12369978909', '2299019866')
		self.q.cadQuarto(202, 'Master')
		self.h.checkIn(self.q, 202, self.c, 5, date(2011, 07, 5))
		self.h.lista[1].num |should| equal_to(5)
		self.h.lista[1].quarto.num |should| equal_to(202)
		self.q.lista[1].situacao |should| equal_to('Ocupado')
		self.c.lista[1].qtdHosp |should| equal_to(1)
		self.h.lista[1].cliente.nome |should| equal_to('Lionel Messi')
		self.h.lista[1].dtinicio |should| equal_to(date.today())
		self.h.lista[1].dtfim |should| equal_to(date(2011, 07, 5))
		self.h.lista[1].situacao |should| equal_to('Em Aberto')
		self.h.lista[1].vlextra |should| equal_to(0.00)

	def testaBcheckOut(self):
		self.h.checkOut(self.h, 4, self.q, 58.95)
		self.h.lista[0].num |should| equal_to(4)
		self.h.lista[0].quarto.num |should| equal_to(203)
		self.q.buscarQuarto(self.q, 203).situacao |should| equal_to('Livre')
		self.h.lista[0].cliente.nome |should| equal_to('Anderson Silva')
		self.h.lista[0].dtfim |should| equal_to(date.today())
		self.h.lista[0].situacao |should| equal_to('Encerrada')
		self.h.lista[0].vlextra |should| equal_to(58.95)
		self.h.lista[0].vltotal |should| equal_to(148.95) #valor de 1 diaria de 90,00(quarto simples) + o gasto no frigobar (58.95)
		
	def testaCnumDeDiarias(self):
		self.h.numDeDiarias(date(2011, 7, 4), date(2011, 7, 4)) |should| equal_to(1)
		self.h.numDeDiarias(date(2011, 7, 4), date(2011, 7, 5)) |should| equal_to(1)
		self.h.numDeDiarias(date(2011, 7, 4), date(2011, 7, 14)) |should| equal_to(10)
		self.h.numDeDiarias(date(2011, 7, 4), date(2011, 10, 12)) |should| equal_to(100)

	def testaElistarHospedagens(self):
		self.h.listarHospedagens(self.h) |should| equal_to([self.h.lista[0], self.h.lista[1]])

	def testaGlistarQuartosPorSituacao(self):
		self.h.listarHospedagensPorSituacao(self.h, 'Em Aberto') |should| equal_to([self.h.lista[1]])
		self.h.listarHospedagensPorSituacao(self.h, 'Encerrada') |should| equal_to([self.h.lista[0]])

	def testaHcancelarHospedagem(self):	
		self.h.cancelarHospedagem(self.h, 9) |should| equal_to("\n\nA Hospedagem informada não Existe")
		self.h.cancelarHospedagem(self.h, 4) |should| equal_to("\n\nHospedagem Cancelada com Sucesso")
		self.h.cancelarHospedagem(self.h, 4) |should| equal_to("\n\nA Hospedagem informada não Existe")

	def testaIvalidarReserva(self):
		self.h.validarHospedagem(self.h, self.r, self.q, 210, self.c, 4, date(2011, 11, 15)) |should| equal_to("Quarto nao Cadastrado")
		self.h.validarHospedagem(self.h, self.r, self.q, 203, self.c, 9, date(2011, 11, 15)) |should| equal_to("Cliente nao Cadastrado")
		self.h.validarHospedagem(self.h, self.r, self.q, 202, self.c, 4, date(2011, 11, 15)) |should| equal_to("Quarto Ocupado")
		self.h.validarHospedagem(self.h, self.r, self.q, 203, self.c, 4, date(2011, 7, 2)) |should| equal_to("Data de Saida deve ser maior do que a de hoje")
		self.r.cadReserva(self.q, 203, self.c, 5, date(2011, 7, 10), date(2011, 7, 15))
		self.h.validarHospedagem(self.h, self.r, self.q, 203, self.c, 4, date(2011, 7, 10)) |should| equal_to("Existe a seguinte reserva para esse Quarto: \n\n"+str(self.r.lista[0]))
		self.h.validarHospedagem(self.h, self.r, self.q, 203, self.c, 4, date(2011, 7, 15)) |should| equal_to("Existe a seguinte reserva para esse Quarto: \n\n"+str(self.r.lista[0]))
		self.h.validarHospedagem(self.h, self.r, self.q, 203, self.c, 4, date(2011, 7, 16)) |should| equal_to("Existe a seguinte reserva para esse Quarto: \n\n"+str(self.r.lista[0]))
		self.h.validarHospedagem(self.h, self.r, self.q, 203, self.c, 4, date(2011, 7, 9)) |should| equal_to("Checkin Concluido")
		
	def testaJcheckOutDeClienteVip(self):
		self.h.checkOut(self.h, 12, self.q, 58.95)
		self.h.checkIn(self.q, 203, self.c, 4, date(2011, 07, 10)) #3º hospedagem do cliente 'Anderson Sliva'
		self.h.checkOut(self.h, 14, self.q, 58.95)
		self.h.checkIn(self.q, 203, self.c, 4, date(2011, 07, 10)) #4º hospedagem do cliente 'Anderson Sliva'
		self.h.checkOut(self.h, 15, self.q, 58.95)
		self.h.checkIn(self.q, 203, self.c, 4, date(2011, 07, 10)) #5º hospedagem do cliente 'Anderson Sliva' *****VIROU VIP******
		self.h.checkOut(self.h, 16, self.q, 90.00)
		self.h.lista[4].num |should| equal_to(16)
		self.h.lista[4].quarto.num |should| equal_to(203)
		self.q.buscarQuarto(self.q, 203).situacao |should| equal_to('Livre')
		self.h.lista[4].cliente.nome |should| equal_to('Anderson Silva')
		self.h.lista[4].dtfim |should| equal_to(date.today())
		self.h.lista[4].situacao |should| equal_to('Encerrada')
		self.h.lista[4].vlextra |should| equal_to(90.00)
		self.h.lista[4].vltotal |should| equal_to(162.00) #1 diaria de 90,00 + frigobar (90.00) - 10% CLIENTE VIP (18.00)
		self.h.checkIn(self.q, 203, self.c, 4, date(2011, 07, 10)) #6º hospedagem do cliente 'Anderson Sliva'
		self.h.checkOut(self.h, 17, self.q, 30.00)
		self.h.lista[5].num |should| equal_to(17)
		self.h.lista[5].quarto.num |should| equal_to(203)
		self.q.buscarQuarto(self.q, 203).situacao |should| equal_to('Livre')
		self.h.lista[5].cliente.nome |should| equal_to('Anderson Silva')
		self.h.lista[5].dtfim |should| equal_to(date.today())
		self.h.lista[5].situacao |should| equal_to('Encerrada')
		self.h.lista[5].vlextra |should| equal_to(30.00)
		self.h.lista[5].vltotal |should| equal_to(108.00) #1 diaria de 90,00 + frigobar (30.00) - 10% CLIENTE VIP (12.00)
		

if __name__ == '__main__':
    unittest.main()

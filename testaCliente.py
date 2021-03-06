#-*- coding:utf-8 -*-

import unittest
from should_dsl import should, should_not

from datetime import date
from cliente import Cliente

class TestaCliente(unittest.TestCase):
	
	def setUp(self):
		self.c = Cliente('Thiago Neves', '12369978909', '2299019866')

	def testaAinit(self):		
		self.c.num |should| equal_to(1)
		self.c.nome |should| equal_to('Thiago Neves')
		self.c.cpf |should| equal_to('12369978909')
		self.c.tel |should| equal_to('2299019866')
		self.c.qtdHosp |should| equal_to(0)
		self.c.vip |should| equal_to('N')
		self.c = Cliente('Ronaldinho Gaucho', '98765478909', '2167549876')
		self.c.num |should| equal_to(2)
		self.c.nome |should| equal_to('Ronaldinho Gaucho')
		self.c.cpf |should| equal_to('98765478909')
		self.c.tel |should| equal_to('2167549876')
		self.c.qtdHosp |should| equal_to(0)
		self.c.vip |should| equal_to('N')

	def testaBcadCli(self):
		self.c.cadCli('Jose Aldo', '12369978909', '2299019866')
		self.c.lista[0].nome |should| equal_to('Jose Aldo')
		self.c.lista[0].num |should| equal_to(4)	
		self.c.lista |should| have(1).itens
		self.c.cadCli('Anderson Silva', '12369978641', '2299019876')
		self.c.lista[1].nome |should| equal_to('Anderson Silva')
		self.c.lista[1].num |should| equal_to(5)	
		self.c.lista |should| have(2).itens

	def testaCbuscarClientes(self):
		self.c.buscarCliente(self.c, 6) |should| equal_to(False)
		self.c.buscarCliente(self.c, 4) |should| equal_to(self.c.lista[0])
		self.c.buscarCliente(self.c, 5) |should| equal_to(self.c.lista[1])

	def testaDsetVip(self):
		self.c.setVip(self.c, 12) |should| equal_to("Cliente Não Cadastrado")
		self.c.setVip(self.c, 5)
		self.c.lista[1].vip |should| equal_to('S')

	def testaElistarClientes(self):
		self.c.listarClientes(self.c) |should| equal_to([self.c.lista[0], self.c.lista[1]])

	def testaFlistarClientesVip(self):
		self.c.listarClientesVip(self.c) |should| equal_to([self.c.lista[1]])
		
if __name__ == '__main__':
    unittest.main()

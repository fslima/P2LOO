#-*- coding:utf-8 -*-

import unittest
from should_dsl import should, should_not

from datetime import date
from quarto import Quarto

class TestaQuarto(unittest.TestCase):
	
	def setUp(self):
		self.q = Quarto(201, 'Simples')

	def testaAinit(self):		
		self.q.num |should| equal_to(201)
		self.q.tipo |should| equal_to('Simples')
		self.q.vldiaria |should| equal_to(90.00)
		self.q.situacao |should| equal_to('Livre')
		self.q = Quarto(202, 'Casal')
		self.q.num |should| equal_to(202)
		self.q.tipo |should| equal_to('Casal')
		self.q.vldiaria |should| equal_to(150.00)
		self.q.situacao |should| equal_to('Livre')

	def testaBcadQuarto(self):
		self.q.cadQuarto(203, 'Master')
		self.q.lista[0].num |should| equal_to(203)
		self.q.lista[0].tipo |should| equal_to('Master')
		self.q.lista[0].vldiaria |should| equal_to(260.00)	
		self.q.lista |should| have(1).itens
		self.q.cadQuarto(301, 'Simples')
		self.q.lista[1].num |should| equal_to(301)
		self.q.lista[1].tipo |should| equal_to('Simples')
		self.q.lista[1].vldiaria |should| equal_to(90.00)	
		self.q.lista |should| have(2).itens

	def testaCbuscarQuarto(self):
		self.q.buscarQuarto(self.q, 201) |should| equal_to(False)
		self.q.buscarQuarto(self.q, 203) |should| equal_to(self.q.lista[0])
		self.q.buscarQuarto(self.q, 301) |should| equal_to(self.q.lista[1])

	def testaDlistarQuartos(self):
		self.q.listarQuartos(self.q) |should| equal_to([self.q.lista[0], self.q.lista[1]])

	def testaElistarQuartosPorTipo(self):
		self.q.listarQuartosPorTipo(self.q, 'Master') |should| equal_to([self.q.lista[0]])
		self.q.listarQuartosPorTipo(self.q, 'Simples') |should| equal_to([self.q.lista[1]])
		self.q.listarQuartosPorTipo(self.q, 'Casal') |should| equal_to([])

	def testaElistarQuartosPorTipo(self):
		self.q.listarQuartosPorSituacao(self.q, 'Livre') |should| equal_to([self.q.lista[0], self.q.lista[1]])
		self.q.lista[0].situacao = 'Ocupado'
		self.q.listarQuartosPorSituacao(self.q, 'Ocupado') |should| equal_to([self.q.lista[0]])
		
if __name__ == '__main__':
    unittest.main()

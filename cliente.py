#-*- coding:utf-8 -*-

class Cliente(object):
	num = 0	
	qtdHosp = 0
	vip = 'N'
	lista = []
	def __init__(self, n, c, t):
		Cliente.num += 1
		self.num = Cliente.num
		self.nome = n
		self.cpf = c
		self.tel = t

	def __repr__(self):
		return "Codigo: "+str(self.num)+" | Nome: "+str(self.nome)+" | CPF: "+str(self.cpf)+" | Telefone: "+str(self.tel)+" | Hospedagens: "+str(self.qtdHosp)+" | Eh VIP: "+str(self.vip)

	def cadCli(self, n, c, t):
		Cliente.lista.append(Cliente(n, c, t))

	def buscarCliente(self, c, n):
		existe = False
		num = 999999
		for i in range(0, len(c.lista)):
			if c.lista[i].num == n:
				existe = True
				num = i
		if existe == True:
			return c.lista[num]
		else:
			return False

	def setVip(self, c, n):
		if self.buscarCliente(c, n) == False:
			return "Cliente Não Cadastrado"
		else:
			self.buscarCliente(c, n).vip = 'S'

	def setQtdHosp(self, c, n):
		if self.buscarCliente(c, n) == False:
			return "Cliente Não Cadastrado"
		else:
			self.buscarCliente(c, n).qtdHosp += 1
			if self.buscarCliente(c, n).qtdHosp == 5:
				self.setVip(c, n)

	def listarClientes(self, c):
		listaDeClientes = []
		for i in range(0, len(c.lista)):
			listaDeClientes.append(c.lista[i])
		return listaDeClientes

	def listarClientesVip(self, c):
		listaDeVips = []
		for i in range(0, len(c.lista)):
			if c.lista[i].vip == 'S':
				listaDeVips.append(c.lista[i])
		return listaDeVips

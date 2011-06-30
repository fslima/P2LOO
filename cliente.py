#-*- coding:utf-8 -*-

class Cliente(object):
	num = 0	
	qtdhosp = 0
	vip = 'N'
	lista = []
	def __init__(self, n, c, t):
		Cliente.num += 1
		self.num = Cliente.num
		self.nome = n
		self.cpf = c
		self.tel = t

	def __repr__(self):
		return "Codigo: "+str(self.num)+" | Nome: "+str(self.nome)+" | CPF: "+str(self.cpf)+" | Telefone: "+str(self.tel)+" | Hospedagens: "+str(self.qtdhosp)+" | Eh VIP: "+str(self.vip)

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

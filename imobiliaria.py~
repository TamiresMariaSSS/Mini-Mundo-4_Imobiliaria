#coding:utf-8

class Imovel(object):

   def __init__(self, bairro, area, descricao, endereco, proprietario, tipo_imovel, preco_compra):
        self.bairro = bairro
        self.area = area
        self.descricao = descricao
        self.endereco = endereco
        self.proprietario = proprietario
        self.tipo_imovel=tipo_imovel
        self._preco_compra = preco_compra
        self._preco_minimo = preco_compra * 1.10
        self._preco_venda = 0
        self.novo_proprietario = None
        self.antigo_proprietario = None
        
class Proprietario(object):
    lista_proprietarios = []
    def __init__(self, nome, cpf, endereco, telefone):
		        
		self.nome = nome
		self.cpf = cpf
		self.endereco = endereco
		self.telefone = telefone

    def cadastrar_proprietario(self):
        if self not in Proprietario.lista_proprietarios:
            Proprietario.lista_proprietarios.append(self)
        else:
            raise ValueError("Error no Cadastro de Proprietário!")


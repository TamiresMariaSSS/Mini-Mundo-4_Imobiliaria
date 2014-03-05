#coding:utf-8

class Imovel(object):
    imoveis_vendidos = []
    imoveis_comprados = []

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
    
    def __eq__(self, imovel2):
        return self.endereco == imovel2.endereco and self.bairro == imovel2.bairro

    def comprar(self, antigo_proprietario):
        if self not in Imovel.imoveis_comprados:
            self.antigo_proprietario = antigo_proprietario            
            Imovel.imoveis_comprados.append(self)
        else:
            raise ValueError

    def vender(self, preco_de_venda, novo_proprietario):
        if self in Imovel.imoveis_comprados:
            if preco_de_venda >= self._preco_minimo:
                self._preco_venda = preco_de_venda
                self.novo_proprietario = novo_proprietario
                Imovel.imoveis_vendidos.append(self)
                Imovel.imoveis_comprados.remove(self)
            else:
                raise ValueError("preco de venda >= self_preco minimo")
        else:
            raise ValueError("nao esta na lista comprados")

    def listar_imoveis_disponiveis(self):
        return Imovel.imoveis_comprados
    
    def listar_imoveis_vendidos(self, bairro):
        lista_imoveis_vendidos = []
        for i, imovel in enumerate(Imovel.imoveis_vendidos):
            if imovel.bairro == bairro:
                lista_imoveis_vendidos.append("%s %s %s %.0f %.0f" %(imovel.bairro, imovel.antigo_proprietario, imovel.novo_proprietario, imovel._preco_venda, imovel._preco_compra))

        return lista_imoveis_vendidos
        
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

    def listar_proprietarios_compradores(self):
        contador = 0
        lista = []
        for imovel in Imovel.imoveis_vendidos:
            for proprietario in Proprietario.lista_proprietarios:
                if imovel.novo_proprietario == proprietario:
                    contador += 1
            if contador > 1:
                if proprietario not in lista:           
                    lista.append(proprietario)
        
        return lista

    def listar_proprietarios_vendedores(self):
        contador = 0
        lista = []
        for imovel in Imovel.imoveis_comprados:
            for proprietario in Proprietario.lista_proprietarios:
                if imovel.antigo_proprietario == proprietario:
                    contador += 1
                if contador >1:
                    if proprietario not in lista:
                        lista.append(proprietario)
        return lista


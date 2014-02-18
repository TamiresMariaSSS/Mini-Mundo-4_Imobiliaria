#coding:utf-8

import unittest
from should_dsl import should
from imobiliaria import Imovel, Proprietario

class TestImovel(unittest.TestCase):

    def teste_cria_objeto_imovel(self):

        imovel=Imovel('bairro', 100, 'descricao', 'endereco', 'proprietario', 'tipo_imovel', 5.000)

        imovel.bairro |should| equal_to('bairro')
        imovel.area |should| equal_to(100)
        imovel.descricao |should| equal_to('descricao')
        imovel.endereco |should| equal_to('endereco')
        imovel.proprietario |should| equal_to('proprietario')
        imovel.tipo_imovel |should| equal_to('tipo_imovel')
        imovel._preco_compra |should| equal_to(5.000)
        imovel._preco_venda |should| equal_to(0)
        imovel.novo_proprietario |should| equal_to(None)
        imovel.antigo_proprietario |should| equal_to(None)
        
        
class TestProprietario(unittest.TestCase):

    def teste_cria_objeto_proprietario(self):
    
        proprietario=Proprietario('nome', '123.456.789-0', 'endereco', 'telefone')
        proprietario.nome |should| equal_to('nome')
        proprietario.cpf |should| equal_to('123.456.789-0')
        proprietario.endereco |should| equal_to('endereco')
        proprietario.telefone |should| equal_to('telefone')

    def teste_cadastro_proprietarios(self):
    
        proprietario=Proprietario('nome', '123.456.789-0', 'endereco', 'telefone')
        proprietario.cadastrar_proprietario() 
        proprietario.lista_proprietarios[0] |should| equal_to(proprietario)


    def teste_lista_proprietarios(self):
    
        lista_proprietarios = []
        imoveis_vendidos = []
        imoveis_comprados = []
        proprietario1=Proprietario('nome', '123.456.789-0', 'endereco', 'telefone')
        proprietario2=Proprietario('nome2', '123.456.789-0', 'endereco2', 'telefone2')
        proprietario1.cadastrar_proprietario()
        proprietario2.cadastrar_proprietario()
        imovel=Imovel('bairro', 100, 'descricao', 'endereco', proprietario1, 'tipo_imovel', 5.000)
        imovel2=Imovel('bairro2', 103, 'descricao2', 'endereco2', proprietario1, 'tipo_imovel', 6.000)
    

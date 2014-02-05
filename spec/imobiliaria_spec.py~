#coding:utf-8

import unittest
from should_dsl import should
from imobiliaria import Imovel

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

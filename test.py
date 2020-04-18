import unittest

from models import Cliente, GerenciadorDeCupom, Compra


class TestGerarCupom(unittest.TestCase):
    """
    Dado um determinado cliente verificar se ele está apto a ganhar
    um cupom.
    """

    def setUp(self):
        self.cliente = Cliente('Tarzan')

    def test_apto_a_ganhar_cupom(self):
        compra = Compra(100, self.cliente)
        self.cliente.compras.append(compra.valor)
        gerenciador = GerenciadorDeCupom(self.cliente)
        self.assertTrue(gerenciador.pode_gerar_cupom())

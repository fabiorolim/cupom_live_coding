# Sisteminha para gerar cupom
# Dado um valor x de compras acumuladas o cliente
# ganha um cupom
# A cada R$ 100,00 em compras gera-se um cupom de R$ 20,00

# Cliente
# Cupom
# Compra

import random
import string


class Cliente:
    """
    Representa um cliente do estabelecimento
    """

    def __init__(self, nome, cupons=[], compras=[]):
        self.nome = nome
        self.cupons = cupons
        self.compras = compras

    def __str__(self):
        return self.nome


class Cupom:

    def __init__(self, valor):
        self.valor = valor

    def gerar(self):
        pass

    def __str__(self):
        pass


class CupomDoBurguer(Cupom):
    """
    Representar um cupom de desconto
    """

    def __init__(self, valor=20):
        super().__init__(valor)

    def gerar(self):
        lista_numeros = []
        while len(lista_numeros) <= 10:
            lista_numeros.append(chr(random.randint(97, 120)))
            self.codigo = ''.join(lista_numeros)
        return self.codigo

    def __str__(self):
        return ''.join(self.codigo)


class CupomDoAcai(Cupom):

    def __init__(self, valor=20):
        super().__init__(valor)
        self.codigo = []

    def gerar(self):
        alfa = list(string.ascii_uppercase)
        while len(self.codigo) <= 10:
            self.codigo.append(random.choice(alfa))
        self.codigo = ''.join(self.codigo)
        return self.codigo

    def __str__(self):
        return self.codigo


class Compra:
    """
    Representar uma compra feita por um cliente
    """

    def __init__(self, valor, cliente):
        self.valor = valor
        self.cliente = cliente


class GerenciadorDeCupom:

    def __init__(self, cliente):
        self.cliente = cliente

    def verificar_compras(self):
        total_compras = sum(self.cliente.compras)
        return total_compras

    def pode_gerar_cupom(self):
        if self.verificar_compras() >= 100:
            return True
        else:
            return False

# import random
# valores_compras = []
# cupons_validos = []
#
#
# # Acumula valores das compras
# def comprar(valor):
#     valores_compras.append(valor)
#
#
# def valor_acumulado():
#     return sum(valores_compras)
#
#
# def gerar_cupom():
#     if valor_acumulado() >= 100:
#         lista_numeros = []
#         while len(lista_numeros) <= 10:
#             lista_numeros.append(chr(random.randint(97, 200)))
#             cupom = ''.join(lista_numeros)
#         return cupom
#
#
# def adicionar_cupom(cupom):
#     cupons_validos.append(cupom)

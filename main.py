from models import *

nome = input('Informe o nome do cliente: ')
cliente = Cliente(nome)
valor = float(input('Informe o valor da compra: '))
compra = Compra(valor, cliente)
cliente.compras.append(compra.valor)
gerenciador = GerenciadorDeCupom(cliente)
cupom = CupomDoAcai()
if gerenciador.pode_gerar_cupom():
    print(cupom.gerar())

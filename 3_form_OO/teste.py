from conta import Conta
from data import Data


conta = Conta(123, "Erick", 400.0, 1000.0)
print(conta.get_saldo)
print(conta.extrato())

conta2 = Conta(321, "Jose", 500.0, 2000.0)
print(conta2.get_limite())

d = Data(21, 11, 2007)
d.formatada()




# def cria_conta(numero, titular, saldo, limite):
#     conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
#     return conta

# def depositar(conta, valor):
#     conta["saldo"] += valor

# def saca(conta, valor):
#     conta["saldo"] -= valor

# def extrato(conta):
#     print(f'Saldo é {conta["saldo"]}')

# conta = cria_conta(123, "Erick", 400.0, 1000.0)

# depositar(conta, 50.0)
# extrato(conta)
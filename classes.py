import datetime

class Cliente:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Funcionario:

    def __init__(self, nome, cpf, cargo):
        self.nome = nome
        self.cpf  = cpf
        self.cargo = cargo


class Conta:
    
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self._saldo = saldo
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_valor):
        print('\nErro. Utilize o método depositar()!')

    @property
    def historico(self):
        return self._historico

    def ver_saldo(self):
        print('\nO saldo é de R$', self.saldo)
        transacao = 'Saldo retirado, valor de {}'.format(self._saldo)
        self._historico.adicionar_transacao(transacao)

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            transacao = 'Saque realizado no valor de {}'.format(valor)
            self._historico.adicionar_transacao(transacao)
            return True
        else:
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            transacao = 'Deposito realizado no valor de {}'.format(valor)
            self._historico.adicionar_transacao(transacao)
            return True
        else:
            return False

    def transferir(self, conta_destino, valor):
        if 0 < valor <= self._saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
            transacao = 'Transferencia realizada no valor de {} para a conta de {}'.format(valor, conta_destino.titular)
            self._historico.adicionar_transacao(transacao)
            return True
        else:
            return False


class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def imprimir_historico(self):
        print('\nData abertura:', self.data_abertura)
        print('\nTransações:')
        for transacao in self.transacoes:
            print('  Transação:', transacao)
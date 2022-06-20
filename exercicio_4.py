from classes import Conta

if __name__ == '__main__':

    conta1 = Conta('Maria', '123', 1000.00)
    conta2 = Conta('João', '456', 55890.10)
    conta3 = Conta('José', '789', 726.45)

    print('\nConta 1:', conta1.__dict__)
    print('Conta 2:', conta2.__dict__)
    print('Conta 3:', conta3.__dict__)

    conta1.ver_saldo()
    conta2.ver_saldo()
    conta3.ver_saldo()

    saque_ok = conta2.sacar(1000)
    print('\nSaque realizado com sucesso?', saque_ok)
    conta2.ver_saldo()

    saque_ok = conta3.sacar(2000)
    print('\nSaque realizado com sucesso?', saque_ok)
    conta3.ver_saldo()

    deposito_ok = conta3.depositar(10000)
    print('\nDepósito realizado com sucesso?', deposito_ok)
    conta3.ver_saldo()

    tranferencia_ok = conta1.transferir(conta3, 250.00)
    print('\nTransferência realizada com sucesso?', tranferencia_ok)
    conta1.ver_saldo()
    conta3.ver_saldo()

    print("\n")
    print(dir(conta1))
    print("\n")
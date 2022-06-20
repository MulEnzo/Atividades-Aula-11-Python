from classes import Cliente, Conta

if __name__ == '__main__':

    cliente = Cliente('Maria Clara', '111.111.111-11', 18)
  
    conta = Conta(cliente.nome, '123', 1000.00)
    
    print('\nCliente:', cliente.__dict__)

    print('\nConta:', conta.__dict__)

    conta.saldo = 10000000

    conta.ver_saldo()
    conta.sacar(300.00)
    conta.ver_saldo()
    conta.depositar(690.00)
    conta.ver_saldo()

    print('\nConta:', conta.__dict__)

    conta._historico.imprimir_historico()

    print('\n')
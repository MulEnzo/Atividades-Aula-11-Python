from classes import Cliente, Funcionario, Conta

if __name__ == '__main__':

    c1 = Cliente('Maria', '111.111.111-11', 18)
    c2 = Cliente('João', '222.222.222-22', 23)
    c3 = Cliente('José', '333.333.333-33', 40)

    f1 = Funcionario('Rafael', '444.444.444-44', 'Gerente')
    f2 = Funcionario('Marcelo', '555.555.555-55', 'Caixa')
    f3 = Funcionario('Jonas', '666.666.666-66', 'Caixa')

    conta1 = Conta('Maria', '123', 1000.00)
    conta2 = Conta('João', '456', 55890.10)
    conta3 = Conta('José', '789', 726.45)

    print('\nCliente 1:', c1.__dict__)
    print('Cliente 2:', c2.__dict__)
    print('Cliente 3:', c3.__dict__)

    print('\nFuncionário 1:', f1.__dict__)
    print('Funcionário 2:', f2.__dict__)
    print('Funcionário 3:', f3.__dict__)

    print('\nConta 1:', conta1.__dict__)
    print('Conta 2:', conta2.__dict__)
    print('Conta 3:', conta3.__dict__)

    print('\n\nCliente 1:')
    print('  Nome:', c1.nome)
    print('  CPF:', c1.cpf)
    print('  Idade:', c1.idade)

    print('\n\nCliente 2:')
    print('  Nome:', c2.nome)
    print('  CPF:', c2.cpf)
    print('  Idade:', c2.idade)

    print('\n\nCliente 3:')
    print('  Nome:', c3.nome)
    print('  CPF:', c3.cpf)
    print('  Idade:', c3.idade)

    print("\n")
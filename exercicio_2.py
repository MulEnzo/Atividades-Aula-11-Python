class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def falar_nome(self):
        print("\nMeu nome é {}" .format(self.nome))

    def falar_idade(self):
        print("\nMinha idade é {}" .format(self.idade))

    def estudando(self):
        print("\nEstou estudando!")


class Aluno:

    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = (nota1 + nota2 + nota3) / 3


class Turma:

    def __init__(self):
        self.alunos = []

    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)

    def retornar_aprovados(self, media_aprovacao):
        aprovados = []
        for i in range(len(self.alunos)):
            if self.alunos[i].media >= media_aprovacao:
                aprovados.append(self.alunos[i])
        return aprovados


if __name__ == '__main__':

    p = Pessoa("Enzo", 19, "111.111.111-11")

    p.falar_nome()
    p.falar_idade()
    p.estudando()
    
    a1 = Aluno('Maria', 10, 7, 9)
    a2 = Aluno('João', 6, 9, 5)
    a3 = Aluno('José', 2, 8, 4)

    turma = Turma()

    turma.incluir_aluno(a1)
    turma.incluir_aluno(a2)
    turma.incluir_aluno(a3)

    media_aprovacao = 6

    resultado = turma.retornar_aprovados(media_aprovacao)

    print("\n\nAPROVADOS\n")

    for i in range(len(resultado)):
        print(resultado[i].nome)

    print("\n")
class Pessoa:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def incrementar_idade(self):
        self.idade += 1

    def alterar_telefone(self, novo_telefone):
        self.telefone = novo_telefone


pessoa1 = Pessoa('Kaique', 17, '345678912')
print(pessoa1.telefone)
pessoa1.alterar_telefone('531794269')
print(pessoa1.telefone)
print('----------------------------------------------')


class Aluno(Pessoa):
    def __init__(self, nome, idade, telefone, nota):
        super().__init__(nome, idade, telefone)
        self.nota = nota

    def alterar_nota(self, nova_nota):
        self.nota = nova_nota


aluno1 = Aluno('João', 29, '236895313', 8.0)
print('A nota do aluno é: ' + str(aluno1.nota))

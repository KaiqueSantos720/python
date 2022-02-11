class Restaurante:

    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha

    def restaurante_descricao(self):
        print("O nome do restaurante é " + self.nome + " e o tipo de cozinha é " + self.tipo_cozinha)

    def restaurante_aberto(self):
        print("O restaurante está aberto")


rest1 = Restaurante('alimentação', 'italiana')
print(rest1.nome)
print(rest1.tipo_cozinha)
print("---------------------------------")
rest1.restaurante_aberto()
rest1.restaurante_descricao()
print("---------------------------------")

rest2 = Restaurante('france', 'francesa')
rest3 = Restaurante('spanish', 'espanhola')
rest2.restaurante_descricao()
print("---------------------------------")
rest3.restaurante_descricao()
print("---------------------------------")


class Usuario:

    def __init__(self, primeiro_nome, ultimo_nome, idade, telefone, comida_favorita):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.telefone = telefone
        self.comida_favorita = comida_favorita

    def descricao_usuario(self):
        print("O usuário " + self.primeiro_nome.title() + " " + self.ultimo_nome.title() + " tem " + str(self.idade) + " anos e seu telefone é " + self.telefone)

    def saudacao_usuario(self):
        print(
            "Olá " + self.primeiro_nome.title() + " " + self.ultimo_nome.title() + " sabemos que você adora " + self.comida_favorita + " então fique a vontade")


us1 = Usuario('rafael', 'silva', 23, '957323421', 'lasanha')
us2 = Usuario('joão', 'silva', 26, '945038258', 'strogonoff')
us3 = Usuario('kaique', 'santos', 17, '962405193', 'pizza')

us1.descricao_usuario()
us1.saudacao_usuario()
print("---------------------------------")

us2.descricao_usuario()
us2.saudacao_usuario()
print("---------------------------------")

us3.descricao_usuario()
us3.saudacao_usuario()
print("---------------------------------")

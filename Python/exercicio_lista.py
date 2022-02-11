convidados = []
condicao = 's'

for i in range(1, 11):
    condicao = input("Deseja inserir outro convidado --- s ou n ---- máximo 10")
    if condicao.lower() == 's':
        convidados.append(input("Insira o nome dos convidados "))
    else:
        break

convidados.sort()

for convidado in convidados:
    print(convidado.title())
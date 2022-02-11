# If Else Elif

peca = "Memória RAM"
# peca = "CPU"
preco_ram = 200
preco_cpu = 2000

if peca == "Memória RAM":
    print(peca)
    if preco_ram < 300:
        print("A RAM está em promoção, tendo preço igual a: " + str(preco_ram))

elif peca == "CPU":
    print(peca)
    if preco_cpu < 1800:
        print("A CPU está em promoção, tendo preço igual a: " + str(preco_cpu))

else:
    print("Não é RAM, nem CPU")

print("----------------------------------------")

jogos = ["gta", "bloodborne", "resident evil", "sekiro shadows die twice"]

for jogo in jogos:
    if jogo == "gta":
        print(jogo.upper())
    else:
        print(jogo.title())

print("----------------------------------------")

"""
nivel entre 0 e 10: baixo
nivel entre 11 e 30: medio
nivel entre 31 e 49: alto
nivel 50: mestre
"""

nivel = int(input("Qual o seu nível no jogo? "))

if 0 <= nivel <= 10:
    print("Nível Baixo")
elif 10 < nivel <= 30:
    print("Nível Médio")
elif 30 < nivel < 50:
    print("Nível Alto")
elif nivel == 50:
    print("Mestre")
else:
    print("Nível Inválido")

print("----------------------------------------")

pecas_cliente = []
continua = "n"

while continua.lower() == 'n':
    pecas_cliente.append(input("Insira a peça do seu PC \n").lower())
    continua = input("Acabou? - s ou n ")


pecas_pc = ["cpu", "gpu", "placa-mãe", "ram", "ssd", "gabinete", "fonte"]

for peca in pecas_cliente:
    if peca in pecas_pc:
        print(peca + " foi adicionada ao seu pc")

if "fonte" in pecas_cliente:
    watts = int(input("\nQuantos watts a fonte aguenta? "))
    if 0 < watts <= 300:
        print("Fonte Fraca, as peças podem ser danificadas")
    elif 301 <= watts <= 600:
        print("Fonte Média, suporta o PC, entretanto não suporta upgrades")
    else:
        print("Fonte Forte, suporta grandes upgrades")
else:
    print("\nPC não tem fonte")

if len(pecas_cliente) < len(pecas_pc):
    print("\nAinda faltam peças")
    print("\nPC não está apto para ser usado")
else:
    print("\nPC está pronto para uso")

print("----------------------------------------")
# Funções

def soma(valor1, valor2):
    return valor1 + valor2


def subtracao(valor1, valor2):
    return valor1 - valor2


def multiplicacao(valor1, valor2):
    return valor1 * valor2


print(soma(4, 7))
print(soma(12, 6))
print(soma(8, 3))

print("-------------------------------------")

print(subtracao(1000, 1000))
print(subtracao(10, 2))
print(subtracao(2, 7))

print("-------------------------------------")

print(multiplicacao(3, 7))
print(multiplicacao(10, 6))
print(multiplicacao(2, 8))


def time(nome, cidade):
    print("A equipe " + nome + " é da cidade de " + cidade)


print("-------------------------------------")

# Argumentos Posicionais
time("São Paulo", "São Paulo")
time("Palmeiras", "São Paulo")
time("Flamengo", "Rio de Janeiro")

# Argumentos Nomeados
time(cidade="Rio Grande do Sul", nome="Grêmio")


def nome_completo(nome1="", nome2="", nome3=""):
    return "Seu nome completo é: " + nome1.title() + " " + nome2.title() + " " + nome3.title()


print("-------------------------------------")
print(nome_completo("kaique", "santos"))
print(nome_completo("josé", "silva", "santos"))
print("-------------------------------------")

lista_consoles = ["PS1", "PS2", "PS3", "PS4", "PS5", "Xbox One", "Xbox Series", "Nintendo Switch"]


def imprime_lista(lista):
    for console in lista:
        print(console)


imprime_lista(lista_consoles[:]) # cópia

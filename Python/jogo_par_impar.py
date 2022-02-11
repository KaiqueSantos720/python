from calculadora_modulo import soma

print("BEM VINDO AO JOGO")
continua = 's'

while continua.lower() == 's':
    prosseguir = 0

    while prosseguir == 0:
        jogador1 = input("\nVocê quer par ou impar?")
        numero_jogador1 = int(input("\nDigite um número: "))

        if jogador1.lower() == 'par':
            print("\nJogador 2 é ímpar")
            jogador2 = 'impar'
            numero_jogador2 = int(input("\nDigite um número: "))
            prosseguir = 1
        elif jogador1.lower() == 'impar':
            print("\nJogador 2 é par")
            jogador2 = 'par'
            numero_jogador2 = int(input("\nDigite um número: "))
            prosseguir = 1
        else:
            print("\nO jogador 1 inseriu o dado incorretamente")

    if soma(numero_jogador1, numero_jogador2) % 2 == 0:
        if jogador1.lower() == 'par':
            print("\nParabéns jogador 1, você venceu")
        else:
            print("\nParabéns jogador 2, você venceu")
    else:
        if jogador1.lower() == 'impar':
            print("\nParabéns jogador 1, você venceu")
        else:
            print("\nParabéns jogador 2, você venceu")

    continua = input("\nDeseja jogar novamente? --- s ou n")

print("\nObrigado por ter jogado")

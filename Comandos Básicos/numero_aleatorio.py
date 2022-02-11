# Número Aleatório
"""
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e
permite que o usuário chute um número até que o valor aleatório gerado
no início do programa seja chutado corretamente.
O programa deve informar se o chute foi acima, abaixo
ou igual ao valor aleatório gerado no início do programa.
"""

import random

aleatorio = random.randint(1, 10)
verifica = False

while not verifica:
    numero_chute = int(input("Chute um número de 1 a 10: "))
    if 1 <= numero_chute <= 10:
        if numero_chute == aleatorio:
            print("Acertou")
            verifica = True
        elif numero_chute > aleatorio:
            print("Número Alto, Tente Novamente")
        elif numero_chute < aleatorio:
            print("Número Baixo, Tente Novamente")
    else:
        print("Número Inválido")
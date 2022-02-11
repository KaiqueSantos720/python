from calculadora_modulo import *

continua = 's'

while continua.lower() == 's':
    operacao = input("\nEscolha uma operação matemática --- (+ - * /)")

    if operacao == '+':
        valor1 = int(input("Insira o primeiro valor"))
        valor2 = int(input("Insira o segundo valor"))
        print("\nO resultado é: " + str(soma(valor1, valor2)))

    elif operacao == '-':
        valor1 = int(input("Insira o primeiro valor"))
        valor2 = int(input("Insira o segundo valor"))
        print("\nO resultado é: " + str(subtracao(valor1, valor2)))

    elif operacao == '*':
        valor1 = int(input("Insira o primeiro valor"))
        valor2 = int(input("Insira o segundo valor"))
        print("\nO resultado é: " + str(multiplacacao(valor1, valor2)))

    elif operacao == '/':
        valor1 = int(input("Insira o primeiro valor"))
        valor2 = int(input("Insira o segundo valor"))
        print("\nO resultado é: " + str(divisao(valor1, valor2)))

    else:
        print("\nOperação Inválida")

    continua = input("\nDeseja usar a calculadora? --- s ou n")


print("\nObrigado por usar a calculadora")

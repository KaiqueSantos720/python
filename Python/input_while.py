# Input e Laço While

nome = input("Digite seu nome: \n")
idade = int(input("Digite sua idade: \n"))

print(nome.title() + " possui " + str(idade) + " anos")

print("--------------------------------------")

sair = 'n'

while sair == 'n':
    operacao = input("escolha uma operacao: \n+ soma \n- subtração \n* multiplicação \n/ divisão \n")

    if operacao == "+":
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        print("O resultado da soma é: " + str(valor1 + valor2))
        sair = input("Deseja sair? s ou n \n")

    elif operacao == "-":
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        print("O resultado da subtração é: " + str(valor1 - valor2))
        sair = input("Deseja sair? s ou n \n")

    elif operacao == '*':
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        print("O resultado da multiplicação é: " + str(valor1 * valor2))
        sair = input("Deseja sair? s ou n \n")

    elif operacao == '/':
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        if valor2 == 0:
            print("Não é possível realizar divisão por 0\n")
        else:
            print("O resultado da divisão é: " + str(valor1 / valor2))
            sair = input("Deseja sair? s ou n \n")

    else:
        print("Operação Inválida")

print("\n" + nome.title() + " encerrou a calculadora")

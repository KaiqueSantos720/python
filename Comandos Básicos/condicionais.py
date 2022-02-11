#Condicionais
ganhou_partida = False
if ganhou_partida:
    print("Parabéns, você ganhou a partida")
else:
    print('Você não ganhou, tente novamente')

celular_carregado = True
if celular_carregado:
    print("Celular não precisa ser carregado")
else:
    print("Celular precisa ser carregado")

numero_atrasos = input("Quantas vezes você chegou atrasado? ")
if int(numero_atrasos) >= 3:
    print("Você está suspenso")
elif int(numero_atrasos) == 1:
    print("Pode entrar, mas se você tiver mais dois atrasos você será suspenso")
elif int(numero_atrasos) == 2:
    print("Pode entrar, contudo, se você se atrasar novamente, você será suspenso")
else:
    print("Pode entrar")

valor1 = input("Entre com o valor 1: ")
valor2 = input("Entre com o valor 2: ")
if int(valor1) > int(valor2):
    print("Valor 1 é maior")
elif int(valor2) > int(valor1):
    print("Valor 2 é maior")
elif int(valor2) == int(valor1):
    print("Valores iguais")
else:
    print("Valores Inválidos")
# Fatorial

"""
Crie um programa que recebe um número e imprime o seu fatorial.
"""

fatorial = 1
numero = int(input("Insira um número para que seja calculado seu fatorial"))
if numero >= 1:
    for i in range(fatorial, numero + 1):
        fatorial *= i
    print(fatorial)
else:
    print("Número Inválido")

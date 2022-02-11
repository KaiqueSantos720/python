#Coleções
precos = [10.4, 20, 56.5, 49, 47]
print(precos[2])
print(precos.index(47))

print("-----------------------------")

lista_monte_de_coisa = [23, "Salve", True, 34.56]
print(lista_monte_de_coisa)

print("-----------------------------")

for preco in precos:
    print(preco)

print("-----------------------------")

idades = [15, 46, 75, 34, 23]
soma = 0
for idade in idades:
    soma += idade
print(soma)
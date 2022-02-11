# For
equipes = ["Real Madrid", "Milan", "Bayern", "Liverpool", "Ajax", "Barcelona", "Manchester United", "Chelsea"]
for equipe in equipes:
    print(equipe + " ganhou o torneio")

print("------------------------------------------")

# For com numeros
for numero in range(0, 21, 2):
    print(numero)

print("------------------------------------------")

nums = list(range(1, 101))
print(nums)

print("------------------------------------------")

numeros = []
for numero in nums:
    numeros.append(numero)
print(numeros)
print("------------------------------------------")

# Separação de listas
print(equipes[2:5])
print(equipes[:5])
print(equipes[0:5:2])
print("------------------------------------------")

for equipe in equipes[:3:2]:
    print(equipe)
print("------------------------------------------")

# Cópia de listas
equipes2 = equipes[:]
print(equipes2)

equipes3 = equipes
equipes.append("Leipzig")
print(equipes3)


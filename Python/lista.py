jogadores = ["Lewandowski", "Messi", "De Bruyne", "Cristiano Ronaldo", "Salah"]
print(jogadores)

jogadores.remove("De Bruyne")
jogadores.append("Haaland")
print(jogadores)

jogadores.insert(2, "Mbappe")
del jogadores[1]
print(jogadores)

jogadores.pop(2)
jogadores.insert(0, "Neuer")
print(jogadores)

# Organização de Listas
jogadores.sort()
print(jogadores)

jogadores.sort(reverse=True)
print(jogadores)

print(sorted(jogadores))
print(len(jogadores))


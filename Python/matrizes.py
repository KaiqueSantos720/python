videogame = [
    ['modelo', 'ps5'],
    ['fabricante', 'sony'],
    ['ano', '2019']
]

print(videogame[0][1].upper())
print(videogame[1][1].title())
videogame[2][1] = '2020'
print(videogame[2][1])

videogame.append(['resolução', '4K'])

for linha, coluna in videogame:
    print('Linha: ' + linha + ' Coluna: ' + coluna)

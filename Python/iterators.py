jogos = ['Elden Ring', 'Horizon Forbidden West', 'Forspoken', 'Final Fantasy XVI', 'God of War Ragnarök', 'Pragmata']
itJogos = iter(jogos)

while True:
    try:
        print(next(itJogos))
    except StopIteration:
        print('\nAcabou os elementos')
        break

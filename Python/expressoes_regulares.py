import re  # RegEx

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum"

# Findall

print(re.findall("elit", txt))
print(re.findall("li", txt))
print('--------------------------------------')
print("A letra 'A' está presente " + str(len(re.findall("a", txt))) + " vezes no texto")
print('--------------------------------------')

busca = re.findall(input("Pesquise algo: "), txt)
print(str(busca) + "\nEsta palavra está presente " + str(len(busca)) + " vezes no texto")
print('--------------------------------------')

for elemento in busca:
    print(elemento)

print('\n--------------------------------------\n')

# Search

print("Índice de início: " + str(re.search('dolor', txt).start()))
print("Índice de fim: " + str(re.search('dolor', txt).end()))
print("Tamanho da palavra: " + str(re.search('dolor', txt).end() - re.search('dolor', txt).start()))

print('\n--------------------------------------\n')

# Split

print(re.split("li", txt))
print(re.split('li', txt)[2])

print('\n--------------------------------------\n')

# Sub

print(re.sub(" ", "-", txt))
print(re.sub(",", ";", re.sub(" ", "-", txt)))

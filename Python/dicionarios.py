# Dicionários

time = {'nome': 'bayern', 'pais': 'alemanha', 'cor_camisa': "vermelho", 'pontuacao': 10, 'posicao': 1}

print(time['pontuacao'])
print(time['cor_camisa'])
print("O time da " + time['pais'].title() + ", o " + time['nome'].title() + ", possui " + str(time['pontuacao']) + " pontos")
print(time)
print("--------------------------------------")

time['champions'] = 6 # Adicionar
print("O " + time['nome'].title() + " possui " + str(time['champions']) + " títulos da Champions League")
print("--------------------------------------")

del time['cor_camisa'] # Deletar
print(time)
print("--------------------------------------")

# método itens acessa o dicionario
for atributo, valor in time.items():
    if atributo == 'pontuacao':
        time['pontuacao'] = valor + 3
        print("O " + time['nome'].title() + " possui " + str(time['pontuacao']) + " pontos")
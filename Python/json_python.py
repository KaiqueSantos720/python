import json


jogos_json = "{'nome': 'Final Fantasy VII', 'plataforma': 'PS5', 'ano': '2020'}"
jogos_dictionary = {'nome': 'Final Fantasy VII', 'plataforma': 'PS5', 'ano': '2020'}

jogos = json.loads(json.dumps(jogos_json))
jogos_json = json.dumps(jogos_dictionary, indent=4, separators=(":", " = "), sort_keys=True)

print(jogos)
print(jogos_json)
print("\nO nome do jogo é: " + jogos[10:27] + "\n")

jogos_lista = ['God of War', 'Bloodborne', 'FInal Fantasy VII']
jogos_tupla = ('God of War', 'Bloodborne', 'FInal Fantasy VII')

jogos_json = json.dumps(jogos_lista)
print(jogos_json)
jogos_json = json.dumps(jogos_tupla)
print(jogos_json)

# dictionary é convertido em objeto json
# lista é convertida em array json
# tupla é convertida em array json

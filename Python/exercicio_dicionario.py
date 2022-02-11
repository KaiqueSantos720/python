palavras = {
    'input': 'inseção de dados através do teclado',
    'print': "exibição de dados na tela",
    'append': 'insere dado no fim da lista',
    'sort': 'ordena em ordem alfabética uma lista',
    'string': 'tipo de dado texto'
}

palavra = input("Qual palavra você quer consultar no dicionário?")
if palavra.lower() in palavras:
    print(palavras[palavra.lower()])
else:
    print("Palavra não está presente no dicionário")

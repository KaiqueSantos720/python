import re
import os

# r = read - abrir para leitura do arquivo
# a = append - anexar algo ao arquivo
# w = write - escrever no arquivo
# x = create - criar um arquivo
# t = text - modo de texto
# b = binary - modo binário

nome_arquivo = 'texto.txt'
file = open('C:/Users/Windows 10 Pro/PycharmProjects/pythonProject1/Python/' + nome_arquivo, 'wt')

file.write('Salve salve, tudo bem? \nolá mundo')

texto = input('Digite um texto: \n')

file.write("\n" + texto)

file.close()

file = open('C:/Users/Windows 10 Pro/PycharmProjects/pythonProject1/Python/' + nome_arquivo, 'rt')

print("\n" + re.sub(' ', '-', file.read()))

file.close()


if os.path.exists('C:/Users/Windows 10 Pro/PycharmProjects/pythonProject1/Python/' + "txt.txt"):
    print('\nArquivo existente')
else:
    print("\nCriando arquivo")
    file2 = open('C:/Users/Windows 10 Pro/PycharmProjects/pythonProject1/Python/' + "txt.txt", 'x')
    file2.close()

if os.path.exists('C:/Users/Windows 10 Pro/PycharmProjects/pythonProject1/Python/' + "txt.txt"):
    os.remove('C:/Users/Windows 10 Pro/PycharmProjects/pythonProject1/Python/' + "txt.txt")
    print('\nArquivo Excluído')
else:
    print('Arquivo inexistente')
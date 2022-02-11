# Break Continue

while True:
    print("Para encerrar o programa digite 'sair' ")
    time = input("Digite o time que você torce: ")
    if time.lower() == 'continuar':
        continue # não sai do laço de repetição
    elif time.lower() == 'sair':
        print("Programa Encerrado")
        break # sai do laço de repetição
    else:
        print("O time digitado foi: " + time.title())
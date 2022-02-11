def tipo(elemento):
    if type(elemento) is int:
        print('\ntudo certo')
    else:
        print('\ntipo inválido')


numero = 'kaique'
tipo(numero)
numero = 2020
tipo(numero)

fim = True
while True:
    try:
        print('\nO resultado é: ' + str(
            float(input('\nDigite o numerador: ')) / float(input('\nDigite o denominador: '))))
        fim = False
        break
    except ZeroDivisionError:
        print('\nO numerador não pode ser 0')
    except ValueError:
        print('\nEntrada errada')
    finally:
        if fim:
            print('\nO programa rodará novamente')
        else:
            print('\nPrograma Encerrado')

variavel = "Bayern" #String
variavel = False #Boolean
variavel = 10 #Inteiro
variavel = 10.4 #Float
numero1 = 5
numero2 = 2
numero3 = complex(numero1, numero2)
print(numero3.real)
print(numero3.imag)
print(numero3)

print("Valor: " + str(variavel))
print("Tipo: " + str(type(variavel)))

lista = ["Liverpool", "Chelsea", "Manchester United", "Manchester City", "Tottenham", "Arsenal", 3, 4.5, True]
print(lista[4])
print(lista[8])
tupla = (1, "Kaique", "Estudante")
print(tupla)
array = range(0, 100, 1)

dictionary = {
    "nome":"Kaique",
    "idade":17,
}

print(dictionary.keys())
print(dictionary.values())
print(dictionary["idade"])

set1 = {3,5,6,7,8,5,3,5}
set2 = frozenset({3, 5, 6, 7, 8, 5, 3, 5})
print(set1)
print(set2)
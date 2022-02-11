nome1 = "kaique"
nome2 = "santos"
nome_completo = format(nome1 + " " + nome2)

print(nome_completo)
print(nome_completo.title())
print(nome_completo.upper())
print(nome_completo.lower())

print("Olá " + nome_completo.title() + ", tudo bem?")
print("Olá %s, tudo bem?" % nome_completo)

num = 55.5
num2 = 67
print(str(num) + " " + str(num2))

time = "               Manchester United            "
print(time)
print(time.lstrip())
print(time.rstrip())
print(time.rstrip().lstrip())

time2 = "Chelsea"
time3 = "       liverpool"

print(time.rstrip().lstrip() + "\n" + time2 + "\n" + time3.title().lstrip())

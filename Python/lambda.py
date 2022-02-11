multiplicacao = lambda v1, v2: v1 * v2

print(multiplicacao(3, 5))

expr = lambda v1, v2, v3: (v2 - v1) / v3

print(expr(21, 7, 2))

(lambda primeiro_nome, segundo_nome: print(primeiro_nome.title() + ' ' + segundo_nome.title()))('kaique', 'santos')
print((lambda v1, v2, func: v1 + func(v2))(2, 5, lambda v2: v2 * 10))

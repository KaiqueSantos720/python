import sqlite3
from sqlite3 import Error


# Conectar o banco


def conexao_banco():
    conexao = None
    try:
        conexao = sqlite3.connect('C:\\Users\\Windows 10 Pro\\PycharmProjects\\pythonProject1\\Python\\agenda_database')
    except Error as er:
        print(er)
    return conexao


# Criar tabela


vsql = '''CREATE TABLE tb_contatos(
            n_idcontato integer primary key autoincrement,
            t_nomecontato varchar(30),
            t_telefonecontato varchar(30),
            t_emailcontato varchar(30)
        );'''


def criar_tabela(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print('\nTabela Criada')
    except Error as er:
        print(er)


criar_tabela(conexao_banco(), vsql)


# Inserir dados

def inserir_dados(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()  # persistencia do registro dentro do banco
        print('\nRegistro Inserido')
    except Error as er:
        print(er)


while True:
    continua = input('\nDeseja inserir dados na tabela contatos ? ----- "s" ou "n"\n')
    if continua.lower() == 's':
        vsql = "insert into tb_contatos(t_nomecontato, t_telefonecontato, t_emailcontato)" \
               "values('" + input('\nDigite o nome: ') + "', '" + input("\nDigite o telefone: ") + "', '" + input("\nDigite o email: ") + "')"
        inserir_dados(conexao_banco(), vsql)
    elif continua.lower() == 'n':
        print('\nLoop Encerrado')
        break
    else:
        print('\nOpção Inválida')


# Deletar dados

def deletar_dados(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()  # persistencia do registro dentro do banco
        print('\nRegistro Deletado')
    except Error as er:
        print(er)


while True:
    continua = input('\nDeseja deletar dados na tabela contatos ? ----- "s" ou "n"\n')
    if continua.lower() == 's':
        vsql = "delete from tb_contatos where n_idcontato = "+input('\nDigite o id do registro que será deletado: ')+""
        deletar_dados(conexao_banco(), vsql)
    elif continua.lower() == 'n':
        print('\nLoop Encerrado')
        break
    else:
        print('\nOpção Inválida')


# Atualizar dados

def atualizar_dados(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()  # persistencia do registro dentro do banco
        print('\nRegistro Atualizado')
    except Error as er:
        print(er)


while True:
    continua = input('\nDeseja atualizar dados na tabela contatos ? ----- "s" ou "n"\n')
    if continua.lower() == 's':
        vsql = "update tb_contatos set n_idcontato = "+input('\nDigite o novo ID: ')+" where n_idcontato = "+input('\nDigite o ID ATUAL do registro que será alterado: ')+""
        atualizar_dados(conexao_banco(), vsql)
    elif continua.lower() == 'n':
        print('\nLoop Encerrado')
        break
    else:
        print('\nOpção Inválida')


# Consultar dados

def consultar_dados(conexao, sql):
    cursor = conexao.cursor()
    cursor.execute(sql)

    return cursor.fetchall()


while True:
    continua = input('\nDeseja consultar dados na tabela contatos ? ----- "s" ou "n"\n')
    if continua.lower() == 's':
        while True:
            try:
                vsql = "" + input('\nDigite a query da consulta: ') + ""
                for dado in consultar_dados(conexao_banco(), vsql):
                    print(dado)
                break
            except Error as er:
                print("\nQuery Inválida")
                print()
    elif continua.lower() == 'n':
        print('\nLoop Encerrado')
        break
    else:
        print('\nOpção Inválida')


print('\n\nPrograma Encerrado')

conexao_banco().close()

import sqlite3
from sqlite3 import Error

# Conexão com banco de dados


def conexao_banco():
    return sqlite3.connect('C:\\Users\\Windows 10 Pro\\PycharmProjects\\pythonProject1\\Python\\times.db')


# Criar a tabela

vsql = '''CREATE TABLE tb_times (
            id_time          INTEGER      PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome_time        VARCHAR (30) NOT NULL,
            pais_time        VARCHAR (20),
            cidade_time      VARCHAR (20),
            liga             VARCHAR (15) NOT NULL,
            jogador_destaque VARCHAR (30) );
        '''


def criar_tabela(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print('\nTabela Criada')
    except Error as er:
        print(er)


criar_tabela(conexao_banco(), vsql)


def menu():
    return input('\n1 - Inserir Registro\n2 - Deletar Registro\n3 - Atualizar Registro\n4 - Consultar Registro\n5 - '
                 'Sair\n\nDigite uma opção: ')


def query(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()  # atualizar a base de dados com as devidas atualizações
        print('\nOperação Realizada com Sucesso')
    except Error as er:
        print(er)


def consulta(conexao, sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    return cursor.fetchall()  # retorna o resultado da consulta


def inserir():
    variavel_sql = "INSERT INTO tb_times (nome_time, pais_time, cidade_time, liga, jogador_destaque)" \
               "VALUES('" + input('\nDigite o nome do time: ') + "', '" + input("\nDigite o país da equipe: ") + "', '"\
                   + input("\nDigite a cidade do time: ") + "', '" + input("\nDigite a liga que o clube disputa: ") + \
                   "', '" + input("\nDigite o principal jogador da equipe: ") + "')"
    query(conexao_banco(), variavel_sql)


def deletar():
    variavel_sql = "delete from tb_times where id_time = "+input('\nDigite o id do registro que será deletado: ')+""
    query(conexao_banco(), variavel_sql)


def atualizar():
    op = input('\nO que deseja alterar ?\n1 - Nome do Time\n2 - País do Time\n3 - Cidade do Time\n4 - Liga do Time\n5 '
               '- Jogador de Destaque\n')
    if op == '1':
        query(conexao_banco(), "update tb_times set nome_time = '" + input(
            '\nDigite o novo nome do time: ') + "' where id_time = '" + input(
            '\nDigite o id do registro que deseja alterar: ') + "'")
    elif op == '2':
        query(conexao_banco(), "update tb_times set pais_time = '" + input(
            '\nDigite o novo país do time: ') + "' where id_time = '" + input(
            '\nDigite o id do registro que deseja alterar: ') + "'")
    elif op == '3':
        query(conexao_banco(), "update tb_times set cidade_time = '" + input(
            '\nDigite a nova cidade do time: ') + "' where id_time = '" + input(
            '\nDigite o id do registro que deseja alterar: ') + "'")
    elif op == '4':
        query(conexao_banco(), "update tb_times set liga = '" + input(
            '\nDigite a nova liga do time: ') + "' where id_time = '" + input(
            '\nDigite o id do registro que deseja alterar: ') + "'")
    elif op == '5':
        query(conexao_banco(), "update tb_times set jogador_destaque = '" + input(
            '\nDigite o novo jogador de destaque: ') + "' where id_time = '" + input(
            '\nDigite o id do registro que deseja alterar: ') + "'")
    else:
        print('\nOpção Inválida')


def consultar():
    try:
        for dado in consulta(conexao_banco(), input('\nDigite a query da consulta: \n')):
            print(str(dado).replace(',', ""))
    except Error as er:
        print(er)
        print('\nQuery Inválida')


while True:
    opcao = menu()
    if opcao == '1':
        inserir()
    elif opcao == '2':
        deletar()
    elif opcao == '3':
        atualizar()
    elif opcao == '4':
        consultar()
    elif opcao == '5':
        print('\nPrograma Encerrado')
        break
    else:
        print('\nOpção Inválida')


conexao_banco().close()

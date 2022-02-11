from tkinter import *
import os


def sem():
    print('dfsdf')


def novo_contato():
    exec(open(os.path.dirname(__file__) + "\\tkinter_interface_grafica.py").read())  # abrir nova janela


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

barra_menu = Menu(programa)
menu_contatos = Menu(barra_menu, tearoff=0)
menu_contatos.add_command(label="Novo", command=novo_contato)  # novo registro
menu_contatos.add_command(label="Pesquisar", command=sem)  # pesquisar registro
menu_contatos.add_command(label="Deletar", command=sem)  # deletar registro
menu_contatos.add_separator()  # barra separadora
menu_contatos.add_command(label="Fechar", command=programa.quit)  # sair do programa

barra_menu.add_cascade(label="Clubes", menu=menu_contatos)

menu_manutencao = Menu(barra_menu, tearoff=0)
menu_manutencao.add_command(label="Banco de Dados", command=sem)
barra_menu.add_cascade(label="Manutenção", menu=menu_manutencao)

menu_sobre = Menu(barra_menu, tearoff=0)
menu_sobre.add_command(label="Equipes", command=sem)
barra_menu.add_cascade(label="Sobre", menu=menu_sobre)

programa.config(menu=barra_menu)

programa.mainloop()

from tkinter import *
import os
import banco_gravar_dados as bdd


def gravar():
    variavel_sql = "INSERT INTO tb_times (nome_time, pais_time, cidade_time, liga, jogador_destaque)" \
                   "VALUES('" + vnome.get() + "', '" + vpais.get() + "', '" + vcidade.get() + "', '" + vliga.get() \
                   + "', '" + vjog.get() + "') "
    bdd.query(variavel_sql)
    vnome.delete(0, END)
    vpais.delete(0, END)
    vcidade.delete(0, END)
    vliga.delete(0, END)
    vjog.delete(0, END)


programa = Tk()

programa.title("Bayern de Munique")
programa.geometry('1920x1080')  # tamanho da janela
programa.configure(background="#030d62")  # cor da janela

# config das janela, mostrando o elemento pai, e em seguida as config
'''txt1 = Label(programa, text = "Bayern de Munique", background = "#d60000", foreground = "#fff")
txt1.place(x=400, y=0, width=150, height=50)

vtxt = 'Real Madrid'
vbg = '#fff'
vfg = '#f8be11'
txt2 = Label(programa, text = vtxt, background = vbg, foreground = vfg)
txt2.pack(ipadx = 150, ipady = 50, padx = 0, pady = 0, side = 'top', fill = X, expand = True)'''
# indicado quando faz parte de um container

# anchor - pontos cardeais
# além do Entry, existe o Text que adiciona texto com várias linhas - texto grande

Label(programa, text="Nome: ", background="#dde", foreground="#009", anchor=W).place(x=500, y=150, width=200, height=50)
vnome = Entry(programa)  # entrada de texto de 1 linha
vnome.place(x=650, y=150, width=200, height=50)

Label(programa, text="Pais: ", background="#dde", foreground="#009", anchor=W).place(x=500, y=250, width=200, height=50)
vpais = Entry(programa)  # entrada de texto de 1 linha
vpais.place(x=650, y=250, width=200, height=50)

Label(programa, text="Cidade: ", background="#dde", foreground="#009", anchor=W).place(x=500, y=350, width=200,
                                                                                       height=50)
vcidade = Entry(programa)  # entrada de texto de 1 linha
vcidade.place(x=650, y=350, width=200, height=50)

Label(programa, text="Liga: ", background="#dde", foreground="#009", anchor=W).place(x=500, y=450, width=200, height=50)
vliga = Entry(programa)  # entrada de texto de 1 linha
vliga.place(x=650, y=450, width=200, height=50)

Label(programa, text="Jogador de Destaque: ", background="#dde", foreground="#009", anchor=W).place(x=500, y=550,
                                                                                                    width=200,
                                                                                                    height=50)
vjog = Entry(programa)  # entrada de texto de 1 linha
vjog.place(x=650, y=550, width=200, height=50)

Button(programa, text="gravar", command=gravar).place(x=650, y=650, width=100, height=30)

programa.mainloop()  # execução do programa

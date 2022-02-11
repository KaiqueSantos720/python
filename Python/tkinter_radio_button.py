from tkinter import *


def imprimir_equipe():
    if vtime.get() == 'f':
        print('Real Madrid')
    elif vtime.get() == 'b':
        print('Bayern de Munique')
    elif vtime.get() == 'm':
        print('Milan')
    else:
        print("Selecione um time")


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

vtime = StringVar()
vjog = StringVar()

lbl_equipes = Label(programa, text="Equipes")
lbl_equipes.pack()

rb_real = Radiobutton(programa, text="Real Madrid", value="f", variable=vtime)  # criação do raio button
rb_real.pack()

rb_bayern = Radiobutton(programa, text="Bayern de Munique", value="b", variable=vtime)  # criação do raio button
rb_bayern.pack()

rb_milan = Radiobutton(programa, text="Milan", value="m", variable=vtime)  # criação do raio button
rb_milan.pack()

rb_ibra = Radiobutton(programa, text="Ibrahimovic", value="i", variable=vjog)  # criação do raio button
rb_ibra.pack()

rb_lewa = Radiobutton(programa, text="Lewandowski", value="l", variable=vjog)  # criação do raio button
rb_lewa.pack()

btn_equipes = Button(programa, text="Equpe Selecionada", command=imprimir_equipe)
btn_equipes.pack()

programa.mainloop()

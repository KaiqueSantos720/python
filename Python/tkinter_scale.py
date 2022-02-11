from tkinter import *


def definir_valor():
    scale.set(numero.get())


def valor():
    print(scale.get())


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

numero = IntVar()

label = Label(programa, text="Valor")
label.pack()

scale = Scale(programa, from_=0, to=50, orien=HORIZONTAL)
scale.set(25)
scale.pack()

botao = Button(programa, text="Valor Selecionado", command=valor)
botao.pack()

entrada = Entry(programa, textvariable=numero)
entrada.pack()

botao2 = Button(programa, text="Selecionar valor", command=definir_valor)
botao2.pack()

programa.mainloop()

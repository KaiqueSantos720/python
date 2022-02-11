from tkinter import *
from tkinter import ttk


def imprimir_esporte():
    print(combobox.get())


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

lista = ['Bayern', 'Liverpool', 'Milan']

label = Label(programa, text="equipes")
label.pack()

combobox = ttk.Combobox(programa, values=lista)
combobox.set("Liverpool")  # define o elemento selecionado
combobox.pack()

botao = Button(programa, text="Clube Selecionado", command=imprimir_esporte)
botao.pack()

programa.mainloop()

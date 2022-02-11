from tkinter import *


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

label1 = Label(programa, text="Nome da Equipe: ")
label2 = Label(programa, text="País da Equipe: ")
label3 = Label(programa, text="Cidade da Equipe: ")

entrada1 = Entry(programa)
entrada2 = Entry(programa)
entrada3 = Entry(programa)

botao = Button(programa, text="Equipes")
botao.grid(column=0, row=12, sticky="w")
label1.grid(column=0, row=0, sticky='w')
label2.grid(column=0, row=4, sticky='w')
label3.grid(column=0, row=7, sticky='w')

entrada1.grid(column=0, row=1)
entrada2.grid(column=0, row=5)
entrada3.grid(column=0, row=8)  # N, S, E, W

programa.mainloop()

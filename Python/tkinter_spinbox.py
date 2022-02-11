from tkinter import *


def imprimir():
    print(spinbox.get())
    print(spinbox2.get())


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

spinbox = Spinbox(programa, from_=0, to=75)
spinbox.pack()

spinbox2 = Spinbox(programa, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
spinbox2.pack()

botao = Button(programa, text="Imprimir Valor", command=imprimir)
botao.pack()

programa.mainloop()

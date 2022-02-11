from tkinter import *


def imprimir():
    print("Senha Digitada: " + senha.get())
    password.delete(0, END)


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

senha = StringVar()

password = Entry(programa, textvariable=senha, show="*")
password.pack()

botao = Button(programa, text="Imprimir Senha", command=imprimir)
botao.pack()


programa.mainloop()

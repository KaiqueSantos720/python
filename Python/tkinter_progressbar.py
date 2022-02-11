from tkinter import *
from tkinter import ttk


def setar_barra(maximo):
    contador = 0
    etapas = maximo / 100
    while contador < etapas:
        contador += 1
        i = 0
        while i < 1000000:
            i += 1
        barra.set(contador)
        programa.update()


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

barra = DoubleVar()
barra.set(0)

progressbar = ttk.Progressbar(programa, variable=barra, maximum=100)
progressbar.place(x=0, y=0, width=1920, height=20)

botao = Button(programa, text="Setar Barra", command=lambda: setar_barra(10000))
botao.place(x=800, y=200)

programa.mainloop()

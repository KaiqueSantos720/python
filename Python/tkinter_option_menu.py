from tkinter import *


def imprimir_equipe():
    if vtime.get() == 'Chelsea':
        print('Chelsea')
    elif vtime.get() == 'Bayern':
        print('Bayern de Munique')
    elif vtime.get() == 'Juventus':
        print('Juventus')
    else:
        print("Selecione um time")


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

lista_times = ['Bayern', 'Chelsea', 'Juventus']

vtime = StringVar()
vtime.set(lista_times[0])  # valor padrão

lbl_equipes = Label(programa, text="Equipes")
lbl_equipes.pack()

option_time = OptionMenu(programa, vtime, *lista_times)
option_time.pack()

btn_equipes = Button(programa, text="Equpe Selecionada", command=imprimir_equipe)
btn_equipes.pack()

programa.mainloop()

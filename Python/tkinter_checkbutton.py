from tkinter import *


def fut():
    print('Futebol: ' + str(v_fut.get()))


def vol():
    print('Vôlei: ' + str(v_vol.get()))


def bas():
    print('Basquete: ' + str(v_bas.get()))


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

v_fut = IntVar()
v_vol = IntVar()
v_bas = IntVar()

quadro = Frame(programa, borderwidth=1, relief="solid")
quadro.place(x=200, y=200, width=300, height=300)

cb_futebol = Checkbutton(quadro, text="Futebol", variable=v_fut, onvalue=1, offvalue=0, command=fut)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(quadro, text="Vôlei", variable=v_vol, onvalue=1, offvalue=0, command=vol)
cb_volei.pack(side=LEFT)

cb_basquete = Checkbutton(quadro, text="Basquete", variable=v_bas, onvalue=1, offvalue=0, command=bas)
cb_basquete.pack(side=LEFT)


programa.mainloop()

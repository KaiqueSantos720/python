from tkinter import *
from tkinter import messagebox


def mostrar_mensagem():
    messagebox.showinfo('Equipes', message="Equipes Europeias")


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

numero_texto = StringVar()

frame_quadro1 = Frame(programa, borderwidth=1, relief="solid", background="#f00")
# relief - (flat, raised, sunken, solid)
frame_quadro1.place(x=400, y=10, width=300, height=100)

frame_quadro2 = Frame(programa, borderwidth=1, relief="solid", background="#00f")
# relief - (flat, raised, sunken, solid)
frame_quadro2.place(x=400, y=200, width=300, height=100)

Label(frame_quadro1, text="Tipo de caixa, (1 --- 2 --- 3)").pack()
numero = Entry(frame_quadro1, textvariable=numero_texto)
numero.pack()
numero_texto.set('1')

botao = Button(frame_quadro1, text="Mostrar Mensagem", command=mostrar_mensagem)
botao.pack()

lb_clube = Label(frame_quadro2, text="Bayern", background="#f00", foreground="#fff", font=("Times New Roman", 15))
lb_clube.pack(side=LEFT, fill=X, expand=True) # Centralizado

programa.mainloop()

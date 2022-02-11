from tkinter import *


def imprimir():
    print(listbox.get(ACTIVE))


def inserir():
    listbox.insert(END, novo_jogo.get())
    novo_jogo.delete(0, END)


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

lista_jogos = ["God of War", "Bloodborne", "Resident Evil", "Ghost of Tsushima", "Shadow of the Colossus"]

listbox = Listbox(programa)
for jogo in lista_jogos:
    listbox.insert(END, jogo)
listbox.place(x=500, y=200, width=800, height=800)


botao = Button(programa, text="Imprimir Jogo", command=imprimir)
botao.place(x=500, y=1050)

novo_jogo = Entry(programa)
novo_jogo.pack()

botao2 = Button(programa, text="Inserir Jogo", command=inserir)
botao2.pack()


programa.mainloop()

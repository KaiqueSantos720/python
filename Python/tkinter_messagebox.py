from tkinter import *
from tkinter import messagebox


def mostrar_mensagem(tipo_mensagem, mensagem):
    if tipo_mensagem == '1':
        messagebox.showinfo('Equipes', message=mensagem)
    elif tipo_mensagem == '2':
        messagebox.showwarning('Equipes', message=mensagem)
    elif tipo_mensagem == '3':
        messagebox.showerror('Equipes', message=mensagem)


def reseta_textbox():
    res = messagebox.askyesno("Resetar", "Confirmar Reset?")
    # askoscancel = ok, cancel
    # askretrycancel - repetir, cancelar
    # asktesnocancel - sim, não, cancelar
    if res:
        numero.delete(0, END)
        numero.insert(0, '1')


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

numero_texto = StringVar()
vmensagem = "Equipes Inválidas"

Label(programa, text="Tipo de caixa, (1 --- 2 --- 3)").pack()
numero = Entry(programa, textvariable=numero_texto)
numero.pack()
numero_texto.set('1')

botao = Button(programa, text="Mostrar Mensagem", command=lambda: mostrar_mensagem(numero_texto.get(), vmensagem))
botao.pack()

botao_reset = Button(programa, text="Resetar Mensagem", command=reseta_textbox)
botao_reset.pack()

programa.mainloop()

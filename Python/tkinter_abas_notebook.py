from tkinter import *
from tkinter import ttk


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

notebook = ttk.Notebook(programa)
notebook.place(x=10, y=10, width=500, height=300)

frame1 = Frame(notebook)
notebook.add(frame1, text="Equipes Inglesas")

frame2 = Frame(notebook)
notebook.add(frame2, text="Equipes Alemãs")

label1 = Label(frame1, text="Manchester United")
label1.pack()

label2 = Label(frame2, text="Bayern de Munique")
label2.pack()

label3 = Label(frame1, text="Manchester City")
label3.pack()

label4 = Label(frame2, text="Leipzig")
label4.pack()

programa.mainloop()

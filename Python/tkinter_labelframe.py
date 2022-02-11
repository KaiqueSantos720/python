from tkinter import *


programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

label = LabelFrame(programa, text="Equipes", borderwidth=1, relief="solid", foreground="#000")
label.place(x=200, y=200, width=600, height=600)

label1 = Label(label, text="Bayern")
label1.pack()

label2 = Label(label, text="Chelsea")
label2.pack()

label3 = Label(label, text="Tottenham")
label3.pack()


programa.mainloop()

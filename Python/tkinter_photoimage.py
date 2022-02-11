from tkinter import *
import os

caminho = os.path.dirname(__file__)

programa = Tk()
programa.geometry('1920x1080')
programa.configure(background="#030d62")

img_jogo = PhotoImage(file=caminho+"\\ds.png")
label_img_jogo = Label(programa, image=img_jogo)
label_img_jogo.pack(side=LEFT, fill=X, expand=True)

programa.mainloop()

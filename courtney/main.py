# kesha.courtney.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, INVENTARIO
from browser import html, document, alert, doc
from _spy.vpython.main import *
from Tkinter import*
janela = Tk()

def name(event):
    print ("olá")
janela.geometry("100x300+100+100")
botao1 = Button(janela,Text = "Tenta Novamente a fase")
botao1.bind ("<Button-1>", name)
botao1.pack()
janela.mainloop()

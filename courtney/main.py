# kesha.courtney.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, INVENTARIO
from browser import html, document, alert, doc, Tkinder
from _spy.vpython.main import *
#from Tkinter import*
#janela = Tk()

#def name(event):
 #   print ("olá")
#janela.geometry("100x300+100+100")
#botao1 = Button(janela,Text = "Tenta Novamente a fase")
#botao1.bind ("<Button-1>", name)
#botao1.pack()
#janela.mainloop()

class botoes():
    def frameBotoesTelaInicial(self):
            self.frame1= tk.Frame()
            btn1= tk.Button(master=self.frame1, text="Tentar novamente esta fase", command= self.processaInserir).pack(side=tk.LEFT, padx= 20, pady= 20)
            btn2= tk.Button(master=self.frame1, text="Não quero jogar", command= self.processaPesquisar).pack(side=tk.LEFT, padx= 20, pady= 20)
            btn3= tk.Button(master=self.frame1, text="Desisto",command= self.processaEditar).pack(side=tk.LEFT, padx= 20, pady= 20)
            btn3= tk.Button(master=self.frame1, text="Terminei mas acho que está errado",command= self.processaListar).pack(side=tk.LEFT, padx= 20, pady= 20)
            return self.frame1       
         
    def create_canvas_area(self):
        lbl1= tk.Label(self.root, text="Sistema Gerenciador de Componentes do Caderno", font=("Helvetica", 20, "bold"), fg="blue").pack()

        self.frameBotoesTelaInicial().pack()
             
             
"""def processaInserir(self):
    tkmsg.showinfo("Botão pressionado","Botão Inserir")
         
def processaPesquisar(self):
    tkmsg.showinfo("Botão pressionado","Botão Pesquisar")       

def processaEditar(self):
    tkmsg.showinfo("Botão pressionado","Botão Editar")

def processaListar(self):
    tkmsg.showinfo("Botão pressionado","Botão Listar")
"""
botoes()
from tkinter import *
from playsound import playsound
from gtts import *
import os


root = Tk()
root.title('Conversor de Texto para fala')
root.geometry('450x450')
root.iconbitmap('micro1.ico')
root.maxsize(450, 450)
root.minsize(450, 450)
root.configure(bg='black')
def go():
    dados = ent.get()
    fala = gTTS(text=dados, lang='pt', tld='com.br')
    arquivo_fala = 'salvo.mp3'
    fala.save(arquivo_fala)
    playsound(arquivo_fala)

def go1():
    ent.delete(0, END)
    os.remove('salvo.mp3')
titulo = Label(bg='black', fg = '#e827ea', font=('gabriola', 20), text='Conversor de Texto para Fala')
titulo.place(x=115, y=25)

inserir = Label(bg='black', fg = 'White', font=('gabriola', 20), text='Insira o texto: ')
inserir.place(x=165, y=85)

ent = Entry(root, width=45, borderwidth=4, relief=FLAT, font='Montserrat', justify=CENTER)
ent.place(x=20, y=155)

bt = Button(root, bg='#c69749', fg= 'white', padx=37, pady=10, text='INICIAR', font= 'gabriola', command=go, relief=FLAT)
bt.place(x=170, y=200)

bt1 = Button(root, bg='#c69749', fg= 'white', padx=33, pady=10, text='RESETAR', font= 'gabriola', command=go1, relief=FLAT)
bt1.place(x=170, y=280)


root.mainloop()



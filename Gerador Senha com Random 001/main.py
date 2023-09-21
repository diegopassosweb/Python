from tkinter import *
from tkinter import ttk, Tk, messagebox
from PIL import Image, ImageTk

import string
import random

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#f05a43"  # vermelha

fundo_dark="#484f60"
fundo_claro = "#fff"

fundo = co1

janela = Tk()
janela.title('')
janela.geometry('300x360')
janela.configure(bg=co1)

style = ttk.Style(janela)
style.theme_use('clam')

#dividindo a tela em dois frames
frame_cima = Frame(janela, width=295, height=50,bg=co1, pady=0, padx=0, relief="flat",)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310,bg=co1, pady=0, padx=0, relief="flat",)
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#trabalhando no frame cima
img = Image.open('password.png')
img = img.resize((30, 30))
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief="flat", anchor="nw", bg=co1)
app_logo.place(x=2, y=0)

app_nome = Label(frame_cima, text='GERADOR DE SENHAS', width=20, height=1, padx=0, relief="flat", anchor="nw", bg=co1, fg=co0, font=('Ivy 16 bold'))
app_nome.place(x=35, y=2)

app_linha = Label(frame_cima, text='', width=295, height=1, padx=0, relief="flat", anchor="nw", bg=co3, fg=co0, font=('Ivy 1'))
app_linha.place(x=0, y=35)

#funçao gerar senha
def criar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '(){}[]*;/,_.-+'
    
    global combinar
    
    #condiçao maiusculas
    if estado_1.get() == alfa_maior:
        combinar = alfa_maior
    else:
        pass
    
    #condiçao minusculas
    if estado_2.get() == alfa_menor:
        combinar = combinar + alfa_menor
    else:
        pass
    
    #condiçao maiusculas
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass
    
    #condiçao maiusculas
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass
    
    comprimento = int(spin.get())
    senha = ''.join(random.sample(combinar,  8))
    
    app_senha['text'] = senha
    
    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)
        
        messagebox.showinfo('sucesso', 'A senha foi copiada com sucesso')
        
    button_copiar_senha = Button(frame_baixo, command=copiar_senha, text='Copiar', width=6, height=2, overrelief='solid', relief="raised", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0 )
    button_copiar_senha.grid(row=0, column=1, sticky=NW, padx=5, pady=7, columnspan=1)


#trabalhando no frame baixo
app_senha = Label(frame_baixo, text='-----', width=21, height=2, padx=0, relief="solid", anchor="center", font=('Ivy 12 bold'), bg=co1, fg=co0 )
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, text='Numero Total de Caracteres', height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), bg=co1, fg=co0 )
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8 )

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '(){}[]*;/,_.-+'


frame_caracteres = Frame(frame_baixo, width=295, height=210,bg=co1, pady=0, padx=0, relief="flat",)
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

#letras maiusculas
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfa_maior, offvalue='off', relief='flat', bg=co1)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='ABC Letras maiusculas', height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), bg=co1, fg=co0 )
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

#letras minusculas
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfa_menor, offvalue='off', relief='flat', bg=co1)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='ABC Letras minusculas', height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), bg=co1, fg=co0 )
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

#Numeros
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off', relief='flat', bg=co1)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='123 Numeros', height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), bg=co1, fg=co0 )
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

#Simbolos
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offvalue='off', relief='flat', bg=co1)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='!@# Simbolos', height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), bg=co1, fg=co0 )
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

#Button
button_gerar_senha = Button(frame_caracteres, command=criar_senha, text='Gerar Senha', width=34, height=1, overrelief='solid', relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co3, fg=co1 )
button_gerar_senha.grid(row=5, column=0, sticky=NSEW, padx=5, pady=11, columnspan=5)





janela.mainloop()

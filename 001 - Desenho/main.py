from tkinter import *
from tkinter import ttk, Tk

from tkinter import filedialog as fd

import cv2

from PIL import Image, ImageTk

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit

janela = Tk()
janela.title('')
janela.geometry('300x356')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

app_img = Image.open('img.png')
app_img = app_img.resize((50,50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(janela, image=app_img, text='Imagem > Desenho a lapis', width=300, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

global imagem_ori, l_imagem, imagem

imagem_ori = ['']
def escolher_img():
    global imagem_ori, l_imagem, imagem
    imagem = fd.askopenfilename()
    imagem_ori.append(imagem)
    

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(janela, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=60, y=60)

def converter_img():
    global imagem_ori, l_imagem, imagem 
    
    valor_escala = escala.get()

    imagem = cv2.imread(imagem_ori[-1])
    
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    desfoco = cv2.GaussianBlur(imagem_cinza, (21, 21), 0,0) 
    
    lapis = cv2.divide(imagem_cinza, desfoco, scale=valor_escala)
    
    cv2.imwrite('imagem_convertida.png', lapis)
    
    imagem = Image.open('imagem_convertida.png')
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(janela, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=60, y=60)

    

l_opcoes = Label(janela, text='Configuraçoes ---------------------'.upper(), anchor=NW, font=('Verdana 7 bold'), bg=co1, fg=co4)
l_opcoes.place(x=10, y=260)

escala = Scale(janela,command=converter_img, from_=0, to=255, length=120, bg=co1, fg='red', orient=HORIZONTAL)
escala.place(x=10, y=300)

b_escolher = Button(janela,command=escolher_img, text="Escolher imagem",width=15, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co4 )
b_escolher.place(x=147, y=287)

b_salvar = Button(janela, command=converter_img, text="Salvar",width=15, overrelief=RIDGE,  font=('ivy 10'),bg=co2, fg=co1 )
b_salvar.place(x=147, y=317)


janela.mainloop()
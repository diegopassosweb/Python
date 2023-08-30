from tkinter import *
from tkinter import Tk, ttk

from PIL import Image, ImageTk

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  #
co11 = "#f2f4f2"

# criando janela
janela = Tk()
janela.title("")
janela.geometry("250x400")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

# frames
frameCima = Frame(janela, width=300, height=50, bg=co1, relief="flat" )
frameCima.grid(row=0, column=0)
frameMeio = Frame(janela, width=300, height=90, bg=co1, relief="flat" )
frameMeio.grid(row=1, column=0)
frameBaixo = Frame(janela, width=300, height=290, bg=co9, relief="flat" )
frameBaixo.grid(row=2, column=0)

#logo

app_ = Label(frameCima, text='Orçamento', compound=LEFT, padx=5, relief=FLAT, anchor=NW,
font=('Verdana 20'), bg=co1, fg=co4)
app_.place(x=0, y=0)

# abrindo img
app_img = Image.open('log.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW,
font=('Verdana 20'), bg=co1, fg=co4)
app_logo.place(x=160, y=0)

app_linha = Label(frameCima, width=295, relief=FLAT, anchor=NW,
font=('Verdana 1'), bg=co3, fg=co1)
app_linha.place(x=0, y=47)

# funçao
def calcular():
    renda_mensal = float(e_valor.get())

    obter50 = (50 / 100) * renda_mensal
    obter30 = (30 / 100) * renda_mensal
    obter20 = (20 / 100) * renda_mensal

    l_necessidades['text'] = ("R${:,.2f}".format(obter50))
    l_gastos['text'] = ("R${:,.2f}".format(obter30))
    l_poupanças['text'] = ("R${:,.2f}".format(obter20))

    


# frame meio
app_ = Label(frameMeio,text='Digite sua renda mensal', relief=FLAT, anchor=NW,
font=('Ivy 10'), bg=co1, fg=co4)
app_.place(x=7, y=15)

e_valor = Entry(frameMeio, width=10, font=('Ivy 14'), justify='center', relief='solid')
e_valor.place(x=10, y=40)

app_calcular = Button(frameMeio, command=calcular, text='Calcular'.upper(), overrelief=RIDGE, anchor=NW,
font=('Ivy 8'), bg=co1, fg=co0)
app_calcular.place(x=150, y=40)

# frame baixo

app_ = Label(frameBaixo,text='Seus numero de 50% 30% 20%', relief=FLAT, width=35, anchor=NW,
font=('Verdana 11'), bg=co3, fg=co1)
app_.place(x=0, y=0)

# total necessidades
l_totalnecessidades = Label(frameBaixo,text='Necessidades', relief=FLAT, width=35, anchor=NW,
font=('Verdana 10'), bg=co9, fg=co0)
l_totalnecessidades.place(x=10, y=40)

l_necessidades = Label(frameBaixo, relief=FLAT, width=22, anchor=NW,
font=('Verdana 12'), bg=co1, fg=co4)
l_necessidades.place(x=10, y=75) 

# total gastos
l_totalgastos = Label(frameBaixo,text='Gastos', relief=FLAT, width=35, anchor=NW,
font=('Verdana 10'), bg=co9, fg=co0)
l_totalgastos.place(x=10, y=115)

l_gastos = Label(frameBaixo, relief=FLAT, width=22, anchor=NW,
font=('Verdana 12'), bg=co1, fg=co4)
l_gastos.place(x=10, y=145) 

# total poupanças
l_totalpoupanças = Label(frameBaixo,text='Poupanças', relief=FLAT, width=35, anchor=NW,
font=('Verdana 10'), bg=co9, fg=co0)
l_totalpoupanças.place(x=10, y=185)

l_poupanças = Label(frameBaixo, relief=FLAT, width=22, anchor=NW,
font=('Verdana 12'), bg=co1, fg=co4)
l_poupanças.place(x=10, y=215) 




janela.mainloop()
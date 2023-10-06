
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# cores
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

# funcao calcular a regra 50 30 20
def calcular():
    # valores a serem inseridos
    Renda_mensal_apos_impostos = float(e_valor_quantia.get())

    # Obtendo as percentagens
    obter_50_percento = (50 / 100) * Renda_mensal_apos_impostos
    obter_30_percento = (30 / 100) * Renda_mensal_apos_impostos
    obter_20_percento = (20 / 100) * Renda_mensal_apos_impostos

    l_necessidades['text'] = 'R${:,.2f}'.format(obter_50_percento)
    l_quer['text'] = 'R${:,.2f}'.format(obter_30_percento )
    l_poupanca['text'] = 'R${:,.2f}'.format(obter_20_percento)


janela = Tk()
janela.title('')
janela.geometry('250x400')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

frameCima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=300, height=90, bg=co1, relief="solid")
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela, width=300, height=290, bg=co9, relief="raised")
frameBaixo.grid(row=2, column=0)

#logo
app_ = Label(frameCima, text='Orçamento', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'), bg=co1, fg=co4)
app_.place(x=0, y=0)

app_img = Image.open('log.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=160, y=0)

l_linha = Label(frameCima, width=295, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=0, y=47)

# Frame Meio --------------------------------------------------
l_valor_quantia = Label(frameMeio, text="Renda mensal após impostos?", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_valor_quantia.place(x=7, y=15)
e_valor_quantia = Entry(frameMeio, width=10, font=('Ivy 14 '), justify='center',relief="solid")
e_valor_quantia.place(x=10, y=40)

botao_calcular = Button(frameMeio,anchor=NW, command=calcular, text=" Calcular".upper(), overrelief=RIDGE,  font=('ivy 9 '),bg=co1, fg=co0 )
botao_calcular.place(x=150, y=40)


# Frame Baixo -------------------------------------------------------
l_nome = Label(frameBaixo, text="Seus números de 50/30/20:",padx=10, width=35, height=1,anchor=NW, font=('Verdana 11 '), bg=co3, fg=co1)
l_nome.place(x=0, y=0)

# Total necessidades -----------------------------------
l_total_necessidades = Label(frameBaixo, text="Necessidades", height=1,anchor=E, font=('Verdana 10 '), bg=co9, fg=co0)
l_total_necessidades.place(x=10, y=40)

l_necessidades = Label(frameBaixo,width=22, height=1,anchor=NW, font=('Verdana 12 '), bg=co1, fg=co4)
l_necessidades.place(x=10, y=75)

# Total Quer -----------------------------------
l_total_quer = Label(frameBaixo, text="Quer: ", height=1,anchor=E, font=('Verdana 10 '), bg=co9, fg=co0)
l_total_quer.place(x=10, y=115)

l_quer = Label(frameBaixo, width=22, height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
l_quer.place(x=10, y=145)

# Total Poupança-----------------------------------
l_total_poupanca = Label(frameBaixo, text="Poupança e amortização da dívida:", height=1,anchor=E, font=('Verdana 10 '), bg=co9, fg=co0)
l_total_poupanca.place(x=10, y=185)

l_poupanca = Label(frameBaixo, width=22, height=1,anchor=NW, font=('Verdana 12 '), bg=co1, fg=co4)
l_poupanca.place(x=10, y=215)





janela.mainloop()
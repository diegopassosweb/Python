
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, ttk
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

janela = Tk()
janela.title('')
janela.geometry('380x500')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

frameCima = Frame(janela, width=380, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2)

frameBaixo = Frame(janela, width=380, height=400, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=10)

frameResultado = Frame(janela, width=364, height=50, bg=co3, relief="flat")
frameResultado.grid(row=1, column=0, pady=10)

frameAtivos = Frame(frameBaixo, width=180, height=370, bg=co9, relief="flat")
frameAtivos.grid(row=0, column=0, pady=0, padx=5)

framePassivos = Frame(frameBaixo, width=180, height=370, bg=co9, relief="flat")
framePassivos.grid(row=0, column=1, pady=0)

app_img = Image.open('logo.png')
app_img = app_img.resize((50,50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text='Calculadora de patrimonio liquido', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Ivy 12'), bg=co1, fg=co4)
app_.place(x=50, y=0)

l_linha = Label(frameCima, width=380, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=0, y=47)


l_nome = Label(frameAtivos, text='Insira ativos', padx=10, width=35, height=1, anchor=NW, font=('Verdana 11'), bg=co2, fg=co1)
l_nome.place(x=0, y=0)

l_casa = Label(frameAtivos, text='Valor da casa', height=1, anchor=E, font=('Verdana 9'), bg=co9, fg=co0)
l_casa.place(x=10, y=40)

e_valor_casa = Entry(frameAtivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_casa.place(x=10, y=65)

l_imoveis = Label(frameAtivos, text='Imoveis', height=1, anchor=E, font=('Verdana 9'), bg=co9, fg=co0)
l_imoveis.place(x=10, y=105)

e_valor_imovel = Entry(frameAtivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_imovel.place(x=10, y=125)

l_veiculos = Label(frameAtivos, text='Veiculos', height=1, anchor=E, font=('Verdana 9'), bg=co9, fg=co0)
l_veiculos.place(x=10, y=165)

e_valor_veiculos = Entry(frameAtivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_veiculos.place(x=10, y=195)

l_investimentos = Label(frameAtivos, text='Investimentos', height=1, anchor=E, font=('Verdana 9'), bg=co9, fg=co0)
l_investimentos.place(x=10, y=230)

e_valor_investimentos = Entry(frameAtivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_investimentos.place(x=10, y=255)


l_ativos = Label(frameAtivos, text="Outros ativos", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_ativos.place(x=10, y=295)

e_outros_ativos = Entry(frameAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_outros_ativos.place(x=10, y=315)


# Entrando Passivos -------------------------------------------------------

l_nome = Label(framePassivos, text="Insira Passivos",padx=10, width=35, height=1,anchor=NW, font=('Verdana 11 '), bg=co5, fg=co1)
l_nome.place(x=0, y=0)

# Hipoteca ($)
l_hipoteca = Label(framePassivos, text="Hipoteca", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_hipoteca.place(x=10, y=40)

e_valor_hipoteca = Entry(framePassivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_hipoteca.place(x=10, y=65)


#  Empréstimos de carro
l_carro = Label(framePassivos, text="Empréstimos de carro", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_carro.place(x=10, y=105)

e_valor_carro = Entry(framePassivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_carro.place(x=10, y=125)


# Empréstimos Estudantis
l_estudante = Label(framePassivos, text="Empréstimos Estudantis", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_estudante.place(x=10, y=165)

e_valor_estudante = Entry(framePassivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_estudante.place(x=10, y=195)


# Outras dívidas
l_dividas = Label(framePassivos, text="Outras dívidas", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_dividas.place(x=10, y=230)

e_valor_dividas = Entry(framePassivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_dividas.place(x=10, y=255)

l_resultado = Label(frameResultado, text='R${:,.2f}'.format(00), padx=10, width=15, height=1, anchor=NE, font=('Verdana 25 bold'), bg=co3, fg=co1)
l_resultado.place(x=0, y=7)

def calcular():
    ativo_1 = e_valor_casa.get()
    ativo_2 = e_valor_imovel.get()
    ativo_3 = e_valor_veiculos.get()
    ativo_4 = e_valor_investimentos.get()
    ativo_5 = e_outros_ativos.get()
    
    passivo_1 = e_valor_hipoteca.get()
    passivo_2 = e_valor_carro.get()
    passivo_3 = e_valor_estudante.get()
    passivo_4 = e_valor_dividas.get()
    
    if ativo_1 == '' or ativo_2 == '' or ativo_3 == '' or ativo_4 == '' or ativo_5 == '' or passivo_1 == '' or passivo_2 == '' or passivo_3 == '' or passivo_4 == '':
        print('Entra algum valor')
        
        return
    
    else:
        Total_ativos = float(ativo_1) + float(ativo_2) + float(ativo_3) + float(ativo_4) + float(ativo_5)
        
        Total_passivos = float(passivo_1) + float(passivo_2) + float(passivo_3) + float(passivo_4)
        
        Patrimonio_liquido = Total_ativos - Total_passivos
        
        l_resultado['text'] = 'R${:,.2f}'.format(Patrimonio_liquido)

botao_calcular = Button(framePassivos, command=calcular, width=12, anchor=CENTER, text=' Calcular'.upper(), overrelief=RIDGE, font=('Ivy 9 bold'), bg=co1, fg=co0 )
botao_calcular.place(x=10, y=310)





janela.mainloop()
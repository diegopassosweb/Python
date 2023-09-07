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


janela = Tk()
janela.title('')
janela.geometry('380x500')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

#frames
frameCima = Frame(janela, width=380, height=50, bg=co1)
frameCima.grid(row=0, column=0, columnspan=2)

frameResultado = Frame(janela, width=380, height=50, bg=co3)
frameResultado.grid(row=1, column=0, pady=10)

frameBaixo = Frame(janela, width=380, height=400, bg=co1)
frameBaixo.grid(row=2, column=0, pady=10)

#dividindo frame baixo
frameeAtivos = Frame(frameBaixo, width=180, height=370, bg=co9)
frameeAtivos.grid(row=0, column=0, padx=5)

framePassivo = Frame(frameBaixo, width=180, height=370, bg=co9)
framePassivo.grid(row=0, column=1)

#logo
app_logo = Image.open('logo.png')
app_logo = app_logo.resize((50,50))
app_logo = ImageTk.PhotoImage(app_logo)

app_logo = Label(frameCima, image=app_logo, width=900, compound=LEFT, padx=5, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text='Calculadora Patrimonio', width=900, compound=LEFT, padx=5, anchor=NW, bg=co1, fg=co4, font=('Ivy 12'))
app_.place(x=50, y=0)

l_linha = Label(frameCima, width=380, anchor=NW, bg=co3, fg=co1, font=('Verdana 1'))
l_linha.place(x=0, y=47)

# Funçao patrimonio liquido

def calcular():
    
    ativo_1 = e_valor_casa.get()
    ativo_2 = e_valor_imovel.get()
    ativo_3 = e_valor_veiculos.get()
    ativo_4 = e_valor_investimentos.get()
    ativo_5 = e_outros_ativos.get()
    
    passivo_1 = e_valor_hipoteca.get()
    passivo_2 = e_valor_carro.get()
    passivo_3 = e_valor_estudantes.get()
    passivo_4 = e_valor_dividas.get()
    
    #verificiando entradas
    
    if ativo_1 == '' or ativo_2 == '' or ativo_3 == '' or ativo_4 == '' or ativo_5 == '' or passivo_1 == '' or passivo_2 == '' or passivo_3 == '' or passivo_4 == '':
        print('Entra algum valor nos campos')
        return
    else:
        total_ativos = float(ativo_1) + float(ativo_2) + float(ativo_3) + float(ativo_4) + float(ativo_5)
        
        total_passivos = float(passivo_1) + float(passivo_2) +  float(passivo_3) +  float(passivo_4)
        
        patrimonio_liquido = total_ativos - total_passivos
        
        l_resultado['text'] = 'R${:,.2f}'.format(patrimonio_liquido)
        



# Entrando Ativos -------------------------------------------------------

l_nome = Label(frameeAtivos, text="Insira Ativos",padx=10, width=35, height=1,anchor=NW, font=('Verdana 11 '), bg=co2, fg=co1)
l_nome.place(x=0, y=0)

# Valor da casa
l_casa = Label(frameeAtivos, text="Valor da casa", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_casa.place(x=10, y=40)

e_valor_casa = Entry(frameeAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_casa.place(x=10, y=65)


#  Imóveis
l_imoveis = Label(frameeAtivos, text="Imóveis", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_imoveis.place(x=10, y=105)

e_valor_imovel = Entry(frameeAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_imovel.place(x=10, y=125)


# Veículos
l_veiculos = Label(frameeAtivos, text="Veículos", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_veiculos.place(x=10, y=165)

e_valor_veiculos = Entry(frameeAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_veiculos.place(x=10, y=195)


# Investimentos e Poupança
l_investimentos = Label(frameeAtivos, text="Investimentos", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)

l_investimentos.place(x=10, y=230)
e_valor_investimentos = Entry(frameeAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_investimentos.place(x=10, y=255)


# Outros ativos
l_ativos = Label(frameeAtivos, text="Outros ativos", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_ativos.place(x=10, y=295)

e_outros_ativos = Entry(frameeAtivos, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_outros_ativos.place(x=10, y=315)

# Entrando Passivos -------------------------------------------------------

l_nome = Label(framePassivo, text="Insira Passivos",padx=10, width=35, height=1,anchor=NW, font=('Verdana 11 '), bg=co5, fg=co1)
l_nome.place(x=0, y=0)

# Valor da casa
l_casa = Label(framePassivo, text="Hipoteca", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_casa.place(x=10, y=40)

e_valor_hipoteca = Entry(framePassivo, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_hipoteca.place(x=10, y=65)


#  Imóveis
l_carro = Label(framePassivo, text="Emprestimmo de Carro", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_carro.place(x=10, y=105)

e_valor_carro = Entry(framePassivo, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_carro.place(x=10, y=125)


# Veículos
l_estudantes = Label(framePassivo, text="Emprestimo estudantes", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_estudantes.place(x=10, y=165)

e_valor_estudantes = Entry(framePassivo, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_estudantes.place(x=10, y=195)


# Investimentos e Poupança
l_dividas = Label(framePassivo, text="Outras dividas", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)

l_dividas.place(x=10, y=230)
e_valor_dividas = Entry(framePassivo, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_valor_dividas.place(x=10, y=255)


#resultado
l_resultado = Label(frameResultado, text='R${:,.2f}'.format(00), width=15, padx=10, anchor=NE, font=('Verdana 25 bold '), bg=co3, fg=co1)
l_resultado.place(x=0, y=7)

l_buttoncalc = Button(framePassivo,command=calcular, text='Calcular'.upper(), width=12, padx=10, anchor=CENTER, font=('Ivy 9 bold '), bg=co3, fg=co1)
l_buttoncalc.place(x=10, y=310)









janela.mainloop()

from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
                 
co0 = "#2e2d2b" 
co1 = "#feffff" 
co2 = "#4fa882" 
co3 = "#38576b" 
co4 = "#403d3d"   
co5 = "#F3E99F"  
co6 = "#03091f"  

janela = Tk()
janela.title('')
janela.geometry('400x350')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

investimento_inicial = 1000
dias_de_investimento = 30
retorno_garantido = 126


def calcular_lucro(investimento_inicial, dias_de_investimento, retorno_garantido):
    try:
        # obtendo valor
        quantia = float(e_valor.get())

        # obtendo dias de investimento
        dias_de_investimento = int(e_valor_dias.get())

        # obtendo a percentagem
        percentagem = float(e_valor_percentagem.get())

        investimento_inicial = quantia 
        retorno_garantido = percentagem

        retorno_diario = retorno_garantido / 100 / dias_de_investimento
        lucro_total = investimento_inicial * (1 + retorno_garantido / 100)
        lucro_diario = investimento_inicial * retorno_diario
        lucro_semanal = lucro_diario * 7
        lucro_mensal = lucro_diario * 30

        app_dia['text'] = locale.currency(lucro_diario, symbol=True, grouping=True)
        app_semana['text'] = locale.currency(lucro_semanal, symbol=True, grouping=True)
        app_mes['text'] = locale.currency(lucro_mensal, symbol=True, grouping=True)
        app_total['text'] = locale.currency(lucro_total, symbol=True, grouping=True)

        # Formate o número como uma string de moeda com um símbolo de Reais
        dinheiro_str = locale.currency(1234.56, symbol=True, grouping=True)
    except ValueError as e:
        pass
    
    retorno_diario = retorno_garantido / 100 / dias_de_investimento
    lucro_total = investimento_inicial * (1 + retorno_garantido / 100)
    lucro_diario = investimento_inicial * retorno_diario
    lucro_semanal = lucro_diario * 7
    lucro_mensal = lucro_diario * 30
    print("Lucro diário: {:.2f}".format(lucro_diario))
    print("Lucro semanal: {:.2f}".format(lucro_semanal))
    print("Lucro mensal: {:.2f}".format(lucro_mensal))
    print("Lucro total: {:.2f}".format(lucro_total))

#frames 

frameCima = Frame(janela, width=450, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

framePergunta = Frame(janela, width=450, height=100, bg=co1, relief="solid")
framePergunta.grid(row=1, column=0, padx=5, sticky=NSEW)

frameResultado = Frame(janela, width=300, height=310, bg='#4E6E81', relief="raised")
frameResultado.grid(row=3, column=0, sticky=NSEW)

frameDia = Frame(frameResultado, width=200, height=100, bg=co1, relief="solid")
frameDia.grid(row=0, column=0, padx=1, pady=1, sticky=NSEW)

frameMes = Frame(frameResultado, width=200, height=100, bg=co1, relief="solid")
frameMes.grid(row=1, column=0, padx=1, pady=1, sticky=NSEW)

frameSemana = Frame(frameResultado, width=200, height=100, bg=co1, relief="solid")
frameSemana.grid(row=0, column=1, padx=1, pady=1, sticky=NSEW)

frameTotal = Frame(frameResultado, width=200, height=100, bg=co1, relief="solid")
frameTotal.grid(row=1, column=1, padx=1, pady=1, sticky=NSEW)

#logo

# app_img = Image.open('')
# app_img = app_img.resize((45,45))
# app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, text='Calculadora de Investimento', font=('Verdana 14'), width=350, compound=LEFT, padx=5, relief=FLAT, anchor=CENTER, bg=co1, fg=co0)
app_logo.place(x=5, y=0)

l_linha = Label(frameCima, width=450, height=1,anchor=NW, font=('Verdana 1 '), bg='#4E6E81', fg=co1)
l_linha.place(x=0, y=48)

app_ = Label(framePergunta, text='Investimento', width=20, height=1, relief=FLAT, anchor=NW, font=('Verdana 10'), bg=co1, fg=co0)
app_.place(x=50, y=15)
e_valor = Entry(framePergunta, width=10, font=('Ivy 22'), justify='center', relief='solid',bg='#F3E99F', fg='#4E6E81')
e_valor.place(x=5, y=50)

app_ = Label(framePergunta, text='Dias*', width=10, height=1, relief=FLAT, anchor=NW, font=('Verdana 10'), bg=co1, fg=co0)
app_.place(x=200, y=15)
e_valor_dias = Entry(framePergunta, width=5, font=('Ivy 22'), justify='center', relief='solid',bg='#F3E99F', fg='#4E6E81')
e_valor_dias.place(x=174, y=50)

app_ = Label(framePergunta, text='Porcentagem %', width=13, height=1, relief=FLAT, anchor=NW, font=('Verdana 10'), bg=co1, fg=co0)
app_.place(x=260, y=15)
e_valor_percentagem = Entry(framePergunta, width=5, font=('Ivy 22'), justify='center', relief='solid',bg='#F3E99F', fg='#4E6E81')
e_valor_percentagem.place(x=270, y=50)


#diario

app_ = Label(frameDia, text='Lucro Diario', width=15, height=1, anchor=CENTER, font=('Verdana 11'), bg=co1, fg='#4E6E81')
app_.place(x=20, y=2)

app_dia = Label(frameDia, text='', width=10, height=1, anchor=CENTER, font=('Verdana 15'), bg=co1, fg=co0)
app_dia.place(x=20, y=35)

# mes
app_ = Label(frameMes, text='Lucro Mensal', width=15, height=1, anchor=CENTER, font=('Verdana 11'), bg=co1, fg='#4E6E81')
app_.place(x=20, y=7)

app_mes = Label(frameMes, text='', width=10, height=1, anchor=CENTER, font=('Verdana 15'), bg=co1, fg=co0)
app_mes.place(x=20, y=35)

# semana

app_ = Label(frameSemana,text="Lucro Semanal", width=15, height=1, anchor=CENTER, font=('Verdana 11'),bg=co1, fg='#4E6E81')
app_.place(x=20, y=7)

app_semana = Label(frameSemana,text="", width=10, height=1,anchor=CENTER, font=('Verdana 15'),bg=co1, fg=co0)
app_semana.place(x=20, y=35)

# total

app_ = Label(frameTotal, text='Lucro Total', width=15, height=1, anchor=CENTER, font=('Verdana 11'), bg=co1, fg='#4E6E81')
app_.place(x=20, y=7)

app_total = Label(frameTotal, text='', width=10, height=1, anchor=CENTER, font=('Verdana 15'), bg=co1, fg=co0)
app_total.place(x=20, y=35)

calcular_lucro(investimento_inicial, dias_de_investimento, retorno_garantido)

janela.mainloop()
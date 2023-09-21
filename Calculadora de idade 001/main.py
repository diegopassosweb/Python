from tkinter import *
from tkinter import ttk

from tkcalendar import Calendar, DateEntry

from dateutil.relativedelta import relativedelta

from datetime import date

janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('310x400')

#cores 
cor1 = "#3b3b3b"
cor2 = "#333333"
cor3 = "#ffffff"
cor4 = "#fcc058"


# criando frames
frame_cima = Frame(janela, width=310, height=140, padx=0, pady=0, relief=FLAT,bg=cor1)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=300, padx=0, pady=0, relief=FLAT,bg=cor1)
frame_baixo.grid(row=1, column=0)

# criando labels frame cima
l_calculadora = Label(frame_cima, text='Calculadora', width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor4)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text='De idade', width=11, height=1, padx=3, relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor2, fg=cor4)
l_idade.place(x=0, y=70)

#funçao
def calcular():
    
    inicial=cal_1.get()
    terminio=cal_2.get()
    
    # separando os valores e atribuindo em variaveis diferentes
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]
 
    # Convertendo os valores em formato  datatime
    data_inicial = date(ano_1, mes_1, dia_1)
 
 
    # separando os valores e atribuindo em variaveis diferentes
    mes_2, dia_2, ano_2 = [int(f) for f in terminio.split('/')]
 
    # Convertendo os valores em formato  datatime
    data_nascimento = date(ano_2, mes_2, dia_2)
    
    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days
    
 
    app_1_anos['text'] = anos
    app_2_mes['text'] = meses
    app_3_dia['text'] = dias

    

# criando labels frame baixo
l_data_inicial = Label(frame_baixo, text="Data Inicial", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor3)
l_data_inicial.place(x=50, y=30)
 
cal_1 = DateEntry(frame_baixo,width=13, background='darkblue',foreground='white', borderwidth=2,date_pattern='mm/dd/y', year=2021)
cal_1.place(x=170, y=30)
 
l_data_nascimento = Label(frame_baixo, text="Data de nascimento", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor3)
l_data_nascimento.place(x=50, y=70)
 
cal_2 = DateEntry(frame_baixo, width=13, background='darkblue',foreground='white', borderwidth=2,date_pattern='mm/dd/y', year=2021)
cal_2.place(x=170, y=70)

app_1_anos = Label(frame_baixo, text="27", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 25 bold'),bg=cor1,  fg=cor3)
app_1_anos.place(x=60, y=135)
app_anos = Label(frame_baixo, text="Anos", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 11 bold'),bg=cor1, fg=cor3)
app_anos.place(x=50, y=175)
 
app_2_mes = Label(frame_baixo, text="27", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 12 bold'),bg=cor1,  fg=cor3)
app_2_mes.place(x=140, y=135)
app_mes = Label(frame_baixo, text="Meses", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 11 bold'),bg=cor1, fg=cor3)
app_mes.place(x=130, y=175)
 
app_3_dia = Label(frame_baixo, text="27", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 12 bold'),bg=cor1,  fg=cor3)
app_3_dia.place(x=220, y=135)
app_dia = Label(frame_baixo, text="Dias", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 11 bold'),bg=cor1, fg=cor3)
app_dia.place(x=210, y=175)

# botao calcular
b_calcular = Button(frame_baixo, command=calcular, text='Calcular', width=20, height=1, padx=0, relief='raised', font=('Ivy 10 bold'), overrelief='ridge', bg=cor1, fg=cor3)
b_calcular.place(x=60, y=225)


janela.mainloop()
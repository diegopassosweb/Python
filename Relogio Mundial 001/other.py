from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, StringVar, ttk

from PIL import Image, ImageTk
import pyglet
pyglet.font.add_file('digital-7.ttf')

from datetime import datetime
from pytz import country_timezones
import pytz

from paises import *

#cores
co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#34c6eb"
co3 = "#38576b"

# criando janela
janela = Tk()
janela.title('')
janela.geometry('300x195')
janela.configure(background=co3)
janela.resizable(width=FALSE, height=FALSE)

# aplicando estilo para janela
style = ttk.Style(janela)
style.theme_use("clam")

# criando frames
frameCima = Frame(janela, width=300, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0, columnspan=2)

frameBaixo = Frame(janela, width=300, height=140, bg=co0, relief=FLAT)
frameBaixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

app_img = Image.open('./icon.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)


app_logo = Label(frameCima, image=app_img, text=" Relogio Mundial",
width=920, compound=LEFT, anchor=NW, font=('digital-7 25'),
bg=co1, fg=co0)
app_logo.place(x=0, y=0)

# codigo do programa
# obtendo zonas de fuso horario
time_zones = pytz.all_timezones


# obtendo zonas com abreviaçao do pais
timezone_country = {}

for i in country_timezones:
    timezones = country_timezones[i]
    for y in timezones:
        timezone_country[y] = i

#lista das zonas (fuso horario)
zona = []

for i in timezone_country.keys():
    zona.append(i)
    
# funçao
global img_bandeira, app_bandeira

def relogio():
    global img_bandeira, app_bandeira
    
    zona = c_zona.get()
    # convertendo a zona selecionado o formato do timezone
    zona_selecionada = pytz.timezone(zona)

    # obtendo a hora da zona selecionado
    country_time = datetime.now(zona_selecionada)

    # obtendo o nome do pais da zona selecionado
    simbolo_do_pais = [timezone_country[zona]]

    for i in paises.keys():
        simbolo_do_pais.append(i.lower())
        
    # pegando o local da imagem
    imagem = "png250px/{}.{}".format(simbolo_do_pais[0],'png').lower()

    # obtendo a chave do pais em letra maiusculas
    key = simbolo_do_pais[0].upper()

    # obtendo o nome do pais
    nome_do_pais = paises[key]
    
    #pegando mais informaçoes
    tempo = country_time
    horas = tempo.strftime('%H:%M:%S')
    dia_da_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")
    periodo = tempo.strftime("%p")

    # passando informaçoes para o label
    
    l_cidade.config(text=zona)
    l_pais.config(text=nome_do_pais)
    l_horas.config(text=horas)
    l_data.config(text=dia_da_semana+","+""+ str(dia) + " "+ str(mes) + " " + (ano)+ " " +(periodo))
    l_periodo.config(text=periodo)
    
    # abrindo bandeira
    img_bandeira = Image.open(imagem)
    img_bandeira = img_bandeira.resize((93,55))
    img_bandeira = ImageTk.PhotoImage(img_bandeira)

    app_bandeira = Label(frameBaixo_baixo, image=img_bandeira,
    bg=co1, fg=co0, relief='solid')
    app_bandeira.place(x=170, y=40)
    
    l_horas.after(200, relogio)

# trabalhando no frame baixo
frameBaixo_cima = Frame(frameBaixo, width=300, height=35, bg=co1,
relief=RAISED)
frameBaixo_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo_baixo = Frame(frameBaixo, width=300, height=155, bg=co1,
relief=FLAT)
frameBaixo_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# trabalhando no frame baixo cima
l_zona = Label(frameBaixo_cima,text="Fuso Horario",
width=35, anchor=NW, font=('Ivy 10'),
bg=co1, fg=co0)
l_zona.place(x=10, y=10)

c_zona = Combobox(frameBaixo_cima, width=25)
c_zona.place(x=123, y=10)
c_zona.set('Asia/Kolkata')
c_zona['values'] = (zona)

# trabalhando frame baixo baixo
l_cidade = Label(frameBaixo_baixo,text="Cabinda", anchor=NW, font=('Arial 10'),
bg=co1, fg=co0)
l_cidade.place(x=10, y=8)

# pais
l_pais = Label(frameBaixo_baixo,text="Angola", anchor=NW, font=('Arial 10'),
bg=co1, fg=co0)
l_pais.place(x=10, y=28)

# horas
l_horas = Label(frameBaixo_baixo,text="10:05:05", anchor=NW, font=('Arial 25 bold'),
bg=co1, fg=co2)
l_horas.place(x=1, y=45)

# periodo 
l_periodo = Label(frameBaixo_baixo,text="PM", anchor=NW, font=('Verdana 10'),
bg=co1, fg=co2)
l_periodo.place(x=135, y=60)

# data
l_data = Label(frameBaixo_baixo,text="26-Sep-22", anchor=NW, font=('Arial 8'),
bg=co1, fg=co0)
l_data.place(x=10, y=79)



relogio()
janela.mainloop()

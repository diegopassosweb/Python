from tkinter import *
from tkinter import ttk, filedialog
from tkscrolledframe import ScrolledFrame
import csv
import random

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

def escolher_arquivo():
    file = filedialog.askopenfilename()

    with open(file) as file:
        ler_csv = csv.reader(file)
        for row in ler_csv:
            Lista_de_nomes.append(row[0])

def gerar():
    global grupos_gerados
    print(Lista_de_nomes)

    def chunks(l, n):
        """Produza grupos sucessivos de tamanho n de l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    random.shuffle(Lista_de_nomes)
    numero = int(e_total.get())
    grupos_gerados = list(chunks(Lista_de_nomes, numero))
    gerar_tabelas()

def gerar_tabelas():
    global grupos_gerados

    r = 0
    c = 0
    r_linha = 0
    n = 1

    for grupo in grupos_gerados:
        if c == 1:
            r = 0

        if c == 2:
            c = 0
            r = 0
            r_linha += 1

        frame = Frame(framecanva, width=190, height=190, relief="solid", bg=co1)
        frame.grid(row=r_linha, column=c, pady=10, padx=10, sticky=NSEW)

        l_grupo = Label(frame, text="Grupo - {}".format(n), width=20, justify=LEFT, anchor=NW, font=('verdana 10'), bg=co6, fg=co1)
        l_grupo.grid(row=r, column=0)

        for i in grupo:
            r += 1
            l_participante = Label(frame, text=i, justify=LEFT, anchor=NW, font=('verdana 8'), bg=co1, fg=co4)
            l_participante.grid(row=r, column=0, sticky=NSEW)
            r += 1

        c += 1
        n += 1

janela = Tk()
janela.title("")
janela.geometry('390x500')
janela.configure(background=co6)
janela.resizable(width=FALSE, height=FALSE)

frame_principal = Frame(janela, width=390, height=500, bg=co6, relief="flat")
frame_principal.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

style = ttk.Style(janela)
style.theme_use("clam")

frame_top = Frame(frame_principal, width=390, height=150, bg=co6, relief="flat")
frame_top.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_resultado = Frame(frame_principal, width=390, height=100, bg=co6, relief="flat")
frame_resultado.grid(row=1, column=0, pady=1, padx=1, sticky=NSEW)

sf = ScrolledFrame(frame_resultado, width=370, height=328, bg=co2)
sf.grid(row=0, column=0, sticky=NW, padx=0)

framecanva = sf.display_widget(Frame, bg=co2)

Lista_de_nomes = []

l_app_nome = Label(frame_top, text="Gerador de grupos aleatórios", width=29, height=1, anchor=NW, relief='flat', font=('Verdana 13 bold'), bg=co6, fg=co1)
l_app_nome.place(x=10, y=10)

l_linha = Label(frame_top, text="", width=500, anchor=NW, font=('Ivy 1'), bg=co1)
l_linha.place(x=0, y=45)
l_linha = Label(frame_top, text="", width=500, anchor=NW, font=('Ivy 1'), bg=co6)
l_linha.place(x=0, y=47)

b_rodando = Button(frame_top, command=escolher_arquivo, text="Carregar uma lista", justify=LEFT, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
b_rodando.place(x=10, y=70)

l_total = Label(frame_top, text="Número de pessoas em cada grupo: ", anchor=NW, font=('Verdana 8'), bg=co6, fg=co1)
l_total.place(x=9, y=112)

e_total = Entry(frame_top, width=8, font=('verdana 10'), justify='center', relief="groove", highlightthickness=1)
e_total.place(x=235, y=114)

b_gerar = Button(frame_top, command=gerar, text="Gerar", justify='center', height=1, bg='#e68a2e', fg=co1, font=('Verdana 8 bold'), relief=RAISED, overrelief=RIDGE)
b_gerar.place(x=305, y=114)

janela.mainloop()
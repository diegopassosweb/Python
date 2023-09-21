from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image, ImageOps, ImageDraw
import requests
import time
import json

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
fundo = "#484f60"

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_principal = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief="flat")
frame_principal.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0, relief="flat")
frame_corpo.grid(row=2, column=0, sticky=NW)

style = ttk.Style(frame_principal)
style.theme_use('clam')

def info():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,AOA,BRL"
    
    #HTTP request
    r = requests.get(api_link)
    
    #converter os dados em dicionario
    dados = r.json()
    
    # USD
    valor_usd = float(dados['USD'])
    valor_formatado_usd = "${:,.3f}".format(valor_usd)
    l_preco_usd["text"] = valor_formatado_usd
    
    # kwanza
    valor_aoa = float(dados['AOA'])
    valor_formatado_aoa = "{:,.3f}".format(valor_aoa)
    l_preco_aoa['text'] = "Em Kwanzas é : AOA " + valor_formatado_aoa
    
    #reais
    valor_reais = float(dados["BRL"])
    valor_formatado_reais = "{:,.3f}".format(valor_reais)
    l_preco_reais['text'] = "Em reais é : R$ " + valor_formatado_reais
    
    frame_corpo.after(1000, info)

imagem = Image.open('btc.png')
imagem = imagem.resize((30, 30))
imagem = ImageTk.PhotoImage(imagem)
l_icon1 = Label(frame_principal, image=imagem, compound=LEFT, bg=fundo, fg='white', font=('Ivy 10 bold'), anchor="nw", relief=FLAT)
l_icon1.place(x=10, y=10)

l_nome = Label(frame_principal, text='Bitcoin Price Tracker', height=1, padx=0, relief="flat", anchor="center", font=('Arial 20'), bg=co1, fg=co2)
l_nome.place(x=50, y=5)

l_preco_usd = Label(frame_corpo, text='', width=14, height=1, padx=0, relief="flat", anchor="center", font=('Arial 20'), bg=fundo, fg=co1)
l_preco_usd.place(x=0, y=50)

l_preco_euro = Label(frame_corpo, text='', height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_preco_euro.place(x=10, y=130)

l_preco_reais = Label(frame_corpo, text='', height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_preco_reais.place(x=10, y=160)

l_preco_aoa = Label(frame_corpo, text='', height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_preco_aoa.place(x=10, y=190)

info()

janela.mainloop()
    
    
    
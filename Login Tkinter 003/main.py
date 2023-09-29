from tkinter import *
from tkinter import Tk, ttk, messagebox

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra


janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


#frames

frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

credenciais = ['joao', '123456']
def verifica_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())
    
    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('LOGIN', 'Seja bem vindo Admin !')
        
        
    
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('LOGIN', 'Seja bem vindo de volta '+credenciais[0])
        
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_cima.winfo_children():
            widget.destroy()
        
        nova_janela()
    
    else:
        messagebox.showwarning('ERRO', 'Verifique nome e senha')

def nova_janela():
    l_nome = Label(frame_cima, text='Usuario: ' + credenciais[0], height=1, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)
    
    l_linha = Label(frame_cima, width=275, text='', height=1, anchor=NW, font=('Ivy 1'), bg=co2)
    l_linha.place(x=10, y=45)
    
    l_nome = Label(frame_baixo, text='Seja bem vindo ' + credenciais[0], height=1, anchor=NE, font=('Ivy 15'), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)
    
# frame cima

l_nome = Label(frame_cima, text='LOGIN', height=1, anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5,y=5)

l_linha = Label(frame_cima, width=275, text='', height=1,anchor=NW, font=('Ivy 1'), bg=co2, )
l_linha.place(x=10, y=45)

# configurando frame baixo

l_nome = Label(frame_baixo, text='Nome *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25,justify='left', highlightthickness=1, font=('', 15), relief='solid')
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text='Senha *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, show='*', width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
e_pass.place(x=15, y=130)

botao_confirmar = Button(frame_baixo,  command=verifica_senha,text='Entrar', width=39, height=2, bg=co2, fg=co1,font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=15, y=180)


janela.mainloop()
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

# criando janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# dividindo a janela
Frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
Frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

Frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
Frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando o frame cima 
l_nome = Label(Frame_cima, text='LOGIN', anchor=NE,font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(Frame_cima, text='', width=275, anchor=NW,font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

cred = ["joao", "123456789"]

# funçao verifica senha
def verify():
    nome = e_nome.get()
    senha = e_pass.get()
    
    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin !!')
    elif cred[0] == nome and cred[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta !!' + cred[0])
        
        # deleta itens presentes no frame
        for widget in Frame_baixo.winfo_children():
            widget.destroy()
        
        for widget in Frame_baixo.winfo_children():
            widget.destroy()
        
        nova_janela()
        
    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha!')

# função apos verificacáo
def nova_janela():
    l_nome = Label(Frame_cima, text='Usuario: ' + cred[0], anchor=NE,font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(Frame_cima, text='', width=275, anchor=NW,font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)
    
    l_nome = Label(Frame_baixo, text='Seja bem vindo: ' + cred[0], anchor=NE,font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)
    
        

# configurando o frame baixo
l_nome = Label(Frame_baixo, text='Nome *', anchor=NW,font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(Frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid' )
e_nome.place(x=14, y=50)

l_pass = Label(Frame_baixo, text='Senha *', anchor=NW,font=('Ivy 10'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(Frame_baixo, width=25, justify='left', show='*', font=('', 15), highlightthickness=1, relief='solid' )
e_pass.place(x=14, y=130)

# Button
b_confirm = Button(Frame_baixo, command=verify, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirm.place(x=15, y=180)


janela.mainloop()
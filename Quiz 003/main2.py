import tkinter as tk
from tkinter import ttk, filedialog
import re
import csv

colors = {
    'background': '#F3F4F9',             # Cor de fundo geral
    'text': '#333333',                    # Cor do texto
    'button_bg': '#4A73B5',                # Cor de fundo do botão
    'button_fg': '#FFFFFF',                # Cor do texto do botão
    'tree_header_bg': '#4A73B5',           # Cor de fundo do cabeçalho da tabela
    'tree_header_fg': '#FFFFFF',           # Cor do texto do cabeçalho da tabela
    'tree_bg': '#FFFFFF',                  # Cor de fundo da tabela
    'tree_odd_row': '#F3F4F9',             # Cor de fundo das linhas ímpares tabela
    'tree_even_row': '#E7E8ED'             # Cor de fundo das linhas pares da tabela
}


janela = tk.Tk()
janela.title('Verificador Email')
janela.geometry('419x210')
janela.configure(bg=colors['background'])

frame_main = tk.Frame(janela, width=419, height=60, bg=colors['background'], pady=0, padx=0, relief='flat')
frame_main.grid(row=0, column=0)

frame_tabela = tk.Frame(janela, width=405, height=110, bg=colors['background'], pady=0, padx=0, relief='flat')
frame_tabela.grid(row=1, column=0)

style = ttk.Style(frame_main)
style.theme_use('clam')

lista_valid_email = []
lista_invalid_email = []

def verificador_de_e_email(email):
    if re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', email):
        lista_valid_email.append(email)
    else:
        lista_invalid_email.append(email)
        
def abrir_ficheiro():
    ficheiro = filedialog.askopenfilename()
    
    emails = []
    
    with open(ficheiro) as file:
        ler_csv = csv.reader(file)
        for row in ler_csv:
            verificador_de_e_email(row[2])
            emails.append(row[2])
    
lista_email = []
num_1 = len(lista_valid_email)
num_2 = len(lista_invalid_email)

count = 0
if num_1 > num_2:
    while num_1 > 0:
        temp = []
        try:
            temp.append(lista_valid_email[count])
        except IndexError:
            temp.append("")
            
        try:
            temp.append(lista_invalid_email[count])
        except IndexError:
            temp.append("")
            
        lista_email.append(temp)
        count += 1
        num_1 -= 1

elif num_2 > num_1:
    while num_2 > 0:
        temp = []
        try:
            temp.append(lista_invalid_email[count])
        except IndexError:
            temp.append("")
        
        try:
            temp.append(lista_invalid_email[count])
        except IndexError:
            temp.append("")
            
        lista_email.append(temp)
        count += 1
        num_2 -= 1
        
for i, item in enumerate(lista_email):
    tree.insert("", 'end', values=(item), tags=('odd_row' if i % 2 == 0 else 'even_row'))

list_header = ['Email valido', 'E-mail invalido']
tree = ttk.Treeview(frame_tabela, selectmode='extended', columns=list_header, show='headings', height=5)
vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview)
hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frame_tabela.grid_rowconfigure(1, weight=2)

header_widths = [200, 200]
header_anchors = ['nw', 'nw']

for col, width, anchor in zip(list_header, header_widths, header_anchors):
    tree.heading(col, text=col.title(), anchor=anchor)
    tree.column(col, width=width, anchor=anchor)
    

tree.tag_configure('odd_row', background=colors['tree_odd_row'])
tree.tag_configure('even_row', background=colors['tree_even_row'])

app_name = tk.Label(frame_main, text='Verificador de E-mail', height=1, padx=0, relief='flat', anchor='center', font=('Arial', 15, 'bold'), bg=colors['background'], fg=colors['text'])
app_name.place(x=10, y=10)

b_add = tk.Button(frame_main, command=abrir_ficheiro, text='Abrir ficheiro CSV', height=1, bg=colors['button_bg'], fg=colors['button_fg'], font=('Arial', 10, 'bold'), relief=tk.RAISED)
b_add.place(x=260, y=20)

janela.mainloop()
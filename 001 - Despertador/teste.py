from tkinter.ttk import *
from tkinter import*

# importando pillow
from PIL import Image, ImageTk
from matplotlib import image
from matplotlib.pyplot import text

from pygame import mixer
import time
from datetime import datetime

from time import sleep
from threading import Thread

janela = Tk()
janela.title("")
janela.geometry('350x150')
janela.resizable(width=FALSE, height=FALSE)


def tocar_alarme():
    mixer.init()
    mixer.music.load('l.mp3')
    mixer.music.play()



def alarme():
    while True:
        control = 1
        h_alarme = "00"
        m_alarme = "00"
        s_alarme = "00"
        p_alarme = "am".upper()
                
        hora_atual = datetime.now()
                
        hora = hora_atual.strftime("%I")
        minuto = hora_atual.strftime("%M")
        segundo = hora_atual.strftime("%S")
        periodo = hora_atual.strftime("%p")
        
        if control == 1:
            if p_alarme == periodo:
                if h_alarme == hora:
                    if m_alarme == minuto:
                        if s_alarme == segundo:
                            print("Hora de fazer uma pausa")
                            tocar_alarme()
                            tocar_alarme()
    
        sleep(1)
    
t1 = Thread(target=alarme)   

# iniciar o thread
t1.start()
mixer.init()



janela.mainloop()
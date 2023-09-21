# importar o App, Builder (GUI)
# criar o aplicativo
# criar a funçao build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.pegar_cot('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cot('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cot('BTC')}"
        
    def pegar_cot(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requesiçao = requests.get(link)
        dic_requisiçao = requesiçao.json()
        cot = dic_requisiçao[f"{moeda}BRL"]["bid"]
        return cot
        
MeuAplicativo().run()
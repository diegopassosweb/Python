from datetime import datetime
from pytz import country_timezones
import pytz

from paises import *

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
    
# convertendo a zona selecionado o formato do timezone
zona_selecionada = pytz.timezone(zona[25])

# obtendo a hora da zona selecionado
country_time = datetime.now(zona_selecionada)

# obtendo o nome do pais da zona selecionado
simbolo_do_pais = [timezone_country[zona[2]]]

for i in paises.keys():
    simbolo_do_pais.append(i.lower())

# pegando o local da imagem
imagem = "png250px/{}.{}".format(simbolo_do_pais[0],'png').lower()

# obtendo a chave do pais em letra maiusculas
key = simbolo_do_pais[0].upper()

# obtendo o nome do pais
nome_do_pais = paises[key]


print(f"A data da {zona_selecionada} é {country_time.strftime('%d-%m-%y')} e o pais é {nome_do_pais} e la sao {country_time.strftime('%H:%M:%S')}")


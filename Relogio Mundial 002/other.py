from datetime import datetime
from pytz import country_timezones
import pytz
from paises import *

time_zones = pytz.all_timezones

#obtendo zonas com abreviaçao do pais
timezone_country = {}

for countrycode in country_timezones:
    timezones = country_timezones[countrycode]
    for timezone in timezones:
        timezone_country[timezone] = countrycode

#lista de zonas
zonas = []
for i in timezone_country.keys():
    zonas.append(i)

#convertendo a zona selecionada no formato timezone
zona_selecionada = pytz.timezone(zonas[5])

#obetendo a hora selecionada
country_time = datetime.now(zona_selecionada)

#obtendo o nome do pais da zona selecionada

#variavel que tera o simbolo do pais
simbol_do_pais = [timezone_country[zonas[56]]]

for i in paises.keys():
    simbol_do_pais.append(i.lower())

# usando format para obter o caminho da imagem (bandeira)
imagem = "png250px/{}.{}".format(simbol_do_pais[0], 'png')

#obtendo o key do pais em letra MAIUSCULAS
key = simbol_do_pais[0].upper()

#obtendo o nome do pais
nome_do_pais = paises[key]

print(f"A data da {zona_selecionada} é {country_time.strftime('%d-%m-%y')} e o pais é {nome_do_pais} e la são {country_time.strftime('%H:%M:%S')}")
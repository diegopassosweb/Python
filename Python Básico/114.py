import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com.br')
except urllib.error.URLError:
    print('Site OFF')
else:
    print('Conseguir acessar')
    # print(site.read())
    

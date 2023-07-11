import math
ang = float(input('Digite um angulo que voce deseja: '))
seno = math.sin(math.radians(ang))
print(f'O angulo de {ang} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(ang))
print(f'O angulo de {ang} tem o COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(ang))
print(f'O angulo de {ang} tem a TANGENTE de {tangente:.2f}')
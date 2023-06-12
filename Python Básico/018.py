import math 
a = float(input("Digite o angulo: "))
s = math.sin(math.radians(a))
print(f'O angulo de {a} tem {s:.2f} seno')
c = math.cos(math.radians(a))
print(f'O angulo de {a} tem {c:.2f} cosseno')
t = math.tan(math.radians(a))
print(f'O angulo de {a} tem {t:.2f} tangente')
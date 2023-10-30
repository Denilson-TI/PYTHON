# PYTHON
# Faça um programa que leia um algulo qualquer e mostre na tela o valor do seno, cosseno e tanjete

import math

angulo=float(input('Digite o angulo: '))

seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))

print('O angulo de {}, tem o valor de {:.2f}'.format(angulo,seno))
print('O angulo de {}, tem o cosseno de {:.2f}'.format(angulo,cosseno))
print('O angulo de {}, tem o valor de {:.2f}'.format(angulo,tangente))
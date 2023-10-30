# PYTHON
# Crie um programa que leia um numero real qualquer pelo teclado, e e mostre a sua porção inteira:

import math


num=float(input('Digite qualquer valor:'))
valor=math.trunc(num)

print('O numero {}, tem a porção inteira {}'.format(num,valor))
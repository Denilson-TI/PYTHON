#PYTHON
# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo, e raiz quadrada:
from math import sqrt,trunc

n=float(input('Digite um numero: '))
dobro = n * 2
triplo= n * 3
r_q = sqrt(n)
print('O doblo é: {}, o Triplo é: {} e a sua raiz quadrada é: {}'.format(dobro,triplo,trunc(r_q)))
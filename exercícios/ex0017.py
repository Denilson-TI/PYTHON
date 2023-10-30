# PYTHON
# Faca um programa que leiao comprimeto do cateto oposto e do cateto adjacente
#  de um triangulo retângulo, calcule e mmostre o comprimento da hipotenusa

from math import hypot

co=float(input('Digite o valor do ateto oposto: '))
ca=float(input('Digite o valor do cateto adjacente: '))

hi=hypot(co,ca)

print('Sendo o cateto oposto {},  e o cateto adjacente {}, resulta na hipotenusa {:.2f}'.format(co,ca,hi))
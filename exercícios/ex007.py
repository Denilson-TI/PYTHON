# PYTHON
# Desenvolva um programa que leia as quatro nota de um aluno. Calcule e mostre sua media:
from math import ceil

n1=float(input('Digite primeira nota: '))
n2=float(input('Digite segunda nota:  '))
n3=float(input('Digite terceira nota: '))
n4=float(input('Digite quarta nota:   '))
media=(n1+n2+n3+n4) / 4
# coloquei a funcionalidade (CEIL), da biblioteca math, para arredondar a nota para cima
print('A primeira nota foi : {} segunda nota: {} terceira nota : {} quarta nota :{} e sua media foi : {:.1f}'.format(n1,n2,n3,n4,ceil(media)))
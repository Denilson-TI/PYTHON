# PYTHON
# O professor quer sortear um dos seus 4 alunos  para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e sorteando o nome do escolhido.

import random

n1=str(input('PRIMEIRO NOME: '))
n2=str(input('SEGUNDO NOME: '))
n3=str(input('TERCEIRO NOME: '))
n4=str(input('QUARTO NOME: '))

lista=[n1,n2,n3,n4]

escolhido=random.choice(lista)

print(' ---------------------------------------------------------------------O escolhido foi {}'.format(escolhido))
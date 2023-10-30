# PYTHON
# O mesmo professor do exercicio anterior quer sortear a ordem de apresentação dos nomes dos alunos.
# Faça um programa que leia o nome dos alunos e sortei o nome dos alunos de mostre a ordem sorteada.

import random
n01=str(input('Primeiro  nome : '))
n02=str(input('Segundo nome : '))
n03=str(input('Terceiro nome:'))
n04=str(input('quarto nome: '))

lista=[n01,n02,n03,n04]

random.shuffle(lista)

print('A ordem escolhida foi: {}'.format(lista))
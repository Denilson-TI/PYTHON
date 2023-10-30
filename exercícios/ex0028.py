# Escreva um programa que faça o computador 'pensar' em um numero e inteiro entre 0-5, e peça para o usuario, 
# tentar descobrir qual foi o numero escolhido pelo computador . O programa deverá escvrever na tela se o usuario 
# venceu oou perdeu.

from random import randint
from time import sleep
computador = randint(0,5)
print('Pensei no numero: {}'.format(computador)) #faz o computador 'PENSAR'
print('=' *20)
print('Vou pensar numero entre 0-5. Tente adivinhar....')
print('=' *20)
jogador=int(input('Em que numero eu pensei ? ')) # Faz o jogador tentar adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você consseguiu me vencer!')
else:
    print('GANHEI !, Eu pensei no numero {} e não no numero {}!'.format(computador,jogador))

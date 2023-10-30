# Crie umm programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR:


from time import sleep
num=int(input('Digite um numero:  '))
valor= num % 2 
print('CARREGANDO...')
sleep(5)
if valor == 0:
    print('O numero é PAR')
else:
    print('O numero é IMPAR')
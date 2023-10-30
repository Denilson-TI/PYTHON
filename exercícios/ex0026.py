# PYTHON
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes apareceu a letra 'A'
# Em qual posição ela apareceu a primeira vez
# em qual posição ela a apareceu a ultima vez
frase=str(input('Digite uma frase: ')).strip().upper()
print('Analisando a frase.....')
print('A letra [a], aparece na frase {} vezes'.format(frase.count('A')))
print('A primeira letra a aparece na posição de {}'.format(frase.find('A')+1))
print('A ultima letra a aparece na posiçaõ de {}'.format(frase.rfind('A')+1))
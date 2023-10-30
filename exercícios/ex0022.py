# PYTHON
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# => O nome com todas letras maiúsculas.
# => O nome com todas maiúsculas.
# quantas letras ao todo sem considerar os espaços.
# Quantas letras tem o primeiro nome.

nome=str(input('Digite seu nome completo : ')).strip()
print(' O nome em  maiúscula é: {}'.format(nome.upper()))
print('O nome em minúsculo é: {} '.format(nome.lower()))
print('Ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
print(nome.find(' '))
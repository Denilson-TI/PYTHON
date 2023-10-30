# PYTHON
# Crie um programa que leia um nome e diga se tem 'SILVA' no nome.
nome=str(input('Digite o seu nome completo: ')).strip().lower()
print('Tem o nome [silva]? {}'.format('silva' in nome))
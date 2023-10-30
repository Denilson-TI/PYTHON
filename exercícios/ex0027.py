
# Faça um programa que leia o nome completo de uma pessoa e mostrando em seguida o primeiro e ultimo nome separadamente
# ex= Ana Maria de Souza
# Primeiro = ANA
# Ultimo = Souza

n =  str(input('Digite seu nome completo: ')).strip()
nome =  n.split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome))
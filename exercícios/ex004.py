# PYTHON
# Digite um programa que leia algo pelo teclado e mostre na tela o 
# seu tipo primitivo, e todas as informações possiveis sobre elas:
a=input('Digite um valor: ')
print('O valor digitado é do tipo:',type(a))
print('É um espaco: ',a.isspace())
print('E um numero: ',a.isnumeric())
print('É alfabetico:',a.isalpha())
print('É alfabeitico: ',a.isalnum())
print('É maisculas: ',a.isupper())
print('É minuscula:',a.islower())
print('É  capitalizada:',a.istitle())
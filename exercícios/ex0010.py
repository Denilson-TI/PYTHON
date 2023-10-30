# PYTHON 
# Crie um programa que leia quanto dinheiro dinheiro uma pessoa tem na carteira e mosrte quantos dolares ela pode comprar:
# considere U$$1.00 = 3.27

valor=float(input('Quantos $ voce tem na carteira: '))
dolar = valor / 3.27

print(' Com R${} Você pode comprar R${:.2f}'.format(valor,dolar))
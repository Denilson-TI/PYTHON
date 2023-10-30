# PYTHON 
# Faça um programa que leia o preço de um produto e mostre seu novo preço , com 5% de desconto:

preco=float(input('Digite o valor do produto: '))

novo_preco=preco-(preco*5/100)
print('O produto que custava {},  vai custa {}, na promoção de  5% !'.format(preco,novo_preco))
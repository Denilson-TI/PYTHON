# PYTHON
# Faça um programa que leia o salário de um funcionari, e mostre seu novo salário com 15% de aumento:

salario=float(input('Digite o valor do  salário atual: '))

novo=salario+(salario*15/100)

print('O salario do funcionario que era ${}, ficou ${} com o aumento de 15% !'.format(salario,novo))
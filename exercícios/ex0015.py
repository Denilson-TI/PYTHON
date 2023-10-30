# PYTHON
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado a quantidade de dias pelos quais
# ele foi alugado, calcule o preço a pagar, sabendo que o carro custava $60 por dia, e $0,50 por km rodado.

km=float(input('Quantos km foram percorridos: '))
dia=float(input('Qunatos dias foi ultilizado:'))

pago = (dia * 60) + (km * 0.50)


print(' O total a pagar é ${}'.format(pago))
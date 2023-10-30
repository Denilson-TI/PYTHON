# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem cobrando R$0,50 por KM para viagens de ate 200km . E R$ 0,45 para viagens mais longas

km = float(input('Digite os km :'))
if km <= 200:
    preco1 = km * 0.50
    print(' O valor que você terá que pagar é de R$ {}'.format(preco1))

else:
    preco2 =  km * 0.45
    print('O valor a ser pago será de: R$ {}'.format(preco2))
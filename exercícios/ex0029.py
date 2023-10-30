# Escreva um programa que leia a velocidade de u carro , se ele ultrapassar a velocidade de 
# 80 km/h, mostre uma mensagem dizendo que ele foi multado, A ulta vai custar R$7,00 por km acima do limite.

velocidade=float(input('Qual a velocidade do carro: '))
if velocidade > 80:
    print('MULTADO!, Você excedeu o limite permitido que é de 80km/h')
    multa=(velocidade-80)*7
    print('Você deve pagar o valor de R${:.2F}!'.format(multa))
else:
    print('Tenha um BOM DIA , dirija com segurança')

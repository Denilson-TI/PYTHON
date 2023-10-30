# PYTHON
# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua area 
# e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta , pinta uma area de 2m².

lar = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))

area = lar * alt

print(' A dimensão da area da parede é de {} m'.format(area))

tinta = area / 2

print('Para pintar a parede vai precisar de {} litros de tinta!'.format(tinta))
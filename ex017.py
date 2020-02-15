# Faça um programa que leia o comprimento do cateto oposto e o adjacente de um triângulo retângulo. Calcule e mostre o
# resultado
from math import sqrt

cateto_adj = float(input('Informe a medida do cateto adjacente: '))
cateto_oposto = float(input('Informe a medida do cateto oposto: '))
hip = sqrt((cateto_adj ** 2) + (cateto_oposto ** 2))
print(f'A hipotenusa vale {hip:.2f}')

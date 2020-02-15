# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tângente
import math

angulo = float(input('Informe o ângulo: '))
print(f'Seno: {math.sin(math.radians(angulo)):.2f}')
print(f'Cosseno: {math.cos(math.radians(angulo)):.2f}')
print(f'Tângente: {math.tan(math.radians(angulo)):.2f}')

# Faça um programa que leia uma medida em metros e converta em centimetros e milimetros
metros = float(input('Digite um valor em metros: '))
print(f'Km: {(metros / 1000)}')
print(f'Hm: {metros / 100}')
print(f'Dam: {metros / 10}')
print(f'Dm: {metros * 10}')
print(f'Cm: {metros * 100}')
print(f'Mm: {metros * 1000}')

# Faça um programa que leia um número e exiba a sua tabuada
num = int(input('Digite um número: '))
print()
print('-'*10, f'Tabuada do {num}', '-'*10)
for i in range(0, 11):
    print(f'{num} x {i} = {(num * i):2}')

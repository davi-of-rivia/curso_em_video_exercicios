# Faça um programa que leia um número e mostre o seu sucessor e antecessor
num = 0
while True:
    num = input('Digite um número: ')
    if num.isnumeric():
        num = int(num)
        break
print()
print(f'Analisando o número {num}, seu antecessor é {num - 1} e seu sucessor é {num + 1}')

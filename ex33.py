# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
maior = 0
menor = 0

for i in range(0, 3):
    numero = int(input(f'Digite o {i + 1}º número: '))
    if i == 0:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f'O maior número digitado foi {maior} e o menor foi {menor}')

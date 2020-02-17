"""
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra 'A', em que posição ela aparece
a primeira e última vez.
"""
frase = str(input('Digite a frase: ')).strip().upper()
letra = str(input('Informe a letra que você deseja achar nessa frase: ')).strip().upper()
print(f'A letra "{letra}" aparece {frase.count(letra)} vezes.')
print(f'A letra "{letra}" aparece pela primeira vez na posição {frase.replace(" ", "").find(letra) + 1}')
print(f'A letra "{letra}" aparece pela última vez na posição: {frase.replace(" ", "").rfind(letra) + 1}')

# Desenvolva um programa que leia três comprimentos de retas e diga se elas podem ou não formar um triângulo.
r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('As retas acima PODEM FORMAR um triângulo!')
else:
    print('As retas acima NÃO PODEM FORMAR um triângulo!')

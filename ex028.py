"""
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o úsuario tentar descobrir
qual foi o número escolhido pelo computador. O programa deve informar se o úsuario venceu ou perdeu.
"""
from random import randint

num_computador = randint(0, 5)
print('='*10, 'Jogo da adivinhação', '='*10)
num = int(input('Digite um número entre 0 e 5: '))

if num_computador == num:
    print('Parabéns, você acertou!')
else:
    print('Infelizmente, você errou!')
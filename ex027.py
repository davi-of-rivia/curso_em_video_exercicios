# Faça um programa que leia o nome completo de uma pessoa e em seguida mostre o primeiro e último nome.
nome = str(input('Digite o seu nome completo: '))
nome_separado = nome.split(' ')
print(f'Primeiro nome: {nome_separado[0]}')
print(f'Último nome: {nome_separado[len(nome_separado) - 1]}')

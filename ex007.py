# Faça um programa que leia as duas notas de um aluno e mostre a sua média
nome = input('Digite o nome do aluno: ').strip()
nota1 = float(input(f'Digite a primeira nota do(a) {nome}: '))
nota2 = float(input(f'Digite a segunda nota do(a) {nome}: '))
print()
print(f'A média do(a) {nome} é {(nota1 + nota2) / 2}')

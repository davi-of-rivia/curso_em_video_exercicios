"""
O mesmo professor do exercício 19 quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que
leia o nome dos quatros alunos e mostre a ordem sorteada.
"""
from random import shuffle

nomes = []
for i in range(0, 4):
    nomes.append(input(f'Informe o nome do(a) {i + 1} aluno(a): '))

# a função shuffle embaralha a orderm da lista
shuffle(nomes)
print()
print('Ordem sorteada: ')
for i in range(0, 4):
    print(nomes[i])
"""
Um professor quer sortear um dos quatros alunos para limpar o quadro. Faça um programa que ajude ele a escolher um de
seus alunos para limpar.
"""
from random import choice

nomes = []
for i in range(0, 4):
    nomes.append(input(f'Qual o nome do {i + 1}ª do(a) aluno(a): '))
print()
# O choice escolhe um elemento dentro da lista aleatóriamente
print(f'O aluno escolhido para limpar o quadro foi {choice(nomes)}')

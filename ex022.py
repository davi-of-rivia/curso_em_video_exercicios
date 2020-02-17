"""
Crie um programa que leia o nome completo do usuário e mostre:

- O nome com letras maiúsculas e minúsculas
- Quantas letras ao todo (sem considerar os espaços)
- Quantas letras tem o primeiro nome
"""
nome_completo = input('Digite o seu nome: ').strip().title()
# Armazenando o primeiro nome
nome = nome_completo.split(' ')
primeiro_nome = nome[0]
print(f'Nome em letras maiúsculas: {nome_completo.upper()}')
print(f'Nome em letras minúscluas: {nome_completo.lower()}')
print(f'Letras ao total: {len(nome_completo.replace(" ", ""))} letras')
print(f'Quantidade de letras do primeiro nome: {len(primeiro_nome)}')

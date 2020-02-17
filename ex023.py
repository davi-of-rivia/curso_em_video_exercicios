# Faça um programa que leia um número de 0 a 9999 e moste na tela cada um dos dígitos separados
num = int(input('Informe um número entre 0 a 9999: '))
# Fatiando a string para separar os dígitos
unidade = int(num / 1 % 10)
dezena = int(num / 10 % 10)
centena = int(num / 100 % 10)
milhar = int(num / 1000 % 10)

# Printando o resultado
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')

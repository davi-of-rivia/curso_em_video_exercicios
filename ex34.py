"""
Escreva um programa que pergunte um salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.
"""
import locale

# Definindo o locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

nome = str(input('Informe o nome do funcionário: ')).strip()
salario = float(input('Digite o salário do funcionário: '))
novo_sal = 0

if salario <= 1250.00:
    novo_sal = salario + (salario * 0.15)
else:
    novo_sal = salario + (salario * 0.1)

print(f'O novo salário do(a) {nome} é de {locale.currency(novo_sal)}')

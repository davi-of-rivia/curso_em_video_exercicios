# Faça um algoritmo que leia o salário do funcionário e mostre o seu novo salário com 15% de aumento
import locale

# Definindo um locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

funcionario = str(input('Digite o nome do funcionário: ')).strip().title()
salario = float(input(f'Informe o salário do(a) {funcionario}: R$'))
novo_salario = salario + (salario * 0.15)
print(f'O salário do(a) {funcionario} era {locale.currency(salario)} e com o reajuste de 15% fica '
      f'{locale.currency(novo_salario)}')

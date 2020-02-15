# Faça um algoritmo que leia um preço de um produto e mostre o seu novo preço com 5% de desconto
import locale

# Definindo o locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

preco = float(input('Digite o preço do produto: '))
print(f'O preço do produto é {locale.currency(preco)} e com 5% de desconto fica '
      f'{locale.currency(preco - (preco * 0.05))}')

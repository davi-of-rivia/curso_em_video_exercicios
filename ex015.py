"""
Faça um programa que pergunte a quantiade de Km rodados por um carro alugado e a quantidade de dias que o mesmo foi
alugado. Calcule o preço a pagar, sabedo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
"""
import locale

# Definindo o locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

km_rodado = float(input('Informe a quantiade de Km rodados: '))
dias_alugados = int(input('Informe a quantidade de dias que o carro foi alugado: '))
aluguel = (km_rodado * .15) + (dias_alugados * 60)
print(f'O valor que você deve pagar pelo aluguel é de {locale.currency(aluguel)}')

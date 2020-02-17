"""
Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
multado. A multa vai custar R$7,00 por cada Km/h acima do limite.
"""
import locale

# Definindo o locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
km_h = int(input('Informe o Km/h: '))

if km_h > 80:
    km_h_excedente = km_h - 80
    multa = km_h_excedente * 7
    print(f'O valor da multa é de {locale.currency(multa)}')
else:
    print('Tá suave')

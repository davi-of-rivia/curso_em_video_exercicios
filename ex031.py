"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
Km para viagem até 200Km e R$0,45 para viagens mais longas.
"""
import locale

# Definindo o locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
viagem = int(input('Informe a distância da viagem em Km: '))
total_viagem = 0

if viagem <= 200:
    total_viagem = viagem * 0.5
else:
    total_viagem = viagem * 0.45

print(f'A viagem irá custar {locale.currency(total_viagem)}')

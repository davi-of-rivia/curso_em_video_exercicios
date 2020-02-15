"""
Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
"""
alt = float(input('Informe a altura da parede: '))
larg = float(input('Informe a largura da parede: '))
area = larg * alt
qtd_tinta = area / 2
print(f'Uma parede de área {area:.2f}m² precisa de {qtd_tinta:.2f}l de tinta!')

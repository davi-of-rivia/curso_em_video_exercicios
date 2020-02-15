# Escreva um programa que leia uma temperatura em graus Celsius e converta para Fahrenheit e Kelvin
celsius = float(input('Informe a temperatura em °C: '))
f = (celsius * (9 / 5)) + 32
kelvin = celsius + 273.15
print(f'Em fahrenheit: {f:.1f}')
print(f'Em kelvin: {kelvin:.2f}')

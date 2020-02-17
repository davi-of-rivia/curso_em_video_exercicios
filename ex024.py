cidade = str(input('Digite o nome de uma cidade: '))
primeiro_nome = cidade.split(' ')

if primeiro_nome[0] == 'Santo':
    print(True)
else:
    print(False)

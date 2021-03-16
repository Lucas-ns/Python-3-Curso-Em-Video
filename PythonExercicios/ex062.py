print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
número = int(input('Primeiro valor: '))
razão = int(input('Razão da PA: '))
termo = número
cont = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont < total:
        print('{} '.format(termo), end='-> ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

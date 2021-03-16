números = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
cont = 0
while True:
    usuário = int(input('Digite um número entre 0 e 20: '))
    while usuário < 0 or usuário > 20:
        usuário = int(input('Tente novamente! Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {números[usuário]}')
    print('-' * 30)
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    if res in 'N':
        break
print(f'Terminando o Programa!\n'
      f'Você digitou {cont} números no total.')
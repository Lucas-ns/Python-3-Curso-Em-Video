print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totced = 0
while True:
    if total >= céd:
        total -= céd
        totced += 1
    else:
        if totced > 0:
            print(f'Foram necessárias {totced} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totced = 0
        if total == 0:
            break
print('Obrigado por usar nosso serviço! Tenha um bom dia.')

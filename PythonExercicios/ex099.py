def maior(* num):
    print('-=' * 30)
    cont = maior = 0
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
    print()
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
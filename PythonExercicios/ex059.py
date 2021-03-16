from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opção = 0
maior = 0
while opção != 5:
    opção = int(input('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
>>>> Qual é sua opção? '''))

    if opção == 1:
        print('A soma entre {} + {} = {}'.format(v1, v2, v1+v2))
    elif opção == 2:
        print('O resultado de {} x {} é {}'.format(v1, v2, v1*v2))
    elif opção == 3:
        if v1 > v2:
            maior = v1
        elif v2 > v1:
            maior = v2
        else:
            print('São iguais.')
        print('Entre {} e {} o maior valor é {}'.format(v1, v2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 15)

print('Fim do programa! Volte sempre!')
from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
soma = cont = 0
while True:
    n = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    pc = randint(0, 10)
    soma += n + pc
    if soma % 2 == 0:
        print('-' * 30)
        print(f'Você jogou {n} e o computador {pc}. Total de {soma} DEU PAR')
        print('-' * 30)
    elif soma % 2 == 1:
        print('-' * 30)
        print(f'Você jogou {n} e o computador {pc}. Total de {soma} DEU ÍMPAR')
        print('-' * 30)
    if soma % 2 == 0 and escolha == 'P':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
    elif soma % 2 == 1 and escolha == 'I':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
    else:
        print('Você PERDEU!')
        break
    soma = 0
    cont += 1
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')
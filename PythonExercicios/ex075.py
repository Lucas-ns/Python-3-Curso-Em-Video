números = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {números}')
if números.count(9) > 1:
    print(f'O valor 9 apareceu {números.count(9)} vezes')
else:
    print(f'O valor 9 apareceu {números.count(9)} vez')
if 3 in números:
    print(f'O valor 3 apareceu na {números.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in números:
    if n % 2 == 0:
        print(f'{n}', end=' ')

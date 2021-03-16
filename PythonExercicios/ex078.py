value = []
for cont in range(0, 5):
    value.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Você digitou os valores {value}')
print(f'O maior valor digitado foi {max(value)} nas posições ', end='')
for i, v in enumerate(value):
    if v == max(value):
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {min(value)} nas posições ', end='')
for i, v in enumerate(value):
    if v == min(value):
        print(f'{i}...', end=' ')
print()

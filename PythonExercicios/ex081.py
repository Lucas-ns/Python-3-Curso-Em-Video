lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    res = str(input('Quer continuar? [S/N] ')).upper().strip()
    cont += 1
    if res == 'N':
        break
lista.sort(reverse=True)
print('-=' * 50)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
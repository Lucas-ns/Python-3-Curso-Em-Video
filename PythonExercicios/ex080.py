números = []
maior = 0
menor = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        maior = menor = n
        números.append(n)
        print('Adicionado ao final da lista...')
    else:
        if n > maior:
            maior = n
            números.append(maior)
            print('Adicionado ao final da lista...')
        elif n < menor:
            menor = n
            números.insert(0, menor)
            print('Adicionado na posição 0 da lista...')
        elif n < números[-1]:
            números.insert(-1, n)
            print('Adicionado antes do último...')
        else:
            números.insert(1, n)
            print('Adicionado antes do último!')
print('-=' * 30)
print(f'Os valores digitados em ordem foram {números}')
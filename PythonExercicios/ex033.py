n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))
maior = n1
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O menor valor digitado foi {}'.format(menor))
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('O maior valor digitado foi {}'.format(maior))

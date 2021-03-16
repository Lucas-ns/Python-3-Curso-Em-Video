número = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(número, f'{número:b}'))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(número, f'{número:0o}'))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(número, f'{número:0x}'))
else:
    print('Opção inválida! Tente novamente.')

def leiaInt(msg):
    n = (input(msg))
    while n.isalpha() or n == '':
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        n = (input(msg)).lstrip()
    return n


n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}.')

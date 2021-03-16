def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\n\033[31mO usuário preferiu não digitar o valor.\033[m')
            return 0
        else:
            return n
            break


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        except(KeyboardInterrupt):
            print(f'\n\033[31mO usuário preferiu não digitar o valor.\033[m')
            return 0
        else:
            return n
            break


i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
user = int(input('Quantos termos você quer mostrar? '))
cont = 0
primeiro = 0
segundo = 1
res = 1
while cont < user:
    print('{} '.format(primeiro), end='-> ')
    primeiro = segundo
    segundo = res
    res = primeiro + segundo
    cont += 1
print('FIM')
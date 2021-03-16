num = int(input('Digite um número para\ncalcular seu Fatorial: '))
total = 1

# While
'''print('Calculando {}! = {} '.format(num, num), end='')
while num != 1:
    total *= num
    num -= 1
    print('x {} '.format(num), end='')
print('= {}'.format(total))'''

# For
print('Calculando {}! = '.format(num), end='')
for c in range(num, 0, -1):
    print(c, 'x ' if c > 1 else '= ', end='')
    total *= c
print('{}'.format(total))

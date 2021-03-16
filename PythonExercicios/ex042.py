a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a == b or a == c or c == b:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

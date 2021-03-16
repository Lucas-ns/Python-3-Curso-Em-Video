from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hipotenusa = pow((co ** 2) + (ca ** 2), 1/2)
hipotenusa = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))


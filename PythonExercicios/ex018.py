from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
radianos = radians(ângulo)
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, sin(radianos)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cos(radianos)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tan(radianos)))

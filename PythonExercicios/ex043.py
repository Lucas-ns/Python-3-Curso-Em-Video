peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de peso IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('CUIDADO! Você está com OBESIDADE MÓRBIDA!')
def leiaDinheiro(p):
    preço = str(input(p)).lstrip().replace(',', '.')
    while preço.isalpha() or preço == '':
        print(f'\033[;31mERRO: "{preço}" é um preço inválido!\033[m')
        preço = str(input('Digite o preço: R$')).strip()
    return float(preço)

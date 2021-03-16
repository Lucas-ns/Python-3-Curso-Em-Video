def aumentar(preço=0, taxa=0, formato=False):
    preço += preço * (taxa/100)
    return preço if formato is False else moeda(preço)


def diminuir(preço=0, taxa=0, formato=False):
    preço -= preço * (taxa / 100)
    return preço if formato is False else moeda(preço)


def dobro(preço=0, formato=False):
    preço = preço * 2
    return preço if formato is False else moeda(preço)


def metade(preço = 0, formato=False):
    preço = preço / 2
    return preço if formato is False else moeda(preço)


def moeda(preço=0, moeda='R$'):
        return f'{moeda}{preço:>.2f}'.replace('.', ',')
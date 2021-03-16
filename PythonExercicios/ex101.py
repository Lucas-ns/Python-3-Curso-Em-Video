def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 65 >= idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


print('-' * 30)
print(voto(int(input('Em que ano você nasceu? '))))

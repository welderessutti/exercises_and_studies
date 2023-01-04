def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif 16 <= idade < 18 or idade > 70:
        return f"Com {idade} anos: VOTO OPCIONAL."
    elif 18 <= idade <= 70:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."


nasc = int(input("Em que ano você nasceu?: "))
print(voto(nasc))

def price_of_paint(parede):
    preco_lata = 80
    qtd_lts = parede / 3
    qtd_latas = qtd_lts // 18
    if qtd_lts % 18:
        qtd_latas += 1
    return qtd_latas, qtd_latas * preco_lata
    

print(price_of_paint(55))
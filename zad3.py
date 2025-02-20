from decimal import Decimal

def stworz_liste(start, koniec, skok):
    start = Decimal(start)
    koniec = Decimal(koniec)
    skok = Decimal(skok)

    rezultat = []
    while start <= koniec: 
        rezultat.append(start)
        start += skok
    
    return rezultat

lista = stworz_liste(2, 5.5, 0.5)

for num in lista:
    print(num)

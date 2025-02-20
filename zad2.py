def znajdz_brakujacy_element(podana_lista, n):
    lista = set(range(1, n + 1))
    zbior = set(podana_lista)
    brakujace_elementy = list(lista - zbior)

    return sorted(brakujace_elementy)

podana_lista = [2, 3, 7, 4, 9]
n = 10
brakujace_elementy = znajdz_brakujacy_element(podana_lista, n)
print(brakujace_elementy)

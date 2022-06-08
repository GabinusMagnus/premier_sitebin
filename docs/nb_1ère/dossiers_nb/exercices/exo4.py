def indice_min(nombres):
    liste = []
    liste.append(nombres)
    for i in range(liste):
        if i < nombres :
            return i
    


# tests

assert indice_min([5]) == 0
assert indice_min([2, 4, 1, 1]) == 2
assert indice_min([5, 3, 2, 5, 2]) == 2


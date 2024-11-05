def my_sort(lst):
    n = len(lst)
    total_moves = 0
    sortie = False
    while not sortie:
        sortie = True
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                # Échange des éléments adjacents
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                total_moves += 1
                sortie = False
    return lst, total_moves

# Exemple d'utilisation
ma_liste = [64, 34, 22, 12,90,25,11]
liste_triee, coups = my_sort(ma_liste)
print("Nombre total de coups nécessaires pour trier la liste : ", coups)
print("Liste triée: ", liste_triee)

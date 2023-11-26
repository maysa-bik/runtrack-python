def my_sort(liste):
    coups = 0  # Initialiser le nombre total de coups à zéro
    trie = False  # Variable pour indiquer si la liste est triée

    while not trie:
        trie = True  # Supposons que la liste est triée à chaque itération

        for i in range(len(liste) - 1):
            # Comparer les éléments adjacents et échanger s'ils sont dans le mauvais ordre
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                trie = False  # La liste n'est pas encore triée
                coups += 1  # Incrémenter le nombre total de coups

    return liste, coups

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
liste_triee, nombre_coups = my_sort(ma_liste)

# Affichage du résultat
print(liste_triee)
print(nombre_coups)

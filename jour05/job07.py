def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        # Vérifier si la note est inférieure à 40
        if note < 40:
            notes_arrondies.append(note)
        else:
            # Calculer le prochain multiple de 5 supérieur ou égal à la note
            prochain_multiple_de_5 = ((note // 5) + 1) * 5

            # Vérifier si la note est à moins de 3 points du prochain multiple de 5
            if prochain_multiple_de_5 - note < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation
liste_notes = [37, 45, 82, 93, 68]
print(liste_notes)
notes_arrondies = arrondir_notes(liste_notes)

# Affichage du résultat
print(notes_arrondies)

#_______________________________________________

def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40: # si la note est inférieure à 40, l'étudiant échoue
            notes_arrondies.append(note)
        else: # si la note est supérieure ou égale à 40, l'étudiant réussit
            prochain_multiple_de_5 = int(note / 5 + 1) * 5
            if note < prochain_multiple_de_5 - 3: # si la note est moins de 3 points du multiple suivant
                notes_arrondies.append(note) # on ne fait pas d'arrondi
            else: # si la note est à moins de 3 points du multiple suivant
                notes_arrondies.append(prochain_multiple_de_5) # on arrondit à ce multiple
    return notes_arrondies

notes = [82, 83, 92, 98, 54, 40, 41, 42, 43, 44]
print(notes)
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)

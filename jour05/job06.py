def distance_gardien_wc(marches, hauteur):
    distance_m_semaine = marches / (120 - (2.5 * hauteur))
    return distance_m_semaine

marches = 5
hauteur = 20
distance = distance_gardien_wc(marches, hauteur)
print(f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {distance:.2f} m par semaine.")

#_____________________________________ 2 manière

def distance_toilettes(marches, hauteur_marche):
    # Nombre de marches aller-retour par jour
    marches_jour = 2 * marches

    # Distance totale par jour en mètres
    distance_jour = marches_jour * hauteur_marche / 100

    # Distance totale par semaine en mètres
    distance_semaine = 7 * distance_jour

    return distance_semaine

# Exemple d'utilisation
nombre_marches = 5
hauteur_marche_cm = 20
distance_total = distance_toilettes(nombre_marches, hauteur_marche_cm)

# Affichage du résultat
print(f"Pour {nombre_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_total:.2f} m par semaine.")

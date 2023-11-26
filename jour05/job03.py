def drw_triangle(height):
    if height <= 0:
        print("la hauteur doit être supérieure à zéro.")
        return
    # boucle pour chaque ligne du triangle 
    for i in range(height):
        # calcul de l'espace avant le côte guche du tringle
        spaces_before = ' ' * (height - i -1)

        # calcul de l'espace entr les côtes  du tringle

        spaces_between = ' ' * (2 * i)

        #afichage de la ligne du tringle 
        if i == 0:
            print(spaces_before + "/\\")
        elif i == height - 1:
            print("/" + "_" * (2 * height - 2) + "\\")    
        else:
            print(spaces_before + "/" + spaces_between + "\\")  

# tester 
drw_triangle(5)              





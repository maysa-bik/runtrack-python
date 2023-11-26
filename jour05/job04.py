def afficher_tapis(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j or i == 0 or i == n:
                print('-', end=" ")
            else:
                print('#', end=" ")
        print()

# Tester avec une taille de 10
taille_tapis = 10
afficher_tapis(taille_tapis)




def rectangle(width, height):
    if width <= 0 or height <= 0:
        print("le 'height' et la 'width' doivent être superieures à zéro.")
        return
    
    print('|' + '-' * (width - 2) + '|')
    
    for _ in range(height - 2 ):
        print('|' + ' ' * (width - 2) + '|')
    if height > 1:
        print('|' + '-' * (width - 2) + '|')

# Appeler la fonction pour afficher le rectangle avec width=10 et height=3
rectangle(10, 3)





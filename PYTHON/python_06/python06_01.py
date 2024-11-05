def draw_rectangle(width, height):
    # Ligne du haut
    print('|' + '-' * (width - 2) + '|')
    
    # Lignes du milieu
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    
    # Ligne du bas (si la hauteur est suffisante pour avoir une ligne du bas)
    if height > 1:
        print('|' + '-' * (width - 2) + '|')

# Exemple d'utilisation
draw_rectangle(10, 3)
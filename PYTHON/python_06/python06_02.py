def draw_triangle(height):
    # Parcourir chaque ligne du triangle
    for i in range(height - 1):
        # Ajouter des espaces pour centrer la ligne
        print(" " * (height - i - 1) + "/" + " " * (2 * i) + "\\")

    # Dernière ligne (base du triangle)
    print("/" + "_" * (2 * (height - 1)) + "\\")

# Exemple d'utilisation
draw_triangle(5)
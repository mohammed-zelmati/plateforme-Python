def draw_triangle(height):
    # Parcourir chaque ligne du triangle
    for i in range(height - 1):
        # Ajouter des espaces pour centrer la ligne
        print(" " * (height - i - 1) + "/" + " " * (2 * i) + "\\")

    # Dernière ligne (base du triangle)
    print("/" + "_" * (2 * (height - 1)) + "\\")

# Exemple d'utilisation
def tapis(n):
    print("+" + "-" *( n+1) + "+")
    i=0
    while i < n + 1:
        print("|" + "#" *( n-i) + " " + "#"* i + "|")
        i +=1
    print("+" + "-" *( n+1) + "+")
tapis(10)    
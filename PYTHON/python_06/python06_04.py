def decale_message(message, decalage):
    resultat = []
    for caractere in message:
        if caractere.isalpha():
            # Déterminer la base (majuscule ou minuscule)
            base = ord('A') if caractere.isupper() else ord('a')
            # Calculer le nouveau caractère décalé
            nouveau_caractere = chr((ord(caractere) - base + decalage) % 26 + base)
            resultat.append(nouveau_caractere)
        else:
            # Ajouter les caractères non alphabétiques sans modification
            resultat.append(caractere)
    return ''.join(resultat)
# Exemple d'utilisation
message = "abcd wxyz!"
decalage = 3
print(decale_message(message, decalage)) 

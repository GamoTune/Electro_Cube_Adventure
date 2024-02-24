# Exemple de conversion d'une liste de deux entiers en une chaîne de caractères

# La liste de deux entiers [12, 34]
liste1 = [12, -34]

# Convertir chaque entier en chaîne de caractères avec la fonction str()
liste1_str = [str(i) for i in liste1]

# Concaténer les deux chaînes de caractères avec la méthode join()
test = ",".join(liste1_str)

# Afficher la chaîne de caractères résultante
print(test)  # Affiche "1234"
# EXERCICE 1 - Lecture fichier texte

with open("ordres.txt", "r") as fichier:
    contenu = fichier.read()

print(contenu)

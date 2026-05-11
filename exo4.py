# EXERCICE 4 - Manipulation JSON

import json

with open("portefeuille.json", "r") as fichier:
    data = json.load(fichier)

print(data["ticker"])
print(data["quantite"])
print(data["prix"])
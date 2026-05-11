# PROJET - Analyse portefeuille trading

import pandas as pd

df = pd.read_csv("reporting.csv")

# Nombre total positions
nombre_positions = len(df)

# PnL total
pnl_total = df["PnL"].sum()

# Positions perdantes
pertes = df[df["PnL"] < 0]

# PnL moyen par produit
moyenne_produit = df.groupby("Produit")["PnL"].mean()

# Produit meilleur PnL
meilleur = df.loc[df["PnL"].idxmax()]

print("Nombre de positions :", nombre_positions)
print("PnL total :", pnl_total)

print("\n=== Positions perdantes ===")
print(pertes)

print("\n=== PnL moyen par produit ===")
print(moyenne_produit)

print("\n=== Meilleur produit ===")
print(meilleur)

# BONUS 1
pertes.to_csv("positions_perdantes.csv", index=False)

# BONUS 2
df["Risque"] = df["PnL"].apply(
    lambda x: "Élevé" if x < 0 else "Faible"
)

print("\n=== Données avec risque ===")
print(df)
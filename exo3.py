# EXERCICE 3 - Calculs avec pandas

import pandas as pd

df = pd.read_csv("positions.csv")

volume_total = df["Quantite"].sum()
pnl_total = df["PnL"].sum()
pnl_moyen = df["PnL"].mean()

print("Volume total :", volume_total)
print("PnL total :", pnl_total)
print("PnL moyen :", pnl_moyen)
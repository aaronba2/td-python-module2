# EXERCICE 5 - Analyse groupby

import pandas as pd

df = pd.read_csv("trading.csv")

resultat = df.groupby("Desk")["PnL"].mean()

print(resultat)
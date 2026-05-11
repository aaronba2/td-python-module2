# EXERCICE 2 - Lecture CSV avec pandas

import pandas as pd

df = pd.read_csv("positions.csv")

print("=== 5 premières lignes ===")
print(df.head())

print("\n=== Positions perdantes ===")
print(df[df["PnL"] < 0])

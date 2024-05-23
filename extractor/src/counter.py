import pandas as pd

df = pd.read_csv("ground_truth_100.csv", sep="|")
for col in [
    "direccion",
    "fot",
    "irregular",
    "medidas",
    "esquina",
    "barrio",
    "frentes",
    "pileta",
]:
    print(df[col].notna().sum())


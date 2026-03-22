# junta todos os CSVs da pasta em um arquivo único

import os
import glob
import pandas as pd

INPUT_FOLDER = os.path.join("data", "csvs")
OUTPUT_FILE  = os.path.join("data", "nome_final_do_arquivo.csv")

dataframes = []

for file in glob.glob(os.path.join(INPUT_FOLDER, "*.csv")):
    filename = os.path.basename(file).lower()
    category = filename.split("_")[0].replace(".csv", "")

    df = pd.read_csv(file)
    cols = [c.lower() for c in df.columns]

    if "periodo" not in cols or "valor" not in cols:
        continue

    df = df[[df.columns[cols.index("periodo")], df.columns[cols.index("valor")]]]
    df.columns = ["periodo", "valor"]
    df["categoria"] = category

    dataframes.append(df)

df_geral = pd.concat(dataframes, ignore_index=True)
df_geral = df_geral.sort_values(by=["categoria", "periodo"])

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
df_geral.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print(f"salvo em {OUTPUT_FILE}")

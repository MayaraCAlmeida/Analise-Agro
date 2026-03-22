# confere um pedaço do CSV antes de mandar pro banco

import pandas as pd

CSV_PATH = r"caminho/do/arquivo.csv"

df = pd.read_csv(CSV_PATH)
print(df.iloc[10:16])

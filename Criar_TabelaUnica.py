# importa CSV pro postgres pra usar no Power BI

import os
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:senha@localhost:5432/NomeDaDatabase"
CSV_PATH = os.path.join("data", "nome_do_arquivo.csv")

engine = create_engine(DATABASE_URL)

df = pd.read_csv(CSV_PATH)
print(df.head())

df.to_sql("nome_da_tabela", engine, if_exists="replace", index=False)
print("feito")

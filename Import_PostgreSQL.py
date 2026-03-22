# lê o CSV, separa por categoria e cria uma tabela pra cada uma no postgres

import os
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:senha@localhost:5432/NomeDaDatabase"
CSV_PATH = os.path.join("data", "nome_do_arquivo.csv")

engine = create_engine(DATABASE_URL)


def limpar_nome(nome):
    nome = nome.lower().strip()
    subs = {"ç":"c","ã":"a","á":"a","â":"a","à":"a","é":"e","ê":"e",
            "í":"i","ó":"o","ô":"o","õ":"o","ú":"u"," ":"_"}
    for a, b in subs.items():
        nome = nome.replace(a, b)
    return nome


df = pd.read_csv(CSV_PATH)

for categoria in df["categoria"].unique():
    nome_tabela = f"agro_{limpar_nome(categoria)}"
    filtrado = df[df["categoria"] == categoria]
    filtrado.to_sql(nome_tabela, engine, if_exists="replace", index=False)
    print(f"{nome_tabela}: {len(filtrado)} linhas")

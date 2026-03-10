"""
Script para unificar vários arquivos CSV em um único arquivo geral.

Este script:
- Lê todos os arquivos CSV dentro de uma pasta;
- Extrai a categoria a partir do nome do arquivo;
- Mantém apenas as colunas "periodo" e "valor";
- Padroniza nomes de colunas;
- Concatena todos os CSVs em um único DataFrame;
- Salva o arquivo final na pasta /data.

Exemplo de estrutura de pastas:

data/
    bovinos_2020.csv
    suinos_2020.csv
    cafe_2019.csv
scripts/
    gerar_geral.py
"""

import pandas as pd
import glob
import os

# Pasta contendo os arquivos CSV
INPUT_FOLDER = os.path.join("data", "csvs")  # Ex: data/csvs/

# Caminho de saída para o arquivo unificado
OUTPUT_FILE = os.path.join("data", "nome_final_do_arquivo.csv")

# Pega todos os arquivos CSV na pasta
csv_files = glob.glob(os.path.join(INPUT_FOLDER, "*.csv"))

dataframes = []

for file in csv_files:
    filename = os.path.basename(file).lower()  # ex: bovinos_2020.csv
    category = filename.split("_")[0].replace(".csv", "")  # ex: bovinos

    # Lê o CSV
    df = pd.read_csv(file)

    # Normaliza nomes das colunas
    cols = [c.lower() for c in df.columns]

    # Verifica se contém as colunas obrigatórias
    if "periodo" in cols and "valor" in cols:
        df = df[[df.columns[cols.index("periodo")], df.columns[cols.index("valor")]]]
    else:
        continue  # pula arquivos fora do padrão

    # Renomeia as colunas
    df.columns = ["periodo", "valor"]

    # Adiciona a categoria como coluna
    df["categoria"] = category

    # Armazena para juntar depois
    dataframes.append(df)

# Concatena tudo
df_geral = pd.concat(dataframes, ignore_index=True)

# Ordena para organização
df_geral = df_geral.sort_values(by=["categoria", "periodo"])

# Salva o resultado final
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
df_geral.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print("✅ Arquivo CSV unificado gerado com sucesso!")
print(f"📁 Local: {OUTPUT_FILE}")

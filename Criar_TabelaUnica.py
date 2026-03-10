"""
Script para importar um arquivo CSV e criar uma tabela única no PostgreSQL,
para ser utilizada em dashboards no Power BI.

Este script:
- Lê um arquivo CSV contendo dados;
- Exibe as primeiras linhas para conferência;
- Cria (ou substitui) uma tabela única no banco PostgreSQL;
- Insere todos os registros do CSV nessa tabela.
"""

import pandas as pd
from sqlalchemy import create_engine
import os


# ===== CONFIGURAÇÕES =====
DATABASE_URL = "postgresql://postgres:senha@localhost:5432/NomeDaDatabase"

# Caminho genérico para uso no GitHub (pasta local 'data/')
CSV_PATH = os.path.join("data", "nome_do_arquivo.csv")

# Criar conexão com o PostgreSQL
engine = create_engine(DATABASE_URL)


# ===== LEITURA DO CSV =====
df = pd.read_csv(CSV_PATH)

print("📌 Primeiras linhas do CSV geral:")
print(df.head())


# ===== ENVIO PARA TABELA ÚNICA =====
df.to_sql("nome_da_tabela", engine, if_exists="replace", index=False)

print("\n🎯 Tabela única 'nome_da_tabela' criada com sucesso no PostgreSQL!")
print("Pronto para conectar no Power BI ✔️")

"""
Script para ler um arquivo CSV, identificar categorias e criar automaticamente
tabelas separadas no PostgreSQL — ideal para análises e conexão com Power BI.

Este script:
- Lê um arquivo CSV contendo dados;
- Exibe as primeiras linhas para conferência;
- Identifica todas as categorias únicas do dataset;
- Cria uma tabela separada no PostgreSQL para cada categoria;
- Substitui a tabela caso ela já exista.
"""

import pandas as pd
from sqlalchemy import create_engine
import os


# ===== CONFIGURAÇÕES =====
DATABASE_URL = "postgresql://postgres:senha@localhost:5432/NomeDaDatabase"

# Caminho genérico para GitHub (CSV dentro da pasta 'data/')
CSV_PATH = os.path.join("data", "nome_do_arquivo.csv")

# Criar conexão com o PostgreSQL
engine = create_engine(DATABASE_URL)


# ===== FUNÇÃO PARA LIMPAR NOMES DE TABELAS =====


def limpar_nome_categoria(nome: str) -> str:
    """Remove acentos, espaços e caracteres especiais para formar nomes válidos de tabela."""
    nome = nome.lower().strip()
    traducoes = {
        "ç": "c",
        "ã": "a",
        "á": "a",
        "â": "a",
        "à": "a",
        "é": "e",
        "ê": "e",
        "í": "i",
        "ó": "o",
        "ô": "o",
        "õ": "o",
        "ú": "u",
        " ": "_",
    }
    for acento, sem_acento in traducoes.items():
        nome = nome.replace(acento, sem_acento)
    return nome


# ===== LEITURA DO CSV =====
df = pd.read_csv(CSV_PATH)

print("📌 Primeiras linhas do CSV geral:")
print(df.head())


# ===== IDENTIFICAR CATEGORIAS =====
categorias = df["categoria"].unique()
print("\n📌 Categorias encontradas:", categorias)


# ===== CRIAR TABELAS SEPARADAS POR CATEGORIA =====
for categoria in categorias:
    nome_tabela = f"agro_{limpar_nome_categoria(categoria)}"
    df_filtrado = df[df["categoria"] == categoria]

    df_filtrado.to_sql(nome_tabela, engine, if_exists="replace", index=False)

    print(f"✅ Tabela '{nome_tabela}' criada com {len(df_filtrado)} linhas")


print("\n🎯 Todas as tabelas foram criadas com sucesso no PostgreSQL!")

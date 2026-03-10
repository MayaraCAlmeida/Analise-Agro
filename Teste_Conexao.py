"""
Script para testar a conexão com um banco de dados PostgreSQL usando SQLAlchemy.

Este script:
- Carrega variáveis de ambiente a partir de um arquivo .env;
- Cria uma engine de conexão com o PostgreSQL;
- Executa um SELECT simples para confirmar se a conexão está funcionando;
- Exibe a versão do PostgreSQL em uso.

Requisitos:
- python-dotenv
- SQLAlchemy
- psycopg2-binary
"""

from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Lê credenciais do PostgreSQL definidas no .env
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST", "localhost")
port = os.getenv("POSTGRES_PORT", "5432")
database = os.getenv("POSTGRES_DB")

# Criação da engine
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)

# Teste da conexão
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("✅ Conexão bem-sucedida!")
        print("Versão do PostgreSQL:", result.fetchone()[0])
except Exception as e:
    print("❌ Erro ao conectar ao PostgreSQL:")
    print(e)

# Dados Agropecuários → PostgreSQL → Power BI

Pipeline pra consolidar CSVs de dados agropecuários, subir pro PostgreSQL e conectar no Power BI.

## Estrutura
```
.
├── data/
│   ├── csvs/          # CSVs originais por categoria
│   └── geral.csv      # gerado pelo Unificar_CSVs.py
├── scripts/
│   ├── Unificar_CSVs.py
│   ├── Teste_Conexao.py
│   ├── Debug.py
│   ├── Import_PostgreSQL.py
│   ├── Criar_PublicTable.py
│   └── Criar_TabelaUnica.py
├── POSTGRESQL.sql
├── .env
├── .gitignore
└── README.md
```

## Dependências
```bash
pip install pandas sqlalchemy psycopg2-binary python-dotenv
```

Python 3.8+ e PostgreSQL 12+.

## Configuração

Crie um `.env` na raiz:
```env
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=nome_do_banco
```

Depois rode os comandos do `POSTGRESQL.sql` pra criar as tabelas.

## Ordem de execução

**1. Unificar os CSVs**
```bash
python Unificar_CSVs.py
```
Lê tudo em `data/csvs/`, extrai a categoria do nome do arquivo e gera o `data/geral.csv`.

**2. Testar conexão**
```bash
python Teste_Conexao.py
```
Confirma que o banco tá acessível e as credenciais do `.env` estão certas.

**3. Debug (opcional)**
```bash
python Debug.py
```
Inspeciona um intervalo de linhas do CSV. Útil pra conferir os dados antes de subir.

**4. Importar pro PostgreSQL**
```bash
python Import_PostgreSQL.py
```
Cria uma tabela separada por categoria: `agro_bovinos`, `agro_suinos`, etc.

**5. Criar tabela única**
```bash
python Criar_TabelaUnica.py
```
Gera a tabela `agro_dados` com tudo consolidado, índices e NOT NULL — pronta pro Power BI.

## Conectar no Power BI

Obter Dados → Banco de Dados PostgreSQL → conecta com as credenciais do `.env` → importa `agro_dados`.

## Estrutura dos dados

CSV original:
```csv
periodo,valor
2020,1500000
```

Após unificação:
```csv
periodo,categoria,valor
2020,bovinos,1500000
```

## Queries úteis
```sql
SELECT COUNT(*) FROM public.agro_dados;

SELECT * FROM public.agro_dados LIMIT 10;

SELECT categoria, SUM(valor) as total, AVG(valor) as media
FROM public.agro_dados
GROUP BY categoria;
```

## Atualizar dados

1. Joga os novos CSVs em `data/csvs/`
2. Roda `Unificar_CSVs.py`
3. Roda `Criar_TabelaUnica.py`
4. Atualiza no Power BI

## Erros comuns

- **Conexão recusada** — verifica se o PostgreSQL tá rodando e as credenciais no `.env`
- **CSV não encontrado** — confirma o caminho e se a pasta `data/csvs/` existe
- **Erro no Power BI** — testa a query direto no PostgreSQL primeiro

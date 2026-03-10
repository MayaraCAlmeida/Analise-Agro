# Projeto de Análise de Dados Agropecuários

Sistema automatizado para processamento de dados agropecuários, integração com PostgreSQL e visualização em Power BI.

## Descrição

Este projeto unifica múltiplos arquivos CSV de dados agropecuários, processa as informações e as organiza em um banco de dados PostgreSQL, facilitando análises e a criação de dashboards no Power BI.

## Estrutura do Projeto

```
.
├── data/
│   ├── csvs/              # Arquivos CSV originais por categoria
│   └── geral.csv          # CSV unificado (gerado)
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

## Pré-requisitos

- Python 3.8+
- PostgreSQL 12+
- Power BI Desktop (para visualização)

### Dependências Python

```bash
pip install pandas sqlalchemy psycopg2-binary python-dotenv
```

## Configuração

### 1. Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=nome_do_banco
```

### 2. Banco de Dados

Execute os comandos SQL do arquivo `POSTGRESQL.sql` para criar as estruturas necessárias no PostgreSQL.

## Fluxo de Trabalho

### Etapa 1: Unificar CSVs

Consolida múltiplos arquivos CSV em um único arquivo geral.

```bash
python Unificar_CSVs.py
```

**Entrada:** Arquivos CSV na pasta `data/csvs/`  
**Saída:** `data/geral.csv`

O script:
- Lê todos os arquivos CSV da pasta especificada
- Extrai a categoria do nome do arquivo
- Padroniza as colunas para `periodo`, `valor` e `categoria`
- Gera um arquivo unificado

### Etapa 2: Testar Conexão

Verifica se a conexão com o PostgreSQL está funcionando corretamente.

```bash
python Teste_Conexao.py
```

Confirma:
- Conectividade com o banco de dados
- Versão do PostgreSQL instalada
- Credenciais do arquivo `.env`

### Etapa 3: Debug (Opcional)

Inspeciona intervalos específicos do CSV para validação dos dados.

```bash
python Debug.py
```

Útil para:
- Conferir formato dos dados
- Identificar inconsistências
- Validar transformações antes do import

### Etapa 4: Importar para PostgreSQL

Cria tabelas separadas para cada categoria no banco de dados.

```bash
python Import_PostgreSQL.py
```

Gera tabelas no formato: `agro_bovinos`, `agro_suinos`, `agro_cafe`, etc.

### Etapa 5: Criar Tabelas Públicas

Alternativa ao script anterior, permite especificar o caminho do CSV manualmente.

```bash
python Criar_PublicTable.py
```

### Etapa 6: Criar Tabela Única

Cria uma tabela consolidada otimizada para conexão com Power BI.

```bash
python Criar_TabelaUnica.py
```

**Resultado:** Tabela `agro_dados` com todos os registros unificados, incluindo:
- Índices otimizados para consultas
- Constraints NOT NULL
- Estrutura pronta para dashboards

### Etapa 7: Dashboard no Power BI

1. Abra o Power BI Desktop
2. Selecione "Obter Dados" > "Banco de Dados PostgreSQL"
3. Configure a conexão usando as credenciais do `.env`
4. Importe a tabela `agro_dados`
5. Crie as visualizações desejadas

## Estrutura dos Dados

### CSV Original

```csv
periodo,valor
2020,1500000
2021,1750000
```

### Tabela Unificada

```csv
periodo,categoria,valor
2020,bovinos,1500000
2021,bovinos,1750000
2020,suinos,980000
```

### Banco de Dados PostgreSQL

**Opção 1: Tabelas Separadas**
- `agro_bovinos`
- `agro_suinos`
- `agro_ovos`
- `agro_leite`
- `agro_cafe`
- `agro_galinaceos`

**Opção 2: Tabela Única** (recomendado para Power BI)
- `agro_dados`

## Consultas Úteis

```sql
-- Total de registros
SELECT COUNT(*) FROM public.agro_dados;

-- Visualizar amostra
SELECT * FROM public.agro_dados LIMIT 10;

-- Dados formatados para relatório
SELECT
    periodo AS "Ano de Faturamento",
    categoria AS "Alimento Agropecuário",
    valor AS "Valor em Reais"
FROM public.agro_dados;

-- Agregação por categoria
SELECT 
    categoria,
    SUM(valor) as total,
    AVG(valor) as media
FROM public.agro_dados
GROUP BY categoria;
```

## Manutenção

### Atualizar Dados

Para adicionar novos dados:

1. Adicione novos CSVs em `data/csvs/`
2. Execute `Unificar_CSVs.py`
3. Execute `Criar_TabelaUnica.py` (modo replace)
4. Atualize o dashboard no Power BI

### Limpar Banco de Dados

```sql
DROP TABLE IF EXISTS
    public.agro_bovinos,
    public.agro_suinos,
    public.agro_ovos,
    public.agro_leite,
    public.agro_galinaceos,
    public.agro_cafe,
    public.agro_dados;
```

## Tratamento de Erros Comuns

**Erro de Conexão PostgreSQL:**
- Verifique se o serviço PostgreSQL está ativo
- Confirme as credenciais no arquivo `.env`
- Teste a conexão com `Teste_Conexao.py`

**CSV não encontrado:**
- Verifique os caminhos nos scripts
- Certifique-se de que a pasta `data/csvs/` existe
- Confirme a estrutura das colunas nos CSVs

**Erro no Power BI:**
- Verifique se os índices foram criados
- Confirme as constraints NOT NULL
- Teste as queries SQL diretamente no PostgreSQL

## Licença

Este projeto está sob a licença MIT.

## Contato

Para dúvidas ou sugestões, abra uma issue no repositório.
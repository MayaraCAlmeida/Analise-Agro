--- CRIAR TABELAS SEPARADAS POR CATEGORIA ---

CREATE TABLE public.agro_bovinos (
    ano INT,
    categoria TEXT,
    valor NUMERIC(10,2)
);

CREATE TABLE public.agro_suinos (
    ano INT,
    categoria TEXT,
    valor NUMERIC(10,2)
);

CREATE TABLE public.agro_ovos (
    ano INT,
    categoria TEXT,
    valor BIGINT
);

CREATE TABLE public.agro_leite (
    ano INT,
    categoria TEXT,
    valor BIGINT
);

CREATE TABLE public.agro_cafe (
    ano INT,
    categoria TEXT,
    valor BIGINT
);

CREATE TABLE public.agro_galinaceos (
    ano INT,
    categoria TEXT,
    valor BIGINT
);

--- EXPLORAR QUERIES ---

SELECT * FROM agro LIMIT 20;
SELECT COUNT(*) FROM public.agro_bovinos;
-- e assim por diante mudando o nome da tabela e o limite


--- APAGAR TABELAS ---

DROP TABLE IF EXISTS
    public.agro_bovinos,
    public.agro_suinos,
    public.agro_ovos,
    public.agro_leite,
    public.agro_galinaceos,
    public.agro_cafe;

---- CRIAÇÃO DE TABELA ÚNICA PARA POWER BI ---
---- IMPORTANTE TER USADO O SCRIPT "Criar_TabelaUnica" ----
CREATE TABLE public.agro_dados(
    id SERIAL PRIMARY KEY,
    ano INT,
    categoria TEXT,
    valor NUMERIC(12,2)
);

---- VERIFICAÇÃO DE DADOS ---- 

--- TOTAL DE REGISTROS ---
SELECT COUNT(*) FROM public.agro_dados;

--- VISUALIZAR AMOSTRA ---

SELECT * FROM public.agro_dados LIMIT 5;

----- FORMATAÇÃO DA TABELA ----
SELECT
    periodo AS "Ano de Faturamento",
    categoria AS "Alimento Agropecuário",
    valor AS "Valor em Reais"
FROM public.agro_dados;

------ EVITAR ERROS NO POWER BI ----
ALTER TABLE public.agro_dados
    ALTER COLUMN periodo SET NOT NULL,
    ALTER COLUMN categoria SET NOT NULL,
    ALTER COLUMN valor SET NOT NULL;

---- OTIMIZAR CONSULTAS ----
CREATE INDEX idx_agro_periodo_categoria
ON public.agro_dados (periodo, categoria);


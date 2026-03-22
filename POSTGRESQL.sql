-- tabelas por categoria
CREATE TABLE public.agro_bovinos   (ano INT, categoria TEXT, valor NUMERIC(10,2));
CREATE TABLE public.agro_suinos    (ano INT, categoria TEXT, valor NUMERIC(10,2));
CREATE TABLE public.agro_ovos      (ano INT, categoria TEXT, valor BIGINT);
CREATE TABLE public.agro_leite     (ano INT, categoria TEXT, valor BIGINT);
CREATE TABLE public.agro_cafe      (ano INT, categoria TEXT, valor BIGINT);
CREATE TABLE public.agro_galinaceos(ano INT, categoria TEXT, valor BIGINT);

-- explorar
SELECT * FROM agro LIMIT 20;
SELECT COUNT(*) FROM public.agro_bovinos;

-- apagar
DROP TABLE IF EXISTS
    public.agro_bovinos, public.agro_suinos, public.agro_ovos,
    public.agro_leite, public.agro_galinaceos, public.agro_cafe;

-- tabela única (rodar depois do script Criar_TabelaUnica)
CREATE TABLE public.agro_dados (
    id       SERIAL PRIMARY KEY,
    ano      INT,
    categoria TEXT,
    valor    NUMERIC(12,2)
);

-- verificação
SELECT COUNT(*) FROM public.agro_dados;
SELECT * FROM public.agro_dados LIMIT 5;

-- formatação pro Power BI
SELECT
    periodo   AS "Ano de Faturamento",
    categoria AS "Alimento Agropecuário",
    valor     AS "Valor em Reais"
FROM public.agro_dados;

-- garantir NOT NULL
ALTER TABLE public.agro_dados
    ALTER COLUMN periodo   SET NOT NULL,
    ALTER COLUMN categoria SET NOT NULL,
    ALTER COLUMN valor     SET NOT NULL;

-- índice pra performance
CREATE INDEX idx_agro_periodo_categoria ON public.agro_dados (periodo, categoria);

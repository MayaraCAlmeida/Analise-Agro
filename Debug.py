"""
Trecho utilizado para debug/conferência dos dados do CSV.

Objetivo:
- Ler o arquivo CSV;
- Visualizar apenas um intervalo específico de linhas;
- Checar se os dados estão corretos antes de enviar para o banco de dados.

Observação:
O índice do pandas começa em 0, portanto df.iloc[10:16]
retorna as linhas 10 até 15.
"""

import pandas as pd

# Caminho do arquivo CSV
CSV_PATH = r"caminho/do/arquivo.csv"

# Ler CSV completo
df = pd.read_csv(CSV_PATH)

# Selecionar um intervalo de linhas para inspeção
intervalo = df.iloc[10:16]

# Exibir o intervalo selecionado
print(intervalo)

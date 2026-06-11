import time
import numpy as np

# matriz grande para evidenciar efeito de cache miss
LINHAS = 4000
COLUNAS = 4000

mat = np.random.rand(LINHAS, COLUNAS)

# loop A: acesso sequencial (linha por linha)
inicio = time.perf_counter()
for i in range(LINHAS):
    _ = mat[i, :].sum()
tempo_linhas = time.perf_counter() - inicio

# loop B: acesso com saltos (coluna por coluna)
inicio = time.perf_counter()
for j in range(COLUNAS):
    _ = mat[:, j].sum()
tempo_colunas = time.perf_counter() - inicio

razao = tempo_colunas / tempo_linhas

print(f"acesso por linhas (sequencial): {tempo_linhas:.4f} s")
print(f"acesso por colunas (saltos):    {tempo_colunas:.4f} s")
print(f"razao colunas/linhas:           {razao:.2f}x")

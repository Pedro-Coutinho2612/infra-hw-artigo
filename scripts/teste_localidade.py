import time
import numpy as np

# matriz grande percorrida elemento a elemento com loops python
LINHAS = 4000
COLUNAS = 4000

mat = np.random.rand(LINHAS, COLUNAS)

# loop A: acesso sequencial (linha por linha)
inicio = time.perf_counter()
soma = 0.0
for i in range(LINHAS):
    for j in range(COLUNAS):
        soma += mat[i, j]
tempo_linhas = time.perf_counter() - inicio

# loop B: acesso com saltos (coluna por coluna)
inicio = time.perf_counter()
soma = 0.0
for j in range(COLUNAS):
    for i in range(LINHAS):
        soma += mat[i, j]
tempo_colunas = time.perf_counter() - inicio

razao = tempo_colunas / tempo_linhas

print(f"acesso por linhas (sequencial): {tempo_linhas:.2f} s")
print(f"acesso por colunas (saltos):    {tempo_colunas:.2f} s")
print(f"razao colunas/linhas:           {razao:.2f}x")

import time, numpy as np, scipy.stats as stats
LINHAS, COLUNAS, REPETICOES, WARMUP = 4000, 4000, 35, 5
t_lin, t_col = [], []
for r in range(REPETICOES):
    mat = np.random.rand(LINHAS, COLUNAS)
    t0 = time.perf_counter()
    for i in range(LINHAS): 
        for j in range(COLUNAS): mat[i, j]
    tl = time.perf_counter() - t0
    t0 = time.perf_counter()
    for j in range(COLUNAS):
        for i in range(LINHAS): mat[i, j]
    tc = time.perf_counter() - t0
    if r >= WARMUP: t_lin.append(tl); t_col.append(tc)
ic_A = stats.t.interval(0.95, len(t_lin)-1, loc=np.mean(t_lin), scale=stats.sem(t_lin))
ic_B = stats.t.interval(0.95, len(t_col)-1, loc=np.mean(t_col), scale=stats.sem(t_col))
print(f"Linhas IC 95%: {ic_A} | Colunas IC 95%: {ic_B}")
t, p = stats.ttest_ind(t_lin, t_col); print(f"p-valor: {p:.4e}")

import time, os, tempfile, numpy as np, scipy.stats as stats
REPETICOES, WARMUP = 35, 5
mops_l, gbs_l, mbs_l = [], [], []
for r in range(REPETICOES):
    v = np.random.rand(250_000).astype(np.float32)
    t0 = time.perf_counter()
    for _ in range(2000): v * 1.0001 + 0.5
    mops = (len(v) * 2 * 2000) / (time.perf_counter() - t0) / 1e6
    tam = 256 * 1024 * 1024; a = np.ones(tam // 8); b = np.empty_like(a)
    t0 = time.perf_counter()
    np.copyto(b, a)
    gb_s = (tam * 2) / (time.perf_counter() - t0) / 1e9
    if r >= WARMUP: mops_l.append(mops); gbs_l.append(gb_s)
def rep(nome, dados):
    ic = stats.t.interval(0.95, len(dados)-1, loc=np.mean(dados), scale=stats.sem(dados))
    print(f"{nome}: Média: {np.mean(dados):.2f} | IC 95%: {ic}")
rep("CPU", mops_l); rep("MEM", gbs_l)

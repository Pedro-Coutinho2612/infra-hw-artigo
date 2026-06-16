import os, time, multiprocessing, numpy as np, scipy.stats as stats
os.environ.update({"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"})
TAREFAS, REPETICOES, WARMUP = 12, 35, 5
def tarefa(_):
    m = np.random.rand(1250, 1000)
    for _ in range(20): (m * 1.0001 + 0.5).sum()
def medir_tempo(n):
    inicio = time.perf_counter()
    with multiprocessing.Pool(n) as p: p.map(tarefa, range(TAREFAS))
    return time.perf_counter() - inicio
if __name__ == "__main__":
    configs = [1, 2, 4, multiprocessing.cpu_count()]
    res = {c: [] for c in configs}
    for n in configs:
        for i in range(REPETICOES):
            t = medir_tempo(n)
            if i >= WARMUP: res[n].append(t)
    for n in configs:
        ic = stats.t.interval(0.95, len(res[n])-1, loc=np.mean(res[n]), scale=stats.sem(res[n]))
        print(f"Threads: {n} | Média: {np.mean(res[n]):.4f}s | SD: {np.std(res[n], ddof=1):.4f} | IC 95%: {ic}")
    t, p = stats.ttest_ind(res[4], res[12]); print(f"p-valor (4 vs 12): {p:.4e}")

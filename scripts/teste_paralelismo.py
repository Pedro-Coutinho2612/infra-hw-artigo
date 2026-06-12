import os
# limita o numpy a 1 thread por processo, senao o BLAS paraleliza sozinho
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import time
import multiprocessing
import numpy as np

TAREFAS = 12  # trabalho total fixo, dividido entre os processos

def tarefa(_):
    # aloca ~10 MB e faz operacoes elemento a elemento sobre a matriz
    m = np.random.rand(1250, 1000)
    s = 0.0
    for _ in range(20):
        s += (m * 1.0001 + 0.5).sum()
    return s

def medir_tempo(num_processos):
    inicio = time.perf_counter()
    with multiprocessing.Pool(num_processos) as pool:
        pool.map(tarefa, range(TAREFAS))
    return time.perf_counter() - inicio

if __name__ == "__main__":
    max_proc = multiprocessing.cpu_count()
    configs = sorted(set([1, 2, 4, max_proc]))

    tempo_base = medir_tempo(1)

    print(f"{'processos':>10}  {'tempo (s)':>10}  {'speedup':>8}  {'eficiencia':>10}")
    print("-" * 45)
    print(f"{1:>10}  {tempo_base:>10.3f}  {'1.000':>8}  {'100.0%':>10}")

    for n in configs[1:]:
        t = medir_tempo(n)
        speedup = tempo_base / t
        eficiencia = speedup / n * 100
        print(f"{n:>10}  {t:>10.3f}  {speedup:>8.3f}  {eficiencia:>9.1f}%")

import time
import multiprocessing
import numpy as np

def tarefa(n):
    # aloca ~10 MB e faz operações sobre a matriz
    m = np.random.rand(1250, 1000)  # ~10 MB (float64)
    for _ in range(n):
        resultado = np.dot(m, m.T)
    return resultado.sum()

def medir_tempo(num_processos, repeticoes=4):
    inicio = time.perf_counter()
    with multiprocessing.Pool(num_processos) as pool:
        pool.map(tarefa, [repeticoes] * num_processos)
    return time.perf_counter() - inicio

if __name__ == "__main__":
    max_proc = multiprocessing.cpu_count()
    configs = sorted(set([1, 2, 4, max_proc]))

    # mede tempo com 1 processo como referência para speedup
    tempo_base = medir_tempo(1)

    print(f"{'processos':>10}  {'tempo (s)':>10}  {'speedup':>8}  {'eficiência':>10}")
    print("-" * 45)
    print(f"{'1':>10}  {tempo_base:>10.3f}  {'1.000':>8}  {'100.0%':>10}")

    for n in configs[1:]:
        t = medir_tempo(n)
        speedup = tempo_base / t
        eficiencia = speedup / n * 100
        print(f"{n:>10}  {t:>10.3f}  {speedup:>8.3f}  {eficiencia:>9.1f}%")

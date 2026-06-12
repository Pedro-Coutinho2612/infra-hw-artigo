import time
import os
import tempfile
import numpy as np
import psutil

# --- fase cpu-bound: array pequeno que cabe na cache, muitas passadas ---
v = np.random.rand(250_000).astype(np.float32)  # ~1 MB, cabe na L2
PASSADAS = 2000
inicio = time.perf_counter()
for _ in range(PASSADAS):
    r = v * np.float32(1.0001) + np.float32(0.5)
tempo_cpu = time.perf_counter() - inicio
mops = (len(v) * 2 * PASSADAS) / tempo_cpu / 1e6
print(f"[cpu]  {tempo_cpu:.3f} s  ->  {mops:.1f} Mop/s")

# --- fase memory-bound: copia de array grande ---
tamanho = 256 * 1024 * 1024
a = np.ones(tamanho // 8, dtype=np.float64)
b = np.empty_like(a)

inicio = time.perf_counter()
np.copyto(b, a)
tempo_mem = time.perf_counter() - inicio
gb_s = (tamanho * 2) / tempo_mem / 1e9
print(f"[mem]  {tempo_mem:.3f} s  ->  {gb_s:.2f} GB/s")

# uso de cpu logo apos a fase de memoria
uso = psutil.cpu_percent(interval=0.5, percpu=True)
ocupados = sum(1 for u in uso if u > 50)
print(f"nucleos acima de 50% apos fase de memoria: {ocupados}")

# --- fase i/o-bound: escrita e leitura em disco ---
tamanho_io = 128 * 1024 * 1024
dados = os.urandom(tamanho_io)

fd, caminho = tempfile.mkstemp(suffix=".bin")
os.close(fd)

inicio = time.perf_counter()
with open(caminho, "wb") as f:
    f.write(dados)
    f.flush()
    os.fsync(f.fileno())
with open(caminho, "rb") as f:
    f.read()
tempo_io = time.perf_counter() - inicio
os.remove(caminho)

mb_s = (tamanho_io * 2) / tempo_io / 1e6
print(f"[i/o]  {tempo_io:.3f} s  ->  {mb_s:.1f} MB/s")

# a banda de memoria fica no teto da ddr4 enquanto a cpu nao satura
# durante a copia: comportamento de sistema memory-bound
print(f"\nbanda de memoria medida: {gb_s:.2f} GB/s")

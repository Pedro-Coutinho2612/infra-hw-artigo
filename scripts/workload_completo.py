import time
import os
import tempfile
import numpy as np
import psutil

# --- fase CPU-bound ---
N = 10_000_000
inicio = time.perf_counter()
acc = 0.0
for i in range(N):
    acc += i * 1.0001
tempo_cpu = time.perf_counter() - inicio
mops = N / tempo_cpu / 1e6
print(f"[cpu]    {tempo_cpu:.3f} s  ->  {mops:.1f} Mop/s")

# --- fase memory-bound ---
tamanho = 256 * 1024 * 1024  # 256 MB
a = np.ones(tamanho // 8, dtype=np.float64)
b = np.empty_like(a)

inicio = time.perf_counter()
np.copyto(b, a)
tempo_mem = time.perf_counter() - inicio
gb_s = (tamanho * 2) / tempo_mem / 1e9  # leitura + escrita
print(f"[mem]    {tempo_mem:.3f} s  ->  {gb_s:.2f} GB/s")

# --- fase I/O-bound ---
tamanho_io = 128 * 1024 * 1024  # 128 MB
dados = os.urandom(tamanho_io)

fd, caminho = tempfile.mkstemp(suffix=".bin")
os.close(fd)

inicio = time.perf_counter()
with open(caminho, "wb") as f:
    f.write(dados)
with open(caminho, "rb") as f:
    f.read()
tempo_io = time.perf_counter() - inicio
os.remove(caminho)

mb_s = (tamanho_io * 2) / tempo_io / 1e6
print(f"[i/o]    {tempo_io:.3f} s  ->  {mb_s:.1f} MB/s")

# --- uso por núcleo ---
print("\nuso por nucleo (%):")
uso = psutil.cpu_percent(interval=1, percpu=True)
for i, u in enumerate(uso):
    print(f"  nucleo {i}: {u}%")

# identifica gargalo comparando tempos normalizados
tempos = {"cpu": tempo_cpu, "memoria": tempo_mem, "i/o": tempo_io}
gargalo = max(tempos, key=tempos.get)
print(f"\ngargalo detectado: {gargalo} ({tempos[gargalo]:.3f} s)")

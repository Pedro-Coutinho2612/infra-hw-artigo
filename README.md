# infra-hw-artigo

Artigo cientifico - Analise experimental da hierarquia de memoria em processador hibrido Intel i5-13420H (Infraestrutura de Hardware, CESAR School)

## Ambiente

- CPU: Intel Core i5-13420H (4P + 4E cores, 12 threads)
- RAM: 7,6 GiB DDR4
- Armazenamento: SSD NVMe SK Hynix
- SO: Ubuntu 24.04.3 LTS via WSL2 (kernel 6.6.87)
- Python 3 + numpy + psutil

## Estrutura

    infra-hw-artigo/
    ├── artigo/          # PDF final e fontes LaTeX
    ├── dados/           # medicoes originais do laboratorio
    ├── dados/           # medicoes originais do laboratorio
    └── scripts/         # scripts Python dos experimentos

## Scripts

| arquivo | o que faz |
|---|---|
| scripts/teste_paralelismo.py | varia numero de processos (1, 2, 4, max) e mede speedup e eficiencia |
| scripts/teste_localidade.py | compara acesso por linhas vs colunas numa matriz numpy para mostrar efeito de cache |
| scripts/workload_completo.py | tres fases (CPU-bound, memory-bound, I/O-bound) com monitoramento por nucleo via psutil |

## Como rodar

    pip install numpy psutil
    python3 scripts/teste_paralelismo.py
    python3 scripts/teste_localidade.py
    python3 scripts/workload_completo.py

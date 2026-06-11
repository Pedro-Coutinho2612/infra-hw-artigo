# infra-hw-artigo

Artigo científico – Análise experimental da hierarquia de memória em processador híbrido Intel i5-13420H (Infraestrutura de Hardware, CESAR School)

## Ambiente

- CPU: Intel Core i5-13420H (4P + 4E cores)
- SO: Ubuntu 24.04 via WSL2
- Python 3.12 + numpy + psutil

## Estrutura

```
infra-hw-artigo/
├── artigo/          # PDF final e fontes LaTeX (main.tex, referencias.bib)
├── scripts/         # scripts Python dos experimentos
├── dados/           # saídas brutas das medições (txt, png)
└── evidencias/      # screenshots dos benchmarks
```

## Scripts

| arquivo | descrição |
|---|---|
| `scripts/teste_localidade.py` | compara acesso por linhas vs. colunas numa matriz numpy para evidenciar localidade de cache |
| `scripts/teste_paralelismo.py` | varia número de processos (1, 2, 4, max) e mede speedup e eficiência |
| `scripts/workload_completo.py` | três fases (CPU-bound, memory-bound, I/O-bound) com monitoramento por núcleo via psutil |

## Como rodar

```bash
pip install numpy psutil
python scripts/teste_localidade.py
python scripts/teste_paralelismo.py
python scripts/workload_completo.py
```

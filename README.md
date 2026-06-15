# Relatório Técnico Expandido (Trilha B) - ABNT NBR 10719

Análise experimental estatística da hierarquia de memória, subsistemas de I/O e paralelismo em processador híbrido Intel Core i5-13420H rodando Ubuntu 24.04 LTS via WSL2. Trabalho de laboratório desenvolvido para a disciplina de Infraestrutura de Hardware (CESAR School).

## Ambiente de Execução

- **CPU**: Intel Core i5-13420H (4 P-cores + 4 E-cores, 12 threads lógicas)
- **RAM**: 7,6 GiB DDR4
- **Armazenamento**: SSD NVMe SK Hynix
- **SO**: Ubuntu 24.04.3 LTS via WSL2 (Kernel Linux 6.6.87-microsoft-standard-WSL2)
- **Python**: Python 3 com as bibliotecas `numpy`, `scipy` e `psutil`

## Estrutura do Repositório

    infra-hw-artigo/
    ├── relatorio/       # Fontes LaTeX do Relatório Técnico (abntex2) e PDF final
    ├── dados/           # Saídas e medições dos experimentos (logs brutos)
    └── scripts/         # Scripts Python implementados com rigor estatístico

## Scripts de Teste

| Arquivo | Descrição | Rigor Estatístico |
|---|---|---|
| [teste_paralelismo.py](file:///c:/Users/Coutinho/OneDrive/Área de Trabalho/trilha_b/infra-hw-artigo/scripts/teste_paralelismo.py) | Varia o número de processos (1, 2, 4, 12) e calcula speedup e eficiência. | 35 execuções (5 warm-up descartadas + 30 válidas). Média, SD, IC 95%, Teste t de Student (4 vs 12 threads). |
| [teste_localidade.py](file:///c:/Users/Coutinho/OneDrive/Área de Trabalho/trilha_b/infra-hw-artigo/scripts/teste_localidade.py) | Compara o tempo de acesso por Linhas (sequencial) vs Colunas (não-sequencial) em matriz $4000 \times 4000$. | 35 execuções (5 warm-up descartadas + 30 válidas). Média, SD, IC 95%, Teste t de Student (Linhas vs Colunas). |
| [workload_completo.py](file:///c:/Users/Coutinho/OneDrive/Área de Trabalho/trilha_b/infra-hw-artigo/scripts/workload_completo.py) | Roda carga sintética mista dividida em três fases: CPU-Bound, Memory-Bound e I/O-Bound. | 35 execuções (5 warm-up descartadas + 30 válidas). Média, SD, IC 95% para cada fase. |

## Como Executar os Testes

1. Garanta as dependências necessárias instaladas:
   ```bash
   pip install numpy scipy
   # No Ubuntu (WSL2), se necessário:
   # sudo apt update && sudo apt install python3-scipy python3-numpy -y
   ```
2. Execute os scripts:
   ```bash
   python3 scripts/teste_paralelismo.py
   python3 scripts/teste_localidade.py
   python3 scripts/workload_completo.py
   ```

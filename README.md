<p align="center"> <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/c913687b-f3a6-4381-bb31-a1bcf7eb9548"  /> </p>


# 🎗️ Breast Cancer Diagnostic EDA & Data Storytelling

Uma análise exploratória de dados (EDA) focada na distribuição
e comportamento estatístico de medições obtidas via
**Aspirado por Agulha Fina (PAAF)** de massas mamárias. 

O objetivo principal deste projeto é traduzir dados biomédicos
em **insights clínicos acionáveis (Data Storytelling)**,
preparando a base para futuros modelos de Inteligência Artificial e auxiliando na tomada de decisão de equipes médicas e de gestão hospitalar.


## Contexto do projeto

Este exercício de preparação de dados faz parte da formação [MCIO + Leega](https://www.linkedin.com/company/mciobrasil/posts/)
para Engenharia de Dados realizada entre 06 de julho de 2026 a 06 de novembro de 2026. A formação inclui:

1. Fundamentos de dados (12 horas)
2. Preparação de dados (20 horas)
3. Engenharia e Arquitetura de dados (20 horas)
4. Visualização e storytelling de dados (20 horas)


---

## Objetivos do Projeto

- **Análise Qualitativa e Quantitativa:** Avaliar a proporção entre casos benignos e malignos no dataset.
- **Identificação de Padrões Anatômicos:** Analisar distribuições e assimetrias de variáveis como raio, área, textura e concavidade.
- **Detecção de Casos Atípicos (Outliers):** Compreender o impacto de tumores agressivos ou em estágios avançados no treino de algoritmos.
- **Redução de Multicolinearidade:** Mapear correlações entre variáveis anatômicas para otimização de futuros modelos de Machine Learning.
- **Automação de Relatórios:** Gerar dashboards automáticos com estatísticas descritivas completas para a equipe médica.

---

## Tecnologias e Bibliotecas Utilizadas

- **Python 3.x**
- **Pandas:** Manipulação, limpeza e estruturação dos dados.
- **NumPy:** Cálculos estatísticos e operações matriciais.
- **Matplotlib & Seaborn:** Criação de visualizações e gráficos informativos.
- **Sweetviz / Ydata-Profiling:** Geração de relatórios interativos automatizados em HTML.

---

## Principais Perguntas & Insights Clínicos

### 1. Proporção dos Diagnósticos (Benigno vs. Maligno)
- **Foco:** Identificação de desbalanceamento de classes.
- **Insight:** Identificar o percentual de casos benignos e malignos é essencial para definir métricas de avaliação de IA (como *Recall* / *Sensibilidade*), garantindo que falsos negativos em exames malignos sejam minimizados.

### 2. Distribuição das Variáveis Numéricas
- **Foco:** Simetria das curvas e médias por diagnóstico.
- **Insight:** Tumores malignos apresentam valores médios significativamente maiores em atributos como `radius_mean` e `area_mean`. Variáveis de área tendem a apresentar assimetria positiva (cauda longa à direita).

### 3. Análise de Outliers (Valores Discrepantes)
- **Foco:** Avaliação via Boxplots ($IQR$).
- **Insight:** No contexto médico, *outliers* nem sempre são erros de medição; frequentemente representam casos graves ou avançados. A retenção desses pontos no treino do modelo garante capacidade de generalização para casos críticos.

### 4. Matriz de Correlação
- **Foco:** Multicolinearidade entre variáveis físicas.
- **Insight:** Variáveis como `radius_mean`, `perimeter_mean` e `area_mean` possuem forte correlação positiva ($\ge 0.95$). A remoção de atributos redundantes simplifica o modelo sem perda relevante de informação.

---

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/breast-cancer-eda-storytelling.git](https://github.com/SEU-USUARIO/breast-cancer-eda-storytelling.git)
   cd breast-cancer-eda-storytelling

2. **Instale as dependências:**

```python
pip install pandas numpy matplotlib seaborn sweetviz
```

3. **Execute o Jupyter Notebook ou Script Python:**

```
python main.py
```

Estrutura do Repositório

```text
├── data/
│   └── dados_cancer.csv         # Dataset de exames clínicos
├── notebooks/
│   └── analise_cancer.ipynb     # Notebook com a análise explicada
├── reports/
│   └── Analise_Exploratoria.html# Relatório HTML interativo gerado
├── main.py                      # Script de execução principal
├── README.md                    # Documentação do projeto
└── requirements.txt             # Dependências do projeto
```

## Certificados

## 📜 Certificados

| 01 - Fundamentos de Dados | 02 - Preparação de Dados |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/bb205a10-f5ad-40c8-bf23-c25679b6f348" width="400" alt="Fundamentos de dados"/> | <img src="https://github.com/user-attachments/assets/1dea7381-fbc8-46f5-9a6c-1a2168252c18" width="400" alt="Preparação de dados"/> |
| **03 - Engenharia e Arquitetura de Dados** | **04 - Visualização e Storytelling de Dados** |
| <img src="https://github.com/user-attachments/assets/0f39db7b-e989-4bca-b3c8-97ff8a95d845" width="400" alt="Engenharia e Arquitetura de dados"/> | <img src="https://github.com/user-attachments/assets/552c0abc-f112-448c-995d-0671432798f6" width="400" alt="Visualização e Storytelling de dados"/> |
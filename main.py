import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Configurações visuais do Seaborn
sns.set_theme(style="whitegrid")

# -------------------------------------------------------------
# 1. CARREGAR OS DADOS
# -------------------------------------------------------------
# Tenta carregar do caminho 'data/dados_cancer.csv' ou da raiz 'dados_cancer.csv'
file_path = "data/dados_cancer.csv"
if not os.path.exists(file_path) and os.path.exists("dados_cancer.csv"):
  file_path = "dados_cancer.csv"

try:
  df = pd.read_csv(file_path)
  print(f"Dataset carregado com sucesso a partir de '{file_path}'!")
except FileNotFoundError:
  print(
      "Aviso: 'dados_cancer.csv' não foi encontrado. Adicione o ficheiro na"
      " pasta 'data/' ou na raiz."
  )
  df = pd.DataFrame()

if not df.empty:
  # Exibir primeiras linhas e informações gerais
  print("\n--- Primeiras Linhas ---")
  print(df.head())

  print("\n--- Informações da Matriz de Dados ---")
  print(df.info())

  # Limpeza preliminar: remoção de 'id' se existir e duplicados
  if "id" in df.columns:
    df.drop(columns=["id"], inplace=True)

  df.drop_duplicates(inplace=True)

  # -------------------------------------------------------------
  # 1. VARIÁVEL CATEGÓRICA: DIAGNOSIS (GRÁFICO DE BARRAS)
  # -------------------------------------------------------------
  if "diagnosis" in df.columns:
    plt.figure(figsize=(8, 5))
    ax = sns.countplot(data=df, x="diagnosis", palette="Set2")
    plt.title("Distribuição dos Diagnósticos (Benigno vs. Maligno)", fontsize=14)
    plt.xlabel("Diagnóstico")
    plt.ylabel("Quantidade de Amostras")

    total = len(df)
    for p in ax.patches:
      percentage = f"{100 * p.get_height() / total:.1f}%"
      count = int(p.get_height())
      ax.annotate(
          f"{count} ({percentage})",
          (p.get_x() + p.get_width() / 2.0, p.get_height()),
          ha="center",
          va="center",
          xytext=(0, 8),
          textcoords="offset points",
      )

    plt.tight_layout()
    plt.show()

  # -------------------------------------------------------------
  # 2. VARIÁVEIS NUMÉRICAS: HISTOGRAMA / DISTRIBUIÇÃO
  # -------------------------------------------------------------
  colunas_num = ["radius_mean", "area_mean"]
  cols_existentes = [c for c in colunas_num if c in df.columns]

  if cols_existentes:
    fig, axes = plt.subplots(
        1, len(cols_existentes), figsize=(7 * len(cols_existentes), 5)
    )
    if len(cols_existentes) == 1:
      axes = [axes]

    for i, col in enumerate(cols_existentes):
      sns.histplot(
          data=df,
          x=col,
          hue="diagnosis" if "diagnosis" in df.columns else None,
          kde=True,
          ax=axes[i],
          palette="Set1",
          element="step",
      )
      axes[i].set_title(f"Distribuição da Variável: {col}")

    plt.tight_layout()
    plt.show()

  # -------------------------------------------------------------
  # 3. IDENTIFICAÇÃO DE OUTLIERS: BOXPLOT
  # -------------------------------------------------------------
  if "radius_mean" in df.columns and "diagnosis" in df.columns:
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df, x="diagnosis", y="radius_mean", palette="Set2")
    plt.title("Identificação de Outliers: Raio Médio por Diagnóstico")
    plt.xlabel("Diagnóstico")
    plt.ylabel("Raio Médio")
    plt.tight_layout()
    plt.show()

  # -------------------------------------------------------------
  # 4. MATRIZ DE CORRELAÇÃO: HEATMAP
  # -------------------------------------------------------------
  plt.figure(figsize=(12, 8))
  df_numeric = df.select_dtypes(include=[np.number])
  if not df_numeric.empty:
    corr = df_numeric.corr()
    sns.heatmap(corr, annot=False, cmap="coolwarm", linewidths=0.5)
    plt.title("Matriz de Correlação entre as Variáveis Numéricas")
    plt.tight_layout()
    plt.show()

  # -------------------------------------------------------------
  # 5. GERAR DASHBOARD AUTOMATIZADO COM SWEETVIZ
  # -------------------------------------------------------------
  try:
    import sweetviz as sv

    os.makedirs("reports", exist_ok=True)
    report = sv.analyze(df)
    report.show_html("reports/Analise_Exploratoria_Cancer.html")
    print(
        "Relatório HTML 'reports/Analise_Exploratoria_Cancer.html' gerado com"
        " sucesso!"
    )
  except ImportError:
    print(
        "Aviso: 'sweetviz' não está instalado. Execute 'pip install sweetviz'"
        " para gerar o relatório em HTML."
    )
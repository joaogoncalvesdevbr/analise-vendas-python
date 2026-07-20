# ============================================================
# PROJETO DE PORTFÓLIO - ANÁLISE DE DADOS DE VENDAS
# PARTE 1 DE 5
# Autor: João Gonçalves
# ============================================================

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

import matplotlib
matplotlib.use("Agg")  # importante no Pydroid

import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Criando pasta para gráficos
# -----------------------------
os.makedirs("graficos", exist_ok=True)

# -----------------------------
# Semente para resultados iguais
# -----------------------------
random.seed(42)
np.random.seed(42)

# -----------------------------
# Listas de dados fictícios
# -----------------------------

clientes = [
    "João Silva","Maria Oliveira","Pedro Santos","Ana Costa","Lucas Ferreira",
    "Juliana Almeida","Carlos Souza","Fernanda Lima","Ricardo Gomes","Camila Rocha",
    "Bruno Martins","Patrícia Ribeiro","Eduardo Barbosa","Larissa Melo","Felipe Araújo",
    "Amanda Cardoso","Gustavo Nunes","Bianca Carvalho","Matheus Dias","Isabela Fernandes",
    "Diego Moreira","Mariana Alves","Renato Freitas","Vanessa Pinto","Rafael Moraes",
    "Paula Castro","Thiago Rezende","Aline Moura","Leonardo Vieira","Beatriz Campos",
    "Vinicius Tavares","Gabriela Lopes","Henrique Duarte","Natália Barros","Igor Mendes",
    "Débora Teixeira","Caio Peixoto","Luana Ribeiro","Murilo Farias","Sabrina Pires",
    "Arthur Monteiro","Cláudia Figueiredo","Daniel Aguiar","Letícia Ramos","Samuel Cunha",
    "Cristina Neves","Victor Braga","Elaine Duarte","Rogério Machado","Priscila Gomes"
]

produtos = {
    "Notebook": 4200,
    "Mouse Gamer": 180,
    "Teclado Mecânico": 350,
    "Monitor 24": 980,
    "SSD 1TB": 520,
    "HD Externo": 430,
    "Headset": 290,
    "Webcam": 240,
    "Cadeira Gamer": 1650,
    "Impressora": 870,
    "Tablet": 2100,
    "Smartphone": 3200
}

categorias = {
    "Notebook":"Informática",
    "Mouse Gamer":"Periféricos",
    "Teclado Mecânico":"Periféricos",
    "Monitor 24":"Monitores",
    "SSD 1TB":"Armazenamento",
    "HD Externo":"Armazenamento",
    "Headset":"Áudio",
    "Webcam":"Periféricos",
    "Cadeira Gamer":"Móveis",
    "Impressora":"Escritório",
    "Tablet":"Mobile",
    "Smartphone":"Mobile"
}

cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Curitiba",
    "Porto Alegre",
    "Salvador",
    "Recife",
    "Fortaleza",
    "Brasília",
    "Campinas"
]

estados = {
    "São Paulo":"SP",
    "Rio de Janeiro":"RJ",
    "Belo Horizonte":"MG",
    "Curitiba":"PR",
    "Porto Alegre":"RS",
    "Salvador":"BA",
    "Recife":"PE",
    "Fortaleza":"CE",
    "Brasília":"DF",
    "Campinas":"SP"
}

vendedores = [
    "Carlos",
    "Mariana",
    "Felipe",
    "Juliana",
    "Renato",
    "Patrícia",
    "Eduardo",
    "Camila"
]

pagamentos = [
    "Pix",
    "Cartão de Crédito",
    "Cartão de Débito",
    "Boleto"
]

# -----------------------------
# Criando vendas fictícias
# -----------------------------

dados = []

data_inicial = datetime(2025, 1, 1)

for i in range(1, 501):

    produto = random.choice(list(produtos.keys()))
    cidade = random.choice(cidades)

    quantidade = random.randint(1, 5)

    preco = produtos[produto]

    desconto = random.choice([0, 5, 10, 15])

    receita = quantidade * preco * (1 - desconto/100)

    custo = receita * random.uniform(0.55, 0.80)

    lucro = receita - custo

    data = data_inicial + timedelta(days=random.randint(0,364))

    dados.append({
        "ID": i,
        "Data": data,
        "Cliente": random.choice(clientes),
        "Cidade": cidade,
        "Estado": estados[cidade],
        "Produto": produto,
        "Categoria": categorias[produto],
        "Quantidade": quantidade,
        "Preço Unitário": preco,
        "Desconto (%)": desconto,
        "Receita": round(receita,2),
        "Lucro": round(lucro,2),
        "Vendedor": random.choice(vendedores),
        "Pagamento": random.choice(pagamentos)
    })

# -----------------------------
# Criando DataFrame
# -----------------------------

df = pd.DataFrame(dados)

# -----------------------------
# Criando colunas auxiliares
# -----------------------------

df["Mês"] = df["Data"].dt.month

nomes_meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

df["Nome do Mês"] = df["Mês"].map(nomes_meses)

df["Ano"] = df["Data"].dt.year

# -----------------------------
# Salvando CSV
# -----------------------------

df.to_csv("dados_vendas.csv", index=False, encoding="utf-8-sig")

print("="*50)
print("DADOS GERADOS COM SUCESSO!")
print("="*50)

print(df.head())

print("\nTotal de vendas:", len(df))
print("Arquivo salvo como: dados_vendas.csv")

# ============================================================
# FIM DA PARTE 1
# ============================================================

# ============================================================
# PROJETO DE PORTFÓLIO - ANÁLISE DE DADOS DE VENDAS
# PARTE 2 DE 5
# Estatísticas e Relatório
# ============================================================

print("\n" + "="*60)
print("RELATÓRIO GERAL DAS VENDAS")
print("="*60)

# -----------------------------
# Estatísticas Gerais
# -----------------------------

receita_total = df["Receita"].sum()
lucro_total = df["Lucro"].sum()
ticket_medio = df["Receita"].mean()
quantidade_total = df["Quantidade"].sum()

print(f"Receita Total: R$ {receita_total:,.2f}")
print(f"Lucro Total: R$ {lucro_total:,.2f}")
print(f"Ticket Médio: R$ {ticket_medio:,.2f}")
print(f"Quantidade de Itens Vendidos: {quantidade_total}")
print(f"Número de Vendas: {len(df)}")

# -----------------------------
# Produto mais vendido
# -----------------------------

print("\n" + "-"*60)
print("TOP 10 PRODUTOS MAIS VENDIDOS")
print("-"*60)

produtos_vendidos = (
    df.groupby("Produto")["Quantidade"]
      .sum()
      .sort_values(ascending=False)
)

print(produtos_vendidos)

# -----------------------------
# Receita por Categoria
# -----------------------------

print("\n" + "-"*60)
print("RECEITA POR CATEGORIA")
print("-"*60)

categoria_receita = (
    df.groupby("Categoria")["Receita"]
      .sum()
      .sort_values(ascending=False)
)

print(categoria_receita.round(2))

# -----------------------------
# Lucro por Vendedor
# -----------------------------

print("\n" + "-"*60)
print("LUCRO POR VENDEDOR")
print("-"*60)

lucro_vendedor = (
    df.groupby("Vendedor")["Lucro"]
      .sum()
      .sort_values(ascending=False)
)

print(lucro_vendedor.round(2))

# -----------------------------
# Receita por Cidade
# -----------------------------

print("\n" + "-"*60)
print("RECEITA POR CIDADE")
print("-"*60)

receita_cidade = (
    df.groupby("Cidade")["Receita"]
      .sum()
      .sort_values(ascending=False)
)

print(receita_cidade.round(2))

# -----------------------------
# Formas de Pagamento
# -----------------------------

print("\n" + "-"*60)
print("FORMAS DE PAGAMENTO")
print("-"*60)

pagamentos = (
    df["Pagamento"]
      .value_counts()
)

print(pagamentos)

# -----------------------------
# Vendas por Mês
# -----------------------------

vendas_mes = (
    df.groupby(["Mês", "Nome do Mês"])["Receita"]
      .sum()
      .reset_index()
      .sort_values("Mês")
)

print("\n" + "-"*60)
print("FATURAMENTO POR MÊS")
print("-"*60)

print(vendas_mes.round(2))

# -----------------------------
# Produto mais lucrativo
# -----------------------------

produto_lucro = (
    df.groupby("Produto")["Lucro"]
      .sum()
      .sort_values(ascending=False)
)

print("\n" + "-"*60)
print("TOP 5 PRODUTOS MAIS LUCRATIVOS")
print("-"*60)

print(produto_lucro.head())

# -----------------------------
# Cliente que mais comprou
# -----------------------------

clientes_top = (
    df.groupby("Cliente")["Receita"]
      .sum()
      .sort_values(ascending=False)
)

print("\n" + "-"*60)
print("TOP 10 CLIENTES")
print("-"*60)

print(clientes_top.head(10).round(2))

# -----------------------------
# Resumo Executivo
# -----------------------------

print("\n" + "="*60)
print("RESUMO EXECUTIVO")
print("="*60)

print(f"Maior faturamento por cidade: {receita_cidade.idxmax()}")
print(f"Melhor vendedor: {lucro_vendedor.idxmax()}")
print(f"Produto campeão de vendas: {produtos_vendidos.idxmax()}")
print(f"Produto mais lucrativo: {produto_lucro.idxmax()}")
print(f"Cliente que mais comprou: {clientes_top.idxmax()}")

print("="*60)

# ============================================================
# FIM DA PARTE 2
# ============================================================

# ============================================================
# PROJETO DE PORTFÓLIO - ANÁLISE DE DADOS DE VENDAS
# PARTE 3A DE 5
# GRÁFICOS PRINCIPAIS
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# -----------------------------
# GRÁFICO 1 - FATURAMENTO POR MÊS
# -----------------------------

plt.figure(figsize=(10,5))

plt.plot(
    vendas_mes["Mês"],
    vendas_mes["Receita"],
    marker="o"
)

plt.title("Faturamento Mensal")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("graficos/faturamento_mensal.png", dpi=300)
plt.show()

# -----------------------------
# GRÁFICO 2 - RECEITA POR CATEGORIA
# -----------------------------

categoria_receita = (
    df.groupby("Categoria")["Receita"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(10,6))

categoria_receita.plot(kind="barh")

plt.title("Receita por Categoria")
plt.xlabel("Receita (R$)")
plt.ylabel("Categoria")

plt.tight_layout()
plt.savefig("graficos/receita_categoria.png", dpi=300)
plt.show()

# -----------------------------
# GRÁFICO 3 - TOP PRODUTOS VENDIDOS
# -----------------------------

top_produtos = (
    df.groupby("Produto")["Quantidade"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(10,6))

top_produtos.plot(kind="barh")

plt.title("Top Produtos Mais Vendidos")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")

plt.tight_layout()
plt.savefig("graficos/top_produtos.png", dpi=300)
plt.show()

# ============================================================
# FIM DA PARTE 3A
# ============================================================

# ============================================================
# PROJETO DE PORTFÓLIO - ANÁLISE DE DADOS DE VENDAS
# PARTE 3B DE 5
# GRÁFICOS DE DESTAQUE
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# -----------------------------
# GRÁFICO 4 - RECEITA POR CIDADE
# -----------------------------

receita_cidade = (
    df.groupby("Cidade")["Receita"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(10,6))

receita_cidade.plot(kind="barh")

plt.title("Receita por Cidade")
plt.xlabel("Receita (R$)")
plt.ylabel("Cidade")

plt.tight_layout()
plt.savefig("graficos/receita_cidade.png", dpi=300)
plt.show()

# -----------------------------
# GRÁFICO 5 - LUCRO POR VENDEDOR
# -----------------------------

lucro_vendedor = (
    df.groupby("Vendedor")["Lucro"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(10,6))

lucro_vendedor.plot(kind="barh")

plt.title("Lucro por Vendedor")
plt.xlabel("Lucro (R$)")
plt.ylabel("Vendedor")

plt.tight_layout()
plt.savefig("graficos/lucro_vendedor.png", dpi=300)
plt.show()

# -----------------------------
# GRÁFICO 6 - FORMAS DE PAGAMENTO
# -----------------------------

pagamento_count = df["Pagamento"].value_counts()

plt.figure(figsize=(8,5))

pagamento_count.plot(kind="pie", autopct="%1.1f%%")

plt.title("Formas de Pagamento")

plt.ylabel("")
plt.tight_layout()

plt.savefig("graficos/formas_pagamento.png", dpi=300)
plt.show()

# ============================================================
# FIM DA PARTE 3B
# ============================================================

# ============================================================
# PROJETO DE PORTFÓLIO - ANÁLISE DE DADOS DE VENDAS
# PARTE 4 DE 5
# GRÁFICOS AVANÇADOS
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# -----------------------------
# GRÁFICO 7 - HEATMAP (CORRELAÇÃO)
# -----------------------------

plt.figure(figsize=(8,6))

corr = df[["Quantidade", "Preço Unitário", "Receita", "Lucro", "Desconto (%)"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Mapa de Correlação entre Variáveis")

plt.tight_layout()
plt.savefig("graficos/heatmap_correlacao.png", dpi=300)
plt.show()

# -----------------------------
# GRÁFICO 8 - HISTOGRAMA DE RECEITA
# -----------------------------

plt.figure(figsize=(10,5))

plt.hist(df["Receita"], bins=20)

plt.title("Distribuição da Receita por Venda")
plt.xlabel("Receita (R$)")
plt.ylabel("Frequência")

plt.tight_layout()
plt.savefig("graficos/histograma_receita.png", dpi=300)
plt.show()

# -----------------------------
# GRÁFICO 9 - BOXPLOT (OUTLIERS)
# -----------------------------

plt.figure(figsize=(8,6))

sns.boxplot(y=df["Receita"])

plt.title("Distribuição e Outliers da Receita")

plt.tight_layout()
plt.savefig("graficos/boxplot_receita.png", dpi=300)
plt.show()

# -----------------------------
# GRÁFICO 10 - RELAÇÃO RECEITA X LUCRO
# -----------------------------

plt.figure(figsize=(8,6))

plt.scatter(df["Receita"], df["Lucro"], alpha=0.5)

plt.title("Relação entre Receita e Lucro")
plt.xlabel("Receita (R$)")
plt.ylabel("Lucro (R$)")

plt.tight_layout()
plt.savefig("graficos/scatter_receita_lucro.png", dpi=300)
plt.show()

# ============================================================
# FIM DA PARTE 4
# ============================================================

# ============================================================
# PROJETO DE PORTFÓLIO - ANÁLISE DE DADOS DE VENDAS
# PARTE 5 DE 5
# FINALIZAÇÃO E ORGANIZAÇÃO
# ============================================================

import os

print("\n" + "="*60)
print("FINALIZAÇÃO DO PROJETO")
print("="*60)

# -----------------------------
# VERIFICAÇÃO DOS ARQUIVOS
# -----------------------------

print("\nArquivos gerados na pasta 'graficos':\n")

for arquivo in os.listdir("graficos"):
    print("-", arquivo)

# -----------------------------
# RESUMO FINAL MAIS PROFISSIONAL
# -----------------------------

print("\n" + "="*60)
print("RESUMO EXECUTIVO FINAL")
print("="*60)

print(f"""
📊 Total de vendas analisadas: {len(df)}
💰 Receita total: R$ {df['Receita'].sum():,.2f}
📈 Lucro total: R$ {df['Lucro'].sum():,.2f}
🛒 Produtos diferentes: {df['Produto'].nunique()}
🏙️ Cidades atendidas: {df['Cidade'].nunique()}
👨‍💼 Vendedores ativos: {df['Vendedor'].nunique()}
💳 Formas de pagamento: {df['Pagamento'].nunique()}
""")

# -----------------------------
# INSIGHTS AUTOMÁTICOS
# -----------------------------

produto_top = df.groupby("Produto")["Quantidade"].sum().idxmax()
vendedor_top = df.groupby("Vendedor")["Lucro"].sum().idxmax()
cidade_top = df.groupby("Cidade")["Receita"].sum().idxmax()
categoria_top = df.groupby("Categoria")["Receita"].sum().idxmax()

print("\n" + "="*60)
print("INSIGHTS PRINCIPAIS")
print("="*60)

print(f"🏆 Produto mais vendido: {produto_top}")
print(f"🏆 Melhor vendedor (lucro): {vendedor_top}")
print(f"🏆 Cidade com maior faturamento: {cidade_top}")
print(f"🏆 Categoria mais forte: {categoria_top}")

# -----------------------------
# DICA DE PORTFÓLIO
# -----------------------------

print("\n" + "="*60)
print("DICA DE PORTFÓLIO")
print("="*60)

print("""
💡 Para deixar esse projeto ainda mais forte no GitHub:

1. Coloque o código em um repositório com nome:
   'analise-vendas-python'

2. Adicione um README.md explicando:
   - objetivo do projeto
   - ferramentas usadas (Pandas, Matplotlib, Seaborn)
   - prints dos gráficos

3. Suba a pasta 'graficos' junto

4. Escreva:
   "Projeto de análise de dados com Python (portfólio)"

🔥 Isso pode te ajudar a conseguir estágio ou vaga júnior
""")

print("\n" + "="*60)
print("PROJETO FINALIZADO COM SUCESSO!")
print("="*60)

# ============================================================
# FIM DO PROJETO
# ============================================================
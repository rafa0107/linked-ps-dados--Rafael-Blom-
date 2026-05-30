import streamlit as st
import pandas as pd
import plotly.express as px

from src.loader import load_data

df, _ = load_data()

import streamlit as st

st.set_page_config(
    page_title="Análise Avançada",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Análise Avançada")

# ====================================
# FILTROS
# ====================================

st.sidebar.header("Filtros")

regioes = st.sidebar.multiselect(
    "Região",
    sorted(df["customer_region"].unique()),
    default=sorted(df["customer_region"].unique())
)

categorias = st.sidebar.multiselect(
    "Categoria",
    sorted(df["product_category"].unique()),
    default=sorted(df["product_category"].unique())
)

df = df[
    (df["customer_region"].isin(regioes))
    &
    (df["product_category"].isin(categorias))
]

# ====================================
# GEOGRÁFICO E TEMPORAL
# ====================================

st.subheader("Comportamento Geográfico e Temporal")

c1,c2 = st.columns(2)

with c1:

    geo = (
        df[df["order_status"] != "Cancelado"]
        .groupby("customer_region")
        ["total_value"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        geo,
        x="customer_region",
        y="total_value",
        title="Receita Líquida por Região",
        labels={
            "customer_region":"Região",
            "total_value":"Receita Líquida (R$)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

with c2:

    evolucao = (
        df.groupby("order_date")
        ["total_value"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        evolucao,
        x="order_date",
        y="total_value",
        markers=True,
        title="Evolução das Vendas",
        labels={
            "order_date":"Data",
            "total_value":"Receita (R$)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================
# CATEGORIAS
# ====================================

st.subheader("Categorias e Preço Médio")

cat = (
    df.groupby("product_category")
    .agg(
        Produtos=("product_name","nunique"),
        Itens_Vendidos=("quantity","sum"),
        Preco_Medio=("unit_price","mean")
    )
    .reset_index()
)

st.dataframe(cat, use_container_width=True)

# ====================================
# PORTFÓLIO
# ====================================

st.subheader("Segmentação de Portfólio")

segmentacao = (
    df.groupby("faixa_preco")
    .agg(
        Receita=("total_value","sum"),
        Volume=("quantity","sum")
    )
    .reset_index()
)

c3,c4 = st.columns(2)

with c3:

    fig = px.bar(
        segmentacao,
        x="faixa_preco",
        y="Receita",
        title="Receita por Faixa de Preço",
        labels={
            "faixa_preco":"Faixa de Preço",
            "Receita":"Receita (R$)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

with c4:

    fig = px.bar(
        segmentacao,
        x="faixa_preco",
        y="Volume",
        title="Volume por Faixa de Preço",
        labels={
            "faixa_preco":"Faixa de Preço",
            "Volume":"Itens Vendidos"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

# Dependência SKU

top_sku = (
    df.groupby("product_name")
    ["total_value"]
    .sum()
    .sort_values(ascending=False)
)

produto_lider = top_sku.index[0]

participacao = (
    top_sku.iloc[0]
    /
    df["total_value"].sum()
) * 100

st.metric(
    "Dependência do SKU Líder",
    f"{participacao:.2f}%"
)

st.info(
    f"Produto com maior participação na receita: {produto_lider}"
)

# ====================================
# SAZONALIDADE
# ====================================

st.subheader("Sazonalidade Semanal")

ordem = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

sazonalidade = (
    df.groupby("dia_semana")
    ["total_value"]
    .sum()
    .reset_index()
)

sazonalidade["dia_semana"] = pd.Categorical(
    sazonalidade["dia_semana"],
    categories=ordem,
    ordered=True
)

sazonalidade = sazonalidade.sort_values(
    "dia_semana"
)

fig = px.bar(
    sazonalidade,
    x="dia_semana",
    y="total_value",
    title="Receita por Dia da Semana",
    labels={
        "dia_semana":"Dia da Semana",
        "total_value":"Receita (R$)"
    }
)

st.plotly_chart(fig, use_container_width=True)

# ====================================
# CANCELAMENTOS
# ====================================

cancelados = df[
    df["order_status"] == "Cancelado"
]

if len(cancelados) > 0:

    correlacao = (
        cancelados
        .groupby(
            ["product_name", "payment_method"]
        )
        .size()
        .reset_index(name="Quantidade")
    )

    fig = px.bar(
        correlacao,
        x="product_name",
        y="Quantidade",
        color="payment_method",
        barmode="group",
        title="Cancelamentos por Produto e Forma de Pagamento",
        labels={
            "product_name":"Produto",
            "payment_method":"Forma de Pagamento",
            "Quantidade":"Quantidade de Cancelamentos"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    cancel_produto = (
    cancelados["product_name"]
    .value_counts()
    .head(20)
    .reset_index()
)

cancel_produto.columns = [
    "Produto",
    "Cancelamentos"
]

fig = px.bar(
    cancel_produto,
    x="Produto",
    y="Cancelamentos",
    title="Produtos com Mais Cancelamentos - Top 20"
)

cancel_pagamento = (
    cancelados["payment_method"]
    .value_counts()
    .reset_index()
)

cancel_pagamento.columns = [
    "Pagamento",
    "Cancelamentos"
]

fig2 = px.pie(
    cancel_pagamento,
    names="Pagamento",
    values="Cancelamentos",
    hole=.4,
    title="Cancelamentos por Forma de Pagamento"
)

c1, c2 = st.columns(2)

with c1:
    st.plotly_chart(fig)

with c2:
    st.plotly_chart(fig2)
import streamlit as st
import pandas as pd
import plotly.express as px

from src.loader import load_data

df, _ = load_data()

import streamlit as st

st.set_page_config(
    page_title="Análise Descritiva",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Análise Descritiva")

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
# KPIs
# ====================================

receita_bruta = df["total_value"].sum()

receita_liquida = df[
    df["order_status"] != "Cancelado"
]["total_value"].sum()

total_pedidos = df["order_id"].nunique()

ticket_medio = receita_bruta / total_pedidos

cancelamento_pct = (
    (df["order_status"] == "Cancelado").sum()
    / len(df)
) * 100

col1,col2,col3,col4,col5 = st.columns(5)

col1.metric("Receita Bruta", f"R$ {receita_bruta:,.2f}")
col2.metric("Receita Líquida", f"R$ {receita_liquida:,.2f}")
col3.metric("Pedidos", total_pedidos)
col4.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")
col5.metric("Taxa Cancelamento", f"{cancelamento_pct:.2f}%")

st.divider()

# ====================================
# REGIÕES
# ====================================

st.subheader("Distribuição por Região")

analise_regiao = (
    df.groupby("customer_region")
    .agg(
        Pedidos=("order_id","count"),
        Receita=("total_value","sum")
    )
    .reset_index()
)

c1,c2 = st.columns(2)

with c1:

    fig = px.bar(
        analise_regiao,
        x="customer_region",
        y="Receita",
        title="Receita por Região",
        labels={
            "customer_region":"Região",
            "Receita":"Receita (R$)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

with c2:

    fig = px.bar(
        analise_regiao,
        x="customer_region",
        y="Pedidos",
        title="Quantidade de Pedidos por Região",
        labels={
            "customer_region":"Região",
            "Pedidos":"Quantidade de Pedidos"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================
# PRODUTOS
# ====================================

st.subheader("Análise de Produtos")

produtos = (
    df.groupby("product_name")
    .agg(
        Volume_Total=("quantity","sum"),
        Receita_Total=("total_value","sum")
    )
    .reset_index()
)

c3,c4 = st.columns(2)

with c3:

    top_volume = (
        produtos
        .sort_values("Volume_Total", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_volume,
        x="Volume_Total",
        y="product_name",
        orientation="h",
        title="Produtos Mais Vendidos",
        labels={
            "Volume_Total":"Quantidade Vendida",
            "product_name":"Produto"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

with c4:

    top_receita = (
        produtos
        .sort_values("Receita_Total", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_receita,
        x="Receita_Total",
        y="product_name",
        orientation="h",
        title="Produtos com Maior Receita",
        labels={
            "Receita_Total":"Receita (R$)",
            "product_name":"Produto"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================
# STATUS E PAGAMENTO
# ====================================

c5,c6 = st.columns(2)

with c5:

    status = (
        df["order_status"]
        .value_counts()
        .reset_index()
    )

    status.columns = ["Status","Quantidade"]

    fig = px.pie(
        status,
        names="Status",
        values="Quantidade",
        hole=.4,
        title="Status dos Pedidos"
    )

    st.plotly_chart(fig, use_container_width=True)

with c6:

    pagamento = (
        df["payment_method"]
        .value_counts()
        .reset_index()
    )

    pagamento.columns = ["Forma de Pagamento","Quantidade"]

    fig = px.pie(
        pagamento,
        names="Forma de Pagamento",
        values="Quantidade",
        hole=.4,
        title="Métodos de Pagamento"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================
# PREÇO MÉDIO
# ====================================

st.subheader("Preço Médio")

preco_medio_geral = df["unit_price"].mean()

st.metric(
    "Preço Médio Geral",
    f"R$ {preco_medio_geral:,.2f}"
)

preco_categoria = (
    df.groupby("product_category")
    ["unit_price"]
    .mean()
    .reset_index()
)

fig = px.bar(
    preco_categoria,
    x="product_category",
    y="unit_price",
    title="Preço Médio por Categoria",
    labels={
        "product_category":"Categoria",
        "unit_price":"Preço Médio (R$)"
    }
)

st.plotly_chart(fig, use_container_width=True)
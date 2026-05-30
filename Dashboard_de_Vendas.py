import streamlit as st

st.set_page_config(
    page_title="Linked PS 2026 Dados - Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard de Vendas")

st.markdown("""
### Desafio Técnico - Linked PS

Este dashboard apresenta:

- Indicadores Executivos
- Análises Descritivas
- Análises Avançadas

Utilize o menu lateral para navegar.
""")

st.info(
    "Os dados foram tratados previamente e modelados em fVendas e dCalendario."
)
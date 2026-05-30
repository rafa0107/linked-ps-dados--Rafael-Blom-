import pandas as pd
import streamlit as st

''' Utiliza cache para guardar os dados do csv, evitando ler ele toda hora que dá o refresh na página'''
@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/f_vendas_tratada.csv",
        parse_dates=["order_date"]
    )

    calendario = pd.read_csv(
        "data/d_calendario.csv"
    )

    return df, calendario
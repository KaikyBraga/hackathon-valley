import pandas as pd
import streamlit as st
from dataframes import *
from bokeh.models import HoverTool
from bokeh.plotting import figure, show
from ranking_acumulados import limpeza_dados_top15_bairros, criar_grafico_top15


st.set_page_config(page_title="Visualização")

#with open("styles.css") as f:
    #st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  

with st.container():
    st.title("Visualizações dos Dados")
    st.write("...")

df = limpeza_dados_top15_bairros(df_taxa_precipitacao_cemaden, df_taxa_precipitacao_inea, df_taxa_precipitacao_websirene, df_estacoes_alertario, df_estacoes_cemaden, df_estacoes_inea, df_estacoes_websirene)

grafico = criar_grafico_top15(df)

st.bokeh_chart(grafico, use_container_width=True)
  
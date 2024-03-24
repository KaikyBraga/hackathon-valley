import pandas as pd
import streamlit as st
from dataframes import *
from bokeh.models import HoverTool
from bokeh.plotting import figure, show
from ranking_acumulados import limpeza_dados_top15_bairros, criar_grafico_top15
from dataframes import *
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely import wkt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import pandas as pd
import geopandas as gpd
import json
import pylab as plt
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool
from bokeh.plotting import figure
from bokeh.palettes import brewer
from mapa import *


st.set_page_config(page_title="Visualização")

#with open("styles.css") as f:
    #st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  

with st.container():
    st.title("Visualizações dos Dados")
    st.write("...")

# Gráfico de Ranking
df = limpeza_dados_top15_bairros(df_taxa_precipitacao_cemaden, df_taxa_precipitacao_inea, df_taxa_precipitacao_websirene, df_estacoes_alertario, df_estacoes_cemaden, df_estacoes_inea, df_estacoes_websirene)

grafico = criar_grafico_top15(df)

st.bokeh_chart(grafico, use_container_width=True)

# Gráfico de Mapa
start_data, end_data = st.select_slider(
    "Selecione o período de Análise de Precipitação",
    options=datas_precipitacao,
    value=(datas_precipitacao[0], datas_precipitacao[-1]))
st.write("Você selecionou datas entre", start_data, "e", end_data)

dia, mes, ano = start_data.split('-')
start_data = f"{ano}-{mes}-{dia}"
dia, mes, ano = end_data.split('-')
end_data = f"{ano}-{mes}-{dia}"

df_mapa_precipitacao = df_mapa(data_inicio=start_data, data_fim=end_data)

st.bokeh_chart(bokeh_plot_map(df=df_mapa_precipitacao), use_container_width=True)
  
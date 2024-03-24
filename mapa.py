from dataframes import *
import streamlit as st
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely import wkt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

filtro_zona_sul = 'nome_regiao_planejamento == "Centro"'



def plot_gráfico(df_bairro, df_taxa_precipitacao_guaratiba):

    df_taxa_precipitacao_guaratiba = df_taxa_precipitacao_guaratiba.groupby("bairro").mean("predictions").reset_index()
    df_taxa_precipitacao_guaratiba = df_taxa_precipitacao_guaratiba[["bairro","predictions"]]

    df_bairro["geometry"] = df_bairro["geometry"].apply(wkt.loads)
    df_bairro.rename(columns={"nome": "bairro"}, inplace = True)
    df_bairro = pd.merge(df_bairro, df_taxa_precipitacao_guaratiba, on="bairro", how="left")
    df_bairro["predictions"] = df_bairro["predictions"].fillna(-1)
    df_bairro = df_bairro[df_bairro["predictions"] != -1]
    
    df_bairro = gpd.GeoDataFrame(df_bairro, geometry="geometry", crs=3395)

    janela, graf = plt.subplots(1, 1, figsize=(10, 10))
    df_bairro.plot("predictions", edgecolor="black", linewidth=0.4, ax=graf, cmap=plt.cm.Blues)
    graf.set_title("Nível de Precipitação no mês",
                    fontdict={"fontsize": "20", "fontname": "Arial", "fontweight": "bold"})
    
    # Barra de legenda à direita do mapa
    eixos_divisor = make_axes_locatable(graf)
    colorbar_axis = eixos_divisor.append_axes("right", size="5%", pad=0.1)
    cbar = plt.colorbar(plt.cm.ScalarMappable(norm=None, cmap=plt.cm.Blues), cax=colorbar_axis)

    # Rótulos e posições dos ticks na barra de cores
    ticks = [0, 25, 50, 75, 100]
    tick_labels = [f'{tick}%' for tick in ticks]
    cbar.set_ticks([tick / 100 for tick in ticks])
    cbar.set_ticklabels(tick_labels, fontdict={"fontsize": "10", "fontname": "Arial"})
    cbar.set_label("Escala de Precipitação", rotation=270, labelpad=15, fontdict={"fontsize": "12", "fontname": "Arial"})
  
    plt.savefig("visualizacoes.png", format="png")
    

plot_gráfico(df_bairro=df_bairro, df_taxa_precipitacao_guaratiba=df_taxa_precipitacao_guaratiba)

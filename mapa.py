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
from dataframes import *

def df_mapa(df_bairro=df_bairro, df_taxa_precipitacao_guaratiba=df_taxa_precipitacao_guaratiba, data_fim=datas_precipitacao[-1],data_inicio=datas_precipitacao[0]):
    """
    Prepração dos dados para Plotagem do Mapa de Precipitação.
    """
    
    # Filtro dos colunas de Precipitação
    df_taxa_precipitacao_guaratiba = df_taxa_precipitacao_guaratiba[data_inicio <= df_taxa_precipitacao_guaratiba["data_particao"]]
    df_taxa_precipitacao_guaratiba = df_taxa_precipitacao_guaratiba[df_taxa_precipitacao_guaratiba["data_particao"] <= data_fim]
    df_taxa_precipitacao_guaratiba = df_taxa_precipitacao_guaratiba.groupby("bairro").mean("predictions").reset_index()
    df_taxa_precipitacao_guaratiba = df_taxa_precipitacao_guaratiba[["bairro","predictions"]]

    df_bairro.rename(columns={"nome": "bairro"}, inplace=True)

    # Adição da coluna de Predição no DataFrame de Bairros
    df_bairro = pd.merge(df_bairro, df_taxa_precipitacao_guaratiba, on="bairro", how="left")

    # Remoção de dados faltantes
    df_bairro["predictions"] = df_bairro["predictions"].fillna(-1)
    df_bairro = df_bairro[df_bairro["predictions"] != -1]

    # Filtro do DataFrame de Bairros
    df_bairro = df_bairro[["bairro", "geometry", "predictions"]]
    df_bairro["predictions"] = df_bairro["predictions"].round(3) 
    df_bairro["geometry"] = df_bairro["geometry"].apply(wkt.loads)

    return df_bairro

def converter_geojson(df):
    """
    Conversão de um DataFrame para um GeoJSONDataSource
    """

    geo_source = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:3395")
    geojson = geo_source.to_json()
    geojson_str = json.dumps(json.loads(geojson))
    geo_source = GeoJSONDataSource(geojson=geojson_str)

    return geo_source

def bokeh_plot_map(df, column="predictions", title="Nível de Precipitação no Rio de Janeiro"):
    """
    Plot bokeh map do Nível de Precipitação no Rio de Janeiro
    """

    geosource = converter_geojson(df)

    # Definição de paleta e coluna referente a cor
    palette = brewer["Blues"][5]
    palette = palette[::-1]
    vals = df[column]

    # Instantiate LinearColorMapper que mapeia linearmente os números em um intervalo em uma sequência de cores
    color_mapper = LinearColorMapper(palette = palette, low = vals.max(), high = vals.min())
    color_bar = ColorBar(color_mapper=LinearColorMapper(palette = palette, low = vals.min(), high = vals.max()), label_standoff=8, width=800, height=20,
                         location=(0,0), orientation="horizontal")
    
    # Configurações Base do Plot
    plot = figure(title = title, height=500, width=800, toolbar_location=None, tools="")
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = None

    # Adição do renderizador na figura
    plot.patches("xs", "ys", source=geosource, fill_alpha=1, line_width=0.5, line_color="black",  
                            fill_color={"field": column, "transform": color_mapper})

    # Layout da figura
    plot.add_layout(color_bar, 'below')

    # Configurações do título
    plot.title.text_font = "Arial"
    plot.title.text_font_size = "18pt"
    plot.title.align = "center"

    # Ferramentas interativas
    hover = HoverTool(tooltips=[("Bairro", "@bairro"), ("Precipitação", "@predictions")])
    plot.add_tools(hover)
    
    return plot

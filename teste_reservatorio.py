from dataframes import *
from bokeh.models import Range1d, HoverTool
from bokeh.plotting import figure, show
import pandas as pd
import numpy as np
import streamlit as st

def plot_nivel_reservatorio(reservatorios=['Bandeira'], anos=[2021]):
    df_nivel_reservatorio_usado = df_nivel_reservatorio[df_nivel_reservatorio["data_particao"].dt.year.isin(anos)]
    df_nivel_reservatorio_usado = df_nivel_reservatorio_usado[df_nivel_reservatorio_usado["altura_agua"] < 100]

    p = figure(title="Nível Anual dos Reservatórios", x_axis_label="X", y_axis_label="Y",
               x_axis_type="datetime",
               y_range=Range1d(0, 5),
               width=800)

    cores = {
        'Bandeira': "Blue",
        'Varnhagen': "Green",
        'Niteroi': "Red"
    }

    lines = []
    for reservatorio in reservatorios:
        # Obtendo o ID do reservatório
        reservatorio_id = reservatorios_dict[reservatorio]  
        df_new_line = df_nivel_reservatorio_usado[df_nivel_reservatorio_usado["id_reservatorio"] == reservatorio_id].sort_values(["data_particao"])

        line = p.line(x="data_particao", y="altura_agua",
                      legend_field="nome_reservatorio",
                      color=cores[reservatorio],
                      source=df_new_line)
        lines.append(line)

    hovertool = HoverTool(
        tooltips=[("Nível de Água", "@altura_agua"), ("Data", "@data_particao{%F}")],
        formatters={"@data_particao": "datetime"},
        renderers=lines,
        mode="vline")
    p.add_tools(hovertool)

    return p

# Opções para o selectbox do reservatório
opcoes_reservatorios = df_nivel_reservatorio["nome_reservatorio"].unique()

# Mapear o nome do reservatório selecionado para o ID correspondente
reservatorios_dict = {nome: id for id, nome in zip(df_nivel_reservatorio["id_reservatorio"], df_nivel_reservatorio["nome_reservatorio"])}

# Selecionar reservatório com o selectbox
reservatorio_selecionado = st.selectbox("Selecione o reservatório:", opcoes_reservatorios, format_func=lambda x: x)

# Opções para o selectbox do ano, ordenadas
opcoes_anos = df_nivel_reservatorio["data_particao"].dt.year.unique()
opcoes_anos = sorted(opcoes_anos)

# Selecionar ano com o selectbox
ano_selecionado = st.selectbox("Selecione o ano:", opcoes_anos)

# Plotar o gráfico com o reservatório e ano selecionados
grafico = plot_nivel_reservatorio(reservatorios=[reservatorio_selecionado], anos=[ano_selecionado])
st.bokeh_chart(grafico)
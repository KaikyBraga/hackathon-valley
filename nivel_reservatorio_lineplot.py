from dataframes import df_nivel_reservatorio
from bokeh.models import Range1d, HoverTool
from bokeh.plotting import figure, show
import streamlit as st

def plot_nivel_reservatorio(reservatorios=[1], anos=[2021]):
    df_nivel_reservatorio_usado = df_nivel_reservatorio[df_nivel_reservatorio["data_particao"].dt.year.isin(anos)]
    df_nivel_reservatorio_usado = df_nivel_reservatorio_usado[df_nivel_reservatorio_usado["altura_agua"] < 100]

    p = figure(title="Nível Anual dos Reservatórios", x_axis_label="X", y_axis_label="Y",
               x_axis_type="datetime",
               y_range=Range1d(0, 10),
               width=800)
    
    # Ajustar o tamanho do título
    p.title.text_font_size = "18pt"
    p.title.align = "center"

    cores = {
        1 : "Blue",
        2 : "Green",
        3 : "Red"
    }

    lines = []
    for reservatorio in reservatorios:
        df_new_line = df_nivel_reservatorio_usado[df_nivel_reservatorio_usado["id_reservatorio"] == reservatorio].sort_values(["data_particao"])

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

def trata_nivel_reservatorio(df_nivel_reservatorio):
    # Opções para o selectbox do reservatório
    opcoes_reservatorios = df_nivel_reservatorio["id_reservatorio"].unique()

    # Mapear o nome do reservatório selecionado para o ID correspondente
    reservatorios_dict = {id: nome for id, nome in zip(df_nivel_reservatorio["id_reservatorio"], df_nivel_reservatorio["nome_reservatorio"])}

    # Selecionar reservatório com o selectbox
    reservatorio_selecionado = st.selectbox("Selecione o reservatório:", opcoes_reservatorios, format_func=lambda x: reservatorios_dict[x])

    # Opções para o selectbox do ano, ordenadas
    opcoes_anos = df_nivel_reservatorio["data_particao"].dt.year.unique()
    opcoes_anos = sorted(opcoes_anos)

    # Selecionar ano com o selectbox
    ano_selecionado = st.selectbox("Selecione o ano:", opcoes_anos)

    return reservatorio_selecionado, ano_selecionado

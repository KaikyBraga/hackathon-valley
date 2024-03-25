import pandas as pd
import streamlit as st
from dataframes import *
from ranking_acumulados import limpeza_dados_top15_bairros, criar_grafico_top15
import pandas as pd
from mapa import *
from ranking_chamados import top_10_chamados
from nivel_reservatorio_lineplot import plot_nivel_reservatorio, trata_nivel_reservatorio


st.set_page_config(page_title="Visualização") 

with st.container():
    st.title("Visualizações dos Dados")
    st.write("...")

with st.container():
    # Gráfico de Ranking
    df = limpeza_dados_top15_bairros(df_taxa_precipitacao_cemaden, df_taxa_precipitacao_inea, df_taxa_precipitacao_websirene, df_estacoes_alertario, df_estacoes_cemaden, df_estacoes_inea, df_estacoes_websirene)

    grafico = criar_grafico_top15(df)

    st.bokeh_chart(grafico, use_container_width=True)

# Visualização do top 10 chamados
with st.container():
    plot_2 = top_10_chamados(df_bairro, df_chamado)

    st.bokeh_chart(plot_2, use_container_width=True)

# Gráfico de Mapa
with st.container():
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

# Gráfico reservatórios
with st.container():

    reservatorio_selecionado, ano_selecionado = trata_nivel_reservatorio(df_nivel_reservatorio)

    # Plotar o gráfico com o reservatório e ano selecionados
    grafico = plot_nivel_reservatorio(reservatorios=[reservatorio_selecionado], anos=[ano_selecionado])

    st.bokeh_chart(grafico, use_container_width=True)




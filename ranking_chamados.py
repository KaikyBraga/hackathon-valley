from dataframes import *
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource

def top_10_chamados(df_bairro, df_chamado):

    """
    Cria top 10 dos bairros com maiores chamados.
    """

    # Adicionando a coluna nome_bairro do df_2 ao df_1
    df_merged = pd.merge(df_chamado, df_bairro[["id_bairro", "nome"]], on="id_bairro", how="left")

    # Ordenar os top 10 bairros por contagem decrescente
    top_10_bairros = df_merged["nome"].value_counts().head(10).sort_values(ascending = True)

    # Criar uma fonte de dados para o gráfico de barras
    source = ColumnDataSource(data=dict(bairros=top_10_bairros.index.tolist(),
                                        contagem=top_10_bairros.tolist()))

    # Criação da figura
    plot_2 = figure(tools="xpan", toolbar_location=None, y_range=top_10_bairros.index.tolist())

    # Construindo um gráfico de barras horizontais
    plot_2.hbar(y="bairros", right="contagem", height=0.7, source=source, color="MediumBlue")

    # Nomeando o gráfico
    plot_2.title.text = "Os 10 bairros com mais chamados"
    plot_2.title.align = "left"

    # Configurando as dimensões e o fundo das visualizações
    plot_2.width = 640
    plot_2.height = 480
    plot_2.ygrid.grid_line_color = None
    plot_2.background_fill_color = "Gainsboro"

    # Customização dos eixos
    plot_2.xaxis.axis_label_text_color = "black"
    plot_2.xaxis.axis_label_text_font = "Arial"
    plot_2.xaxis.axis_label_text_font_size = "12px"

    plot_2.yaxis.axis_label_text_color = "black"
    plot_2.yaxis.axis_label_text_font = "Arial"
    plot_2.yaxis.axis_label_text_font_size = "12px"

    # Adicionando a ferramenta de hover
    hover = HoverTool()
    hover.tooltips = [("Bairro", "@bairros"), ("Quantidade de Chamados", "@contagem")]
    plot_2.add_tools(hover)

    return plot_2

# Exibir o gráfico
show(top_10_chamados(df_bairro, df_chamado))
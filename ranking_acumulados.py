from bokeh.plotting import figure, show
from bokeh.models import HoverTool
from dataframes import *
import pandas as pd

# Renomeando a coluna
df_taxa_precipitacao_cemaden["acumulado_chuva_96h"] = df_taxa_precipitacao_cemaden["acumulado_chuva_96_h"]
df_taxa_precipitacao_inea["acumulado_chuva_96h"] = df_taxa_precipitacao_inea["acumulado_chuva_96_h"]
df_taxa_precipitacao_websirene["acumulado_chuva_96h"] = df_taxa_precipitacao_websirene["acumulado_chuva_96_h"]

# Separando as horas da coluna "data_medicao"
df_taxa_precipitacao_alertario_5min["hora"] = df_taxa_precipitacao_alertario_5min["data_medicao"].str.split().str[1]
df_taxa_precipitacao_cemaden["hora"] = df_taxa_precipitacao_cemaden["data_medicao"].str.split().str[1]  
df_taxa_precipitacao_inea["hora"] = df_taxa_precipitacao_inea["data_medicao"].str.split().str[1]  

# Separando as horas da coluna "primary_key"
df_taxa_precipitacao_websirene["hora"] = df_taxa_precipitacao_websirene["primary_key"].str.split().str[1]  

# Separando dataframes
df1 = df_taxa_precipitacao_alertario_5min[["id_estacao", "acumulado_chuva_96h", "hora", "data_particao"]]
df2 = df_estacoes_alertario[["id_estacao", "estacao"]]

df3 = df_taxa_precipitacao_cemaden[["id_estacao", "acumulado_chuva_96h", "hora", "data_particao"]]
df4 = df_estacoes_cemaden[["id_estacao", "estacao"]]

df5 = df_taxa_precipitacao_inea[["id_estacao", "acumulado_chuva_96h", "hora", "data_particao"]]
df6 = df_estacoes_inea[["id_estacao", "estacao"]]

df7 = df_taxa_precipitacao_websirene[["id_estacao", "acumulado_chuva_96h", "hora", "data_particao"]]
df8 = df_estacoes_websirene[["id_estacao", "estacao"]]

# Convertendo para datetime
df1["data_particao"] = pd.to_datetime(df1["data_particao"])
df1["hora"] = pd.to_datetime(df1["hora"])

df3["data_particao"] = pd.to_datetime(df3["data_particao"])
df3["hora"] = pd.to_datetime(df3["hora"])

df5["data_particao"] = pd.to_datetime(df5["data_particao"])
df5["hora"] = pd.to_datetime(df5["hora"])

df7["data_particao"] = pd.to_datetime(df7["data_particao"])
df7["hora"] = pd.to_datetime(df7["hora"])

# Juntando dataframes
df1_df3_df5_df7_concat = pd.concat([df1, df3, df5, df7], ignore_index=True)
df2_df4_df6_df8_concat = pd.concat([df2, df4, df6, df8], ignore_index=True)
df_merge_final = df1_df3_df5_df7_concat.merge(df2_df4_df6_df8_concat, on="id_estacao")

# Trocando valores NaN por O na coluna "acumulado_chuva_96h"
df_merge_final["acumulado_chuva_96h"] = df_merge_final["acumulado_chuva_96h"].fillna(0)

# Filtrar os dados para o horário específico de 00:30:00
df_filtrado = df_merge_final[df_merge_final["hora"].dt.time == pd.to_datetime("00:30:00").time()]

# Agrupar os dados por bairro e dia e selecionar os valores correspondentes
df_media_por_bairro = df_filtrado.groupby("estacao")["acumulado_chuva_96h"].mean()

# Convertendo a Serie para um Dataframe
df_media_acumulado_bairro = pd.DataFrame(df_media_por_bairro)

# Reseta o índice para trazer a coluna "estacao" de volta como uma coluna
df_media_acumulado_bairro.reset_index(inplace=True)

# Renomear a coluna das médias
df_media_acumulado_bairro["media_acumulado"] = df_media_acumulado_bairro["acumulado_chuva_96h"]

# Ordenando os dados pela coluna "estacao"
df_ordenado = df_media_acumulado_bairro.sort_values(by="media_acumulado", ascending=False).head(15)

# Definindo uma paleta de cores personalizada
paleta_cores_por_bairro = {"Pavuna":"#3F068F", "Vigario geral":"#4C11F9", "Est. pedra bonita":"#8417FA", "Usina":"#0CADFA", 
                           "Andarai":"#15DBFA", "Vicente de carvalho":"#15E0BE", "Padre miguel":"#00EB7D", "Realengo batan":"#E0E071", 
                           "Catete":"#E1DC36", "Jacarepagua":"#DCBA13", "Sao conrado":"#DB9F10", "Praca seca":"#FA8D16", 
                           "Vargem pequena":"#FA5E00", "Jardim maravilha":"#FA0403", "Tanque jacarepagua":"#992400"}

# Criando uma nova coluna no DataFrame para armazenar as cores
df_ordenado["cores"] = df_ordenado["estacao"].map(paleta_cores_por_bairro)

# Criando a figura
p = figure(x_range=df_ordenado["estacao"], height=600, width=1000, title="Top 15 bairros que mais chovem no Rio",
           toolbar_location=None, tools="")

# Adicionando as barras ao gráfico com a paleta de cores
p.vbar(x="estacao", top="media_acumulado", width=0.7, source=df_ordenado, line_color="white", fill_color='cores')

# Configurando os eixos
p.xaxis.major_label_orientation = 45
p.xaxis.major_label_text_font_size = "12pt"
p.xaxis.axis_label = ""
p.yaxis.axis_label = "Acumulado de Chuva(mm)"
p.yaxis.axis_label_text_font_size = "14pt"

# Editando o título
p.title.align = "center"
p.title.text_font_size = "18pt"

# Adicionando a ferramenta de hover
hover = HoverTool()
hover.tooltips = [("Bairro", "@estacao"), ("Quantidade de Chuva", "@media_acumulado")]
p.add_tools(hover)

# Exibindo o gráfico
show(p)
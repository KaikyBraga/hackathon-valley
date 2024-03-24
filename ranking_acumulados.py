import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dataframes import *

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

# Renomear a coluna das médias
df_media_acumulado_bairro["media_acumulado"] = df_media_acumulado_bairro["acumulado_chuva_96h"]

# Ordenando os dados pela coluna "estacao"
df_ordenado = df_media_acumulado_bairro.sort_values(by="media_acumulado", ascending=False).head(15)

# Criando o gráfico de ranking
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x="estacao", y="media_acumulado", data=df_ordenado, palette="plasma", ci=None)
plt.xlabel("")
plt.ylabel("Quantidade de Chuva(mm)")
plt.title("Ranking dos bairros que mais chovem no Rio", color="DarkBlue")

# Girando os rótulos do eixo x
barplot.set_xticklabels(barplot.get_xticklabels(), rotation=45, horizontalalignment="right")

# Evita sobreposição de elementos
plt.tight_layout()  

plt.show()


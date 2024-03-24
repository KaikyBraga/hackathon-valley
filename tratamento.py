from dataframes import *

# Exclusão de colunas desnecessárias
# DF'S DataRio 
df_bairro.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_bairro.to_csv("dados/datario/bairro.csv", index=False)
df_chamado.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_chamado.to_csv("dados/datario/chamado.csv", index=False)

# DF'S RJ-cor 
df_estacoes_alertario.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_estacoes_alertario.to_csv("dados/rj-cor/estacoes_alertario.csv", index=False)
df_estacoes_cemaden.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_estacoes_cemaden.to_csv("dados/rj-cor/estacoes_cemaden.csv", index=False)
df_estacoes_inea.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_estacoes_inea.to_csv("dados/rj-cor/estacoes_inea.csv", index=False)
df_estacoes_websirene.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_estacoes_websirene.to_csv("dados/rj-cor/estacoes_websirene.csv", index=False)
df_h3_grid_res8.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_h3_grid_res8.to_csv("dados/rj-cor/h3_grid_res8.csv", index=False)
df_lamina_agua_inea.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_lamina_agua_inea.to_csv("dados/rj-cor/lamina_agua_inea.csv", index=False)
df_taxa_precipitacao_alertario_5min.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_taxa_precipitacao_alertario_5min.to_csv("dados/rj-cor/taxa_precipitacao_alertario_5min.csv", index=False)
df_taxa_precipitacao_cemaden.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_taxa_precipitacao_cemaden.to_csv("dados/rj-cor/taxa_precipitacao_cemaden.csv", index=False)
df_taxa_precipitacao_guaratiba.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_taxa_precipitacao_guaratiba.to_csv("dados/rj-cor/taxa_precipitacao_guaratiba.csv", index=False)
df_taxa_precipitacao_inea.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_taxa_precipitacao_inea.to_csv("dados/rj-cor/taxa_precipitacao_inea.csv", index=False)
df_taxa_precipitacao_websirene.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_taxa_precipitacao_websirene.to_csv("dados/rj-cor/taxa_precipitacao_websirene.csv", index=False)

# DF'S RJ-rioaguas
df_nivel_lamina_agua_via.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_nivel_lamina_agua_via.to_csv("dados/rj-rioaguas/nivel_lamina_agua_via.csv", index=False)
df_ponto_supervisionado_alagamento.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_ponto_supervisionado_alagamento.to_csv("dados/rj-rioaguas/ponto_supervisionado_alagamento.csv", index=False)
df_sub_bacias.drop(['Unnamed: 0'], axis='columns', inplace=True)
df_sub_bacias.to_csv("dados/rj-rioaguas/sub_bacias.csv", index=False)
import pandas as pd

# DF'S DataRio 
df_bairro = pd.read_csv("dados/datario/bairro.csv")
df_chamado = pd.read_csv("dados/datario/chamado.csv")

# DF'S RJ-cor 
df_estacoes_alertario = pd.read_csv("dados/rj-cor/estacoes_alertario.csv")
df_estacoes_cemaden = pd.read_csv("dados/rj-cor/estacoes_cemaden.csv")
df_estacoes_inea = pd.read_csv("dados/rj-cor/estacoes_inea.csv")
df_estacoes_websirene = pd.read_csv("dados/rj-cor/estacoes_websirene.csv")
df_h3_grid_res8 = pd.read_csv("dados/rj-cor/h3_grid_res8.csv")
df_lamina_agua_inea = pd.read_csv("dados/rj-cor/lamina_agua_inea.csv")
df_taxa_precipitacao_alertario_5min = pd.read_csv("dados/rj-cor/taxa_precipitacao_alertario_5min.csv")
df_taxa_precipitacao_cemaden = pd.read_csv("dados/rj-cor/taxa_precipitacao_cemaden.csv")
df_taxa_precipitacao_guaratiba = pd.read_csv("dados/rj-cor/taxa_precipitacao_guaratiba.csv")
df_taxa_precipitacao_inea = pd.read_csv("dados/rj-cor/taxa_precipitacao_inea.csv")
df_taxa_precipitacao_websirene = pd.read_csv("dados/rj-cor/taxa_precipitacao_websirene.csv")

# DF'S RJ-rioaguas
df_nivel_lamina_agua_via= pd.read_csv("dados/rj-rioaguas/nivel_lamina_agua_via.csv")
df_ponto_supervisionado_alagamento = pd.read_csv("dados/rj-rioaguas/ponto_supervisionado_alagamento.csv")
df_sub_bacias = pd.read_csv("dados/rj-rioaguas/sub_bacias.csv")

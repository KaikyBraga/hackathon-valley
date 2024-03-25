import base64
import streamlit as st

dicionario_arquivos = {"dados/datario/bairro.csv":"bairro",
                       "dados/rj-cor/estacoes_alertario.csv":"estacoes_alertario",
                       "dados/rj-cor/estacoes_cemaden.csv":"estacoes_cemaden",
                       "dados/rj-cor/estacoes_inea.csv":"estacoes_inea",
                       "dados/rj-cor/estacoes_websirene.csv":"estacoes_websirene",
                       "dados/rj-cor/h3_grid_res8.csv":"h3_grid_res8",
                       "dados/rj-cor/lamina_agua_inea.csv":"lamina_agua_inea",
                       "dados/rj-cor/ocorrencias.csv":"ocorrencias",
                       "dados/rj-cor/procedimento_operacional_padrao.csv":"procedimento_operacional_padrao",
                       "dados/rj-cor/taxa_precipitacao_alertario_5min.csv":"taxa_precipitacao_alertario_5min",
                       "dados/rj-cor/taxa_precipitacao_cemaden.csv":"taxa_precipitacao_cemaden",
                       "dados/rj-cor/taxa_precipitacao_websirene.csv":"taxa_precipitacao_websirene",
                       "dados/rj-rioaguas/nivel_lamina_agua_via.csv":"nivel_lamina_agua_via",
                       "dados/rj-rioaguas/nivel_reservatorio.csv":"nivel_reservatorio",
                       "dados/rj-rioaguas/ponto_supervisionado_alagamento.csv":"ponto_supervisionado_alagamento",
                       "dados/rj-rioaguas/sub_bacias.csv":"sub_bacias"
                       }

st.set_page_config(page_title="Download dos Dados")

#with open("styles.css") as f:
    #st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  

# Função para fazer o download do arquivo CSV
def download_arquivo_csv(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        csv = file.read()
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{caminho_arquivo}" style="border: 2px solid #007BFF; color: white; background-color: #007BFF; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block;">Clique aqui para baixar</a>'
    return href

with st.container():
    st.title("Download dos Dados")
    st.write("Clique no botão abaixo para fazer o download dos dados: ")

with st.container():
    # Botão para baixar o arquivo CSV

    caminho_arquivo = st.selectbox("Selecione o reservatório:", dicionario_arquivos.keys(), format_func=lambda x: dicionario_arquivos[x])
    st.markdown(download_arquivo_csv(caminho_arquivo), unsafe_allow_html=True)     
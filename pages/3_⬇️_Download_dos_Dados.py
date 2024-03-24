import base64
import streamlit as st

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
    st.title("Download dos Dados em tempo real")
    st.write("Clique no botão abaixo para fazer o download dos dados: ")

with st.container():
    # Botão para baixar o arquivo CSV
    st.markdown(download_arquivo_csv("dados/datario/bairro.csv"), unsafe_allow_html=True)     
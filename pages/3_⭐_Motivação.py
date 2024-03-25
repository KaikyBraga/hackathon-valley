import streamlit as st
from PIL import Image, ImageDraw, ImageOps

st.set_page_config(page_title="Motivação")

#with open("styles.css") as f:
    #st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  

st.title("Motivação")

# Carregar as imagens
kaiky = Image.open("imagens/kaiky.jpg")
leonardo = Image.open("imagens/leonardo.jpg")
samuel = Image.open("imagens/samuel.jpg")
#luciano = Image.open("imagens/lucinano.jpg")

# Tamanho desejado para as imagens redondas
tamanho_redondo = (1000, 1000)

# Criar máscaras circulares
def aplicar_mascara(imagem, mascara):
    imagem = ImageOps.fit(imagem, mascara.size, centering=(0.5, 0.5))
    imagem.putalpha(mascara)
    return imagem

mascara = Image.new("L", tamanho_redondo, 0)
draw = ImageDraw.Draw(mascara)
draw.ellipse((0, 0) + tamanho_redondo, fill=255)

kaiky = aplicar_mascara(kaiky, mascara)
leonardo = aplicar_mascara(leonardo, mascara)
samuel = aplicar_mascara(samuel, mascara)

# Adicionar margens transparentes às imagens para criar espaço entre elas
kaiky = ImageOps.expand(kaiky, border=30, fill=None)
leonardo = ImageOps.expand(leonardo, border=30, fill=None)
samuel = ImageOps.expand(samuel, border=30, fill=None)

# Exibir imagens redondas lado a lado com espaçamento e nomes abaixo delas
st.image([kaiky, leonardo, samuel], width=230, caption=["Kaiky Braga", "Leonardo Alexandre", "Samuel Lima"])

st.write("Olá! Somos alunos do 3° Período de Ciência de Dados da Escola de Matemática Aplicada da Fundação Getúlio Vargas, iniciamos este projeto com o objetivo de auxiliar a população civil sobre as chuvas do Rio de Janeiro.")

URL_STRING = "https://github.com/LuuSamp/hackathon-valley.git"

st.markdown(
    f'<a href="{URL_STRING}" style="display: inline-block; padding: 12px 20px; background-color: #026773; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Clique para acessar o projeto no GitHub 💻</a>',
    unsafe_allow_html=True
)
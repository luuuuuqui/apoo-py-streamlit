# app.py

import streamlit as st
# Importamos as funções que criamos no nosso módulo de banco de dados
from PostDAO import fetch_all_posts, add_post

# --- CONFIGURAÇÃO DO CACHE E FUNÇÕES DE DADOS DA APLICAÇÃO ---

# A responsabilidade do cache fica aqui, na camada da aplicação!
# Esta função "envolve" a nossa função de busca de dados com o cache do Streamlit.
@st.cache_data
def load_posts():
    """Carrega os posts usando a função do módulo de banco de dados."""
    return fetch_all_posts()

# --- INTERFACE DA APLICAÇÃO ---

st.set_page_config(page_title="Blog Refatorado", layout="centered")

st.title("📝 Meu Blog (Código Refatorado)")

# --- FORMULÁRIO PARA NOVO POST ---

st.header("Escrever Novo Post")
with st.form(key="new_post_form", clear_on_submit=True):
    title = st.text_input("Título do Post")
    content = st.text_area("Conteúdo")
    submit_button = st.form_submit_button(label="Publicar")

# Se o formulário for enviado, chame a função de adicionar post do nosso módulo.
if submit_button:
    if not title or not content:
        st.error("Por favor, preencha o título e o conteúdo do post.")
    else:
        add_post(title, content) # <-- Chamando a função importada
        st.success("Post publicado com sucesso!")
        # Limpa o cache para garantir que a lista de posts seja atualizada.
        st.cache_data.clear()
        # O rerun continua aqui para forçar a atualização da tela.
        st.rerun()

st.markdown("---")

# --- EXIBIÇÃO DOS POSTS ---

st.header("Posts Recentes")
all_posts = load_posts() # <-- Usando nossa função cacheada para carregar os dados

if all_posts.empty:
    st.info("Ainda não há posts no mural.")
else:
    for index, post in all_posts.iterrows():
        st.subheader(post['title'])
        st.write(f"_{post['created_at']}_")
        st.write(post['content'])
        st.markdown("---")
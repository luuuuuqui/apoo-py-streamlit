# app.py
import streamlit as st
from controller import PostController # A View SÓ conversa com o Controller

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Blog MVC", layout="centered")
st.title("📝 Meu Blog com Arquitetura de 4 Camadas")

# --- FORMULÁRIO PARA NOVO POST ---
st.header("Escrever Novo Post")
with st.form(key="new_post_form", clear_on_submit=True):
    title = st.text_input("Título do Post")
    content = st.text_area("Conteúdo")
    submit_button = st.form_submit_button(label="Publicar")

# Ação de submit é delegada para o Controller
if submit_button:
    PostController.add_new_post(title, content)
    st.rerun() # O rerun ainda é útil para atualizar a tela imediatamente

st.markdown("---")

# --- EXIBIÇÃO DOS POSTS ---
st.header("Posts Recentes")

# Busca os posts através do Controller
all_posts = PostController.get_all_posts()

if not all_posts:
    st.info("Ainda não há posts no mural.")
else:
    # A view agora recebe uma lista de objetos Post, muito mais limpo de trabalhar
    for post in all_posts:
        st.subheader(post.title)
        st.caption(f"Publicado em: {post.created_at}")
        st.write(post.content)
        st.markdown("---")
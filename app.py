# app.py
import streamlit as st
import sqlite3
import pandas as pd

# --- CONFIGURAÇÃO DA CONEXÃO E CACHE ---

# O decorador @st.cache_data é crucial para o desempenho.
# Ele armazena o resultado da função em cache. A consulta ao banco
# só será executada novamente se o código da função mudar.
@st.cache_data
def fetch_all_posts():
    """Busca todos os posts do banco de dados."""
    conn = sqlite3.connect('meu_blog.db')
    # O resultado de uma consulta SELECT pode ser facilmente lido pelo pandas
    df = pd.read_sql_query("SELECT * FROM posts ORDER BY created_at DESC", conn)
    conn.close()
    return df

# --- INTERFACE DA APLICAÇÃO ---

st.set_page_config(page_title="Blog com SQLite", layout="centered")

st.title("📝 Meu Blog com Streamlit e SQLite")

# Busca os dados usando a função cacheada
all_posts = fetch_all_posts()

st.header("Posts Recentes")

# Se não houver posts, mostre uma mensagem
if all_posts.empty:
    st.info("Ainda não há posts no mural. Adicione um novo post abaixo!")
else:
    # Itera sobre cada linha do DataFrame para exibir os posts
    for index, post in all_posts.iterrows():
        st.subheader(post['title'])
        st.write(f"_{post['created_at']}_") # Formata a data em itálico
        st.write(post['content'])
        st.markdown("---")
        
# (código anterior aqui...)

# --- FORMULÁRIO PARA NOVO POST ---

st.header("Escrever Novo Post")

# st.form cria um formulário que agrupa elementos
with st.form(key="new_post_form", clear_on_submit=True):
    title = st.text_input("Título do Post")
    content = st.text_area("Conteúdo")
    
    # st.form_submit_button para enviar o formulário
    submit_button = st.form_submit_button(label="Publicar")

# --- LÓGICA DE INSERÇÃO ---

def add_post(title, content):
    """Adiciona um novo post ao banco de dados."""
    conn = sqlite3.connect('meu_blog.db')
    cursor = conn.cursor()
    # FORMA SEGURA: Usando placeholders (?) para evitar SQL Injection
    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

if submit_button:
    # Validação simples
    if not title or not content:
        st.error("Por favor, preencha o título e o conteúdo do post.")
    else:
        add_post(title, content)
        st.success("Post publicado com sucesso!")
        # Limpa o cache para que a lista de posts seja atualizada
        st.cache_data.clear()
        # Força o rerodamento do script para exibir o novo post imediatamente
        st.rerun()
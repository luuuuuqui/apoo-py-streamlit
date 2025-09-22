# controller.py
from typing import List
import streamlit as st  # O cache é uma lógica de aplicação, então fica aqui.

# Importa o modelo e as funções do DAL
from models import Post
import PostDAO as db

class PostController:
    """
    Classe controladora para gerenciar as operações de posts.
    Ela conecta a View (app.py) com o Model (Post) e o DAL (PostDAO.py).
    """

    @staticmethod
    @st.cache_data # O cache é movido para o controller!
    def get_all_posts() -> List[Post]:
        """Busca todos os posts através da camada DAL."""
        return db.fetch_all_posts()

    @staticmethod
    def add_new_post(title: str, content: str):
        """
        Recebe dados brutos da View, cria um objeto Post e o envia para o DAL.
        """
        # Aqui você poderia adicionar lógicas de negócio, como validação.
        if len(title) < 5:
            st.error("O título deve ter pelo menos 5 caracteres.")
            return

        # 1. Cria um objeto do modelo
        new_post = Post(title=title, content=content)
        
        # 2. Passa o objeto para a camada de acesso a dados
        db.add_post(new_post)
        
        # 3. Limpa o cache para que a lista seja atualizada na próxima leitura
        st.cache_data.clear()
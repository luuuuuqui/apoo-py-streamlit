# database.py
from typing import List
import sqlite3
import pandas as pd
from model import Post  # Importa a classe Post do nosso modelo

class PostDAO:
    """
    Data Access Layer (DAL) para gerenciar operações de banco de dados relacionadas a posts.
    """
    
    def __init__(self, db_name: str = 'meu_blog.db'):
        # Nome do arquivo do banco de dados SQLite
        self.DB_NAME = db_name
    
    def get_db_connection(self):
        """Cria e retorna uma conexão com o banco de dados."""
        conn = sqlite3.connect(self.DB_NAME)
        conn.row_factory = sqlite3.Row # Para acessar as colunas por nome
        return conn

    def add_post(self, post: Post):
        """Adiciona um objeto Post ao banco de dados."""
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (post.title, post.content)
        )
        conn.commit()
        conn.close()

    def fetch_all_posts(self) -> List[Post]:
        """Busca todos os posts e retorna uma lista de objetos Post."""
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
        
        rows = cursor.fetchall()
        conn.close()
        
        # Transforma cada linha do resultado do banco em um objeto Post
        return [
            Post(
                id=row['id'], 
                title=row['title'], 
                content=row['content'], 
                created_at=row['created_at']
            ) for row in rows
        ]

        

  
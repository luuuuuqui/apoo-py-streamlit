# database.py

import sqlite3
import pandas as pd
from models import Post  # Importa a classe Post do nosso modelo


# Nome do arquivo do banco de dados como uma constante
DB_NAME = 'meu_blog.db'

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def add_post(post: Post):
    """Adiciona um objeto Post ao banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        (post.title, post.content)
    )
    conn.commit()
    conn.close()

def fetch_all_posts() -> List[Post]:
    """Busca todos os posts e retorna uma lista de objetos Post."""
    conn = get_db_connection()
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

# Opcional: Uma função para inicializar o DB, se necessário.
def init_db():
    """Inicializa o banco de dados e cria a tabela se ela não existir."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    conn.close()

# Se você executar este arquivo diretamente, ele inicializará o banco.
if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado.")
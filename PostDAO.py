# database.py

import sqlite3
import pandas as pd

# Nome do arquivo do banco de dados como uma constante
DB_NAME = 'meu_blog.db'

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def add_post(title, content):
    """Adiciona um novo post ao banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

def fetch_all_posts():
    """
    Busca todos os posts do banco de dados e os retorna como um DataFrame do Pandas.
    Note que esta função não tem NENHUM código do Streamlit.
    A responsabilidade de cache fica na camada da aplicação (app.py).
    """
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM posts ORDER BY created_at DESC", conn)
    conn.close()
    return df

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
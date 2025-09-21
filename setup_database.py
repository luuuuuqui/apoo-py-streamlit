# setup_database.py
import sqlite3

# Conecta ao banco de dados (se não existir, ele será criado)
conn = sqlite3.connect('meu_blog.db')

# Cria um "cursor" que é usado para executar comandos SQL
cursor = conn.cursor()

# Comando SQL para criar uma tabela chamada 'posts'
# IF NOT EXISTS previne erros se o script for executado múltiplas vezes
cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Salva as alterações (commit) e fecha a conexão
conn.commit()
conn.close()

print("Banco de dados e tabela 'posts' criados com sucesso!")
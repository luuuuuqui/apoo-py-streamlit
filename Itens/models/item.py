import sqlite3


class Item:
    def __init__(self, id: int, descricao: str, quantidade: str):
        self.id = id
        self.descricao = descricao
        self.quantidade = quantidade

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "descricao": self.descricao,
            "quantidade": self.quantidade
        }

    def __str__(self) -> str:
        return f"{self.id} - {self.descricao} - {self.quantidade}"

class ItemDAO:
    DB_NAME = "itens.db"

    @staticmethod
    def criar_tabela():
        conn = sqlite3.connect(ItemDAO.DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                quantidade TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def inserir(item: Item) -> None:
        ItemDAO.criar_tabela()
        conn = sqlite3.connect(ItemDAO.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO itens (descricao, quantidade) VALUES (?, ?)",
                       (item.descricao, item.quantidade))
        conn.commit()
        conn.close()

    @staticmethod
    def listar() -> list:
        ItemDAO.criar_tabela()
        conn = sqlite3.connect(ItemDAO.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, quantidade FROM itens")
        rows = cursor.fetchall()
        conn.close()
        return [Item(id=row[0], descricao=row[1], quantidade=row[2]) for row in rows]

    @staticmethod
    def listar_id(id) -> object:
        ItemDAO.criar_tabela()
        conn = sqlite3.connect(ItemDAO.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, quantidade FROM itens WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Item(id=row[0], descricao=row[1], quantidade=row[2])
        return None

    @staticmethod
    def atualizar(item: Item) -> None:
        ItemDAO.criar_tabela()
        conn = sqlite3.connect(ItemDAO.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("UPDATE itens SET descricao = ?, quantidade = ? WHERE id = ?",
                       (item.descricao, item.quantidade, item.id))
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(id) -> None:
        ItemDAO.criar_tabela()
        conn = sqlite3.connect(ItemDAO.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM itens WHERE id = ?", (id,))
        conn.commit()
        conn.close()
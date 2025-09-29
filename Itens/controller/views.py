from models.item import Item, ItemDAO

class View:
    # Itens 
    @staticmethod
    def item_inserir(descricao, quantidade):
        item = Item(0, descricao, quantidade)
        ItemDAO.inserir(item)

    @staticmethod
    def item_listar():
        return ItemDAO.listar()

    @staticmethod
    def item_listar_id(id):
        return ItemDAO.listar_id(id)

    @staticmethod
    def item_atualizar(id, descricao, quantidade):
        item = Item(id, descricao, quantidade)
        ItemDAO.atualizar(item)

    @staticmethod
    def item_excluir(id):
        ItemDAO.excluir(id)
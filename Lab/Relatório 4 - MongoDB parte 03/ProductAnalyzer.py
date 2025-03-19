from database import Database
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, db: Database):
        self.db = db

    # 1. Retorne o total de vendas por dia
    def total_vendas_por_dia(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id": 1}}
        ])
        writeAJson(result, "Total de vendas por dia")
        return result

    # 2. Retorne o produto mais vendido em todas as compras
    def produto_mais_vendido(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Produto mais vendido")
        return result

    # 3. Encontre o cliente que mais gastou em uma única compra
    def cliente_que_mais_gastou(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "compra_id": "$compra_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Cliente que mais gastou")
        return result

    # 4. Liste todos os produtos que tiveram uma quantidade vendida acima de 1 unidade
    def produtos_com_mais_de_uma_unidade_vendida(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_total": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade_total": {"$gt": 1}}},
            {"$sort": {"quantidade_total": -1}}
        ])
        writeAJson(result, "Produtos com mais de uma unidade vendida")
        return result

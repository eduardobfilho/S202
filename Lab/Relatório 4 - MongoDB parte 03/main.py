from database import Database
from ProductAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")

analyzer = ProductAnalyzer(db)

analyzer.total_vendas_por_dia()
analyzer.produto_mais_vendido()
analyzer.cliente_que_mais_gastou()
analyzer.produtos_com_mais_de_uma_unidade_vendida()
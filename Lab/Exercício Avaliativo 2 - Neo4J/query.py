from database import Database

db = Database("bolt://localhost:7687", "neo4j", "neo4jtest")

#Questão 1
query1 = """
MATCH (t:Teacher {name: 'Renzo'})
RETURN t.ano_nasc, t.cpf
"""
query2 = """
MATCH (t:Teacher)
WHERE t.name STARTS WITH 'M'
RETURN t.name, t.cpf
"""
query3 = """
MATCH (c:City)
RETURN c.name
"""
query4 = """
MATCH (s:School)
WHERE s.number >= 150 AND s.number <= 550
RETURN s.name, s.address, s.number
"""

#Questão 2
query5 = """
MATCH (t:Teacher)
RETURN max(t.ano_nasc) AS mais_jovem, min(t.ano_nasc) AS mais_velho
"""

query6 = """
MATCH (c:City)
RETURN avg(c.population) AS media_habitantes
"""

query7 = """
MATCH (c:City {cep: '37540-000'})
RETURN replace(c.name, 'a', 'A') AS nome_modificado
"""

query8 = """
MATCH (t:Teacher)
RETURN substring(t.name, 2) AS nome_a_partir_da_3_letra
"""
if __name__ == "__main__":
    queries = [query1, query2, query3, query4, query5, query6, query7, query8]
    for i, q in enumerate(queries, start=1):
        print(f"\n--- Resultado Query {i} ---")
        result = db.execute_query(q)
        for r in result:
            print(r)

    db.close()

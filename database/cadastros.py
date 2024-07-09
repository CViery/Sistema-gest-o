import sqlite3
import threading

class CadastrosDB:
    def __init__(self):
        self.local = threading.local()

    def get_conn(self):
        if not hasattr(self.local, 'conn'):
            self.local.conn = sqlite3.connect('database.db')
        return self.local.conn

    def cadastrar_produto(self, dados):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            id = dados["id"]
            codigo = dados["codigo"]
            nome = dados["nome"]
            categoria = dados["categoria"]
            valor = dados["valor_compra"]
            estoque_inicial = dados["estoque_inicial"]
            estoque_min = dados["estoque_min"]
            query = "INSERT INTO produtos VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (id, codigo, nome, categoria, valor, estoque_inicial, estoque_min))
            conn.commit()
            print("Salvo")
        except Exception as e:
            print(e)
        finally:
            cursor.close()
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

    def cadastrar_funcionario(self, dados):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            id = dados["id"]
            nome = dados["nome"]
            email = dados["email"]
            senha = dados["senha"]
            query = "INSERT INTO funcionarios VALUES (?, ?, ?, ?)"
            cursor.execute(query, (id, nome, email, senha))
            conn.commit()
            print("Salvo")
        except Exception as e:
            print(e)
        finally:
            cursor.close()
    
    def cadastrar_categorias(self, dados):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            id = dados["id"]
            nome = dados["categoria"]
            query = "INSERT INTO categorias VALUES (?, ?)"
            cursor.execute(query, (id, nome))
            conn.commit()
            print("Salvo")
        except Exception as e:
            print(e)
        finally:
            cursor.close()
    
    def cadastrar_clientes(self, dados):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            nome = dados["nome"]
            veiculo = dados["veiculo"]
            placa = dados["placa"]
            query = "INSERT INTO clientes VALUES (?, ?, ?)"
            cursor.execute(query, (placa, veiculo, nome))
            conn.commit()
            print("Salvo")
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def cadastrar_fornecedor(self, dados):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            cnpj = dados["cnpj"]
            razao_social = dados["razao_social"]
            endereco = dados["endereco"]
            email = dados["email"]
            telefone = dados['telefone']
            query = "INSERT INTO fornecedores VALUES (?, ?, ?, ?)"
            cursor.execute(query, (cnpj, razao_social, endereco, email, telefone))
            conn.commit()
            print("Salvo")
        except Exception as e:
            print(e)
        finally:
            cursor.close()
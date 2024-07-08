from database import cadastros

class Cadastros:
    def __init__(self) -> None:
        self.db = cadastros.CadastrosDB()
    def cadastrar_peca(self, dados):
        try:
            peca = {
                'id' : int(dados['id']),
                'codigo' : dados['codigo'],
                'nome' : dados['nome'],
                'categoria' : dados['categoria'],
                'valor_compra' : float(dados['valor_compra']),
                'estoque_inicial' : int(dados['estoque_inicial']),
                'estoque_min' : int(dados['estoque_min']),
                'descricao' : dados['descricao']
            }
            self.db.cadastrar_produto(peca)
        except Exception as e:
            print(e)
            raise e
    
    
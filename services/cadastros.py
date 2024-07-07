

class Cadastros:
    def __init__(self) -> None:
        pass
    def cadastrar_peca(self, dados):
        try:
            id = int(dados['id'])
            codigo = dados['codigo']
            nome = dados['nome']
            categoria = dados['categoria']
            valor_compra = float(dados['valor_compra'])
            estoque_inicial = int(dados['estoque_inicial'])
            estoque_min = int(dados['estoque_min'])
            descricao = dados['descricao']
            print(id,codigo,nome,categoria, valor_compra, estoque_inicial, estoque_min, descricao)
            """ self.db.cadastrar_pecas(id,codigo,nome,categoria, valor_compra, estoque_inicial, estoque_min, descricao) """
        except Exception as e:
            print(e)
            raise e
    
    
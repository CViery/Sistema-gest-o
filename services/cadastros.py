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
    
    def cadastrar_cliente(self, dados):
        try:
            #verificação se o cliente existe primeiro buscando pela placa
            person = {
                'nome' : str(dados["nome_completo"]),
                'veiculo' : str(dados["veiculo_modelo"]),
                'placa' : str(dados["placa"])
            }
            self.db.cadastrar_clientes(person)
        except Exception as e:
            print(e)
            raise e
        
    def cadastrar_fornecedor(self, dados):
        try:
            verificar = ''
            #verificar se o cnpj já está cadastrado antes de cadastrar um novo
            if verificar:
                print(f'CNPJ Cadastrado na empresa: {verificar[1]} ')
            else:
                empresa = {
                    'cnpj' : dados["cnpj"],
                    'razao_social' : dados["razao_social"],
                    'endereco' : dados["endereco"],
                    'email' : dados["email"],
                    'telefone' : dados['telefone']
                }
                self.db.cadastrar_fornecedor(empresa)
        except Exception as e:
            print(e)
            raise e
    
    def cadastrar_categoria(self, dados):
        try:
            verificar = ''

            if verificar:
                print('Categoria já está cadastrada')
            else:
                categoria = {
                    'id' : int(dados['id']),
                    'categoria': str(dados['categoria'])
                }
                self.db.cadastrar_categorias(categoria)
        except Exception as e:
            print(e)
            raise e
    
    def cadastrar_funcionario(self, dados):
        try:
            verificar = ''
            if verificar:
                print('já existe')
            else:
                senha = dados['senha']
                senha_hash = ''
                person = {
                    'id' : int(dados["id"]),
                    'nome' : dados["nome"],
                    'email' : dados["email"],
                    'senha' : senha_hash
                }
                self.db.cadastrar_funcionario(person)
        except Exception as e:
            print(e)
            raise e
from database import conection

class CadastrosDB : 
  def __init__(self) -> None:
    self.db = conection.Database()
    self.cursor = self.db.cursor
    
  def cadastrar_produto(self,dados):
    try:
      query="INSERT INTO produtos VALUES(?,?,?,?,?,?,?)"
      self.cursor.execute(query,(dados["id"],dados["codigo"],dados["nome"],dados["categoria"],dados["valor_compra"],dados["estoque_inicial"],dados["estoque_min"]))
      self.db.commit()
      print("Salvo")
    except Exception as e:
      print(e)
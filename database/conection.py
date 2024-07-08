import sqlite3


class Database: 
  def __init__(self) -> None:
    self.conn = sqlite3.connect('database.db')
    self.cursor = self.conn.cursor()
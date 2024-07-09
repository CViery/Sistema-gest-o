import sqlite3
import threading

class ConsultasDB:
    def __init__(self):
        self.local = threading.local()

    def get_conn(self):
        if not hasattr(self.local, 'conn'):
            self.local.conn = sqlite3.connect('database.db')
        return self.local.conn
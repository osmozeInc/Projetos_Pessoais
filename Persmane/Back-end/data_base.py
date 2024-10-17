import sqlite3


class Create_DB:
    def __init__(self):
        self.conexao = sqlite3.connect('data_base.db')
        self.Tabela_Lembretes()

    def Tabela_Lembretes(self):
        self.conexao.execute('CREATE TABLE IF NOT EXISTS lembretes(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, data TEXT, tempo TEXT, descricao TEXT)')
        self.conexao.commit()


class Update_DB:
    def __init__(self):
        self.conexao = sqlite3.connect('data_base.db')


class Read_DB:
    def __init__(self):
        self.conexao = sqlite3.connect('data_base.db')


class Delete_DB:
    def __init__(self):
        self.conexao = sqlite3.connect('data_base.db')
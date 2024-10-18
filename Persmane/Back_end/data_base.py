import sqlite3


class Create_DB:
    def __init__(self):
        self.conexao = sqlite3.connect('data_base.db')
        self.Tabela_Lembretes()

    def Tabela_Lembretes(self):
        self.conexao.execute('CREATE TABLE IF NOT EXISTS lembretes(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, data TEXT, hora TEXT, descricao TEXT, link TEXT)')
        self.conexao.commit()
        self.conexao.close()


class Update_DB:
    def __init__(self):
        self.conexao = sqlite3.connect('data_base.db')

    def Update_Lembrete(self, titulo, data, hora, descricao, link):
        self.conexao.execute('INSERT INTO lembretes (titulo, data, hora, descricao, link) VALUES (?, ?, ?, ?, ?)', (titulo, data, hora, descricao, link))
        self.conexao.commit()
        self.conexao.close()
        


class Read_DB:
    def __init__(self):
        self.conexao = sqlite3.connect('data_base.db')


class Delete_DB:
    def __init__(self):
        self.conexao = sqlite3.connect('data_base.db')
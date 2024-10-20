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
    def Update_Lembrete(self, titulo, data, hora, descricao, link):
        conexao = sqlite3.connect('data_base.db')
        conexao.execute('INSERT INTO lembretes (titulo, data, hora, descricao, link) VALUES (?, ?, ?, ?, ?)', (titulo, data, hora, descricao, link))
        conexao.commit()
        conexao.close()
        


class Read_DB:
    def Read_Reminder(self):
        self.conexao = sqlite3.connect('data_base.db')
        lembretes = self.conexao.execute('SELECT * FROM lembretes').fetchall()
        self.conexao.close()
        return lembretes


class Delete_DB:
    def  Delete_Reminder(self, id):
        self.conexao = sqlite3.connect('data_base.db')
        self.conexao.execute('DELETE FROM lembretes WHERE id = ?', (id,))
        self.conexao.commit()
        self.conexao.close()
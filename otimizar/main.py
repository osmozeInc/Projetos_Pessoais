import os
from datetime import datetime
import feedparser


def Menu():
    while True:
        os.system('cls')
        print('Menu:\n'
            '1 - Noticias\n'
            '2 - Palavras chaves\n'
            '3 - Sair\n')
        opcao = int(input('Escolha uma opcao: '))

        if opcao >= 1 and opcao <= 3:
            return opcao

class Noticias:
    def __init__(self):
        self.conjur = feedparser.parse("https://www.conjur.com.br/rss.xml")
        self.data = self.DataDaPesquisa()
        self.plataforma = self.PlataformaDePesquisa()

    def DataDaPesquisa(self):
        while True:
            os.system('cls')
            print('Data das noticias:\n'
                '1 - Hoje\n'
                '2 - Ontem\n'
                '3 - Semana\n'
                '4 - Mes\n'
                '5 - Qualquer\n')
            data = int(input('Escolha uma opcao: '))

            if data == 1:
                return datetime.today()
            elif data == 2:
                return datetime.today() - datetime.timedelta(days=1)

    def PlataformaDePesquisa(self):
        while True:
            os.system('cls')
            print('Plataforma:\n')
            plataforma = int(input('Escolha uma opcao: '))

    def ExibirNoticias(self):
        pass


def main():
    dir = Menu()

    if dir == 1:
        noticias = Noticias()
        noticias.ExibirNoticias()

    elif dir == 2:
        pass

    elif dir == 3:
        pass


if __name__ == '__main__':
    main()
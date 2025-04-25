import os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import feedparser
import requests


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
        self.noticia = 0
        self.PlataformaDePesquisa()            

    def PlataformaDePesquisa(self):
        while True:
            os.system('cls')
            print('Plataforma:\n'
                  '1 - Conjur\n')
            plataforma = int(input('Escolha uma opcao: '))

            if plataforma == 1:
                self.ExibirNoticiasConjur()
                break

    def ExibirNoticiasConjur(self):
        os.system('cls')
        for contador, noticia in enumerate(self.conjur.entries, 1):
            print(f"Noticia numero {contador}\n"
                    f"{noticia.title}\n"
                    f"{noticia.published}\n"
                    f"{"=" * 100}\n\n")
        
        print("digite 0 para voltar ao menu ou o numero da noticia para visualiza-la\n")
        opcao = int(input('Escolha uma opcao: '))

        if opcao == 0:
            return
        elif opcao >= 1 and opcao <= 10:
            self.noticia = opcao - 1
            self.ExibirNoticiasConjurResumida()

    def ExibirNoticiasConjurResumida(self):
        titulo = self.conjur.entries[self.noticia].title

        resumo_html = self.conjur.entries[self.noticia].description
        resumo = BeautifulSoup(resumo_html, 'html.parser').get_text()

        data_completa = self.conjur.entries[self.noticia].published_parsed
        data = f"{data_completa[2]:02}/{data_completa[1]:02}/{data_completa[0]:02}"

        link = self.conjur.entries[self.noticia].link

        os.system('cls')
        print(f"Titulo: {titulo}\n\n"
                f"Resumo: {resumo}\n\n"
                f"Data: {data}\n"
                f"{"=" * 100}\n\n"
                f"Link: {link}\n\n")
        
        print("1 - Ler matéria completa\n"
              "2 - Construir story\n"
              "3 - Rever noticias\n"
              "4 - Voltar ao menu\n")
        opcao = int(input('Escolha uma opcao: '))

        if opcao == 1:
            self.ExibirNoticiasConjurCompleta()
        elif opcao == 2:
            pass
        elif opcao == 3:
            self.ExibirNoticiasConjur()
        elif opcao == 4:
            return
        
    def ExibirNoticiasConjurCompleta(self):
        conteudo_html = requests.get(self.conjur.entries[self.noticia].link).text
        
        conteudo_completo = BeautifulSoup(conteudo_html, 'html.parser')
        conteudo_corpo = conteudo_completo.find('div', class_='the_content')

        os.system('cls')  # ou 'clear' no Linux/macOS

        elementos = conteudo_corpo.find_all(['p', 'h2'])

        for elemento in elementos:
            texto = elemento.get_text(strip=True)
            if texto:
                print(texto, "\n")



def main():
    while True:
        dir = Menu()

        if dir == 1:
            noticias = Noticias()

        elif dir == 2:
            pass

        elif dir == 3:
            break


if __name__ == '__main__':
    main()

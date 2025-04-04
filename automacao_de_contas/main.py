import csv
import os
import time
import random
import openai
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Menu(arq):
    input_menu = int(input("Ambiente do automatizador:\n"
            "1 - Contas\n"
            "2 - Navegador\n"
            "3 - (teste) receber valores de login\n"
            "9 - Sair\n> "))
    return input_menu
       

class ManipularArquivo():
    def __init__(self):
        self.nome_arquivo = 'contas.csv'

    def ArquivosCSV(self):
        tarefa = 0
        while tarefa < 1 or tarefa > 3:

            os.system("cls")
            tarefa = int(input("Escolha o que fazer:\n"
                               "1 - Consultar tabela de contas\n"
                               "2 - Consultar tabela de chaves da openai\n"
                               "3 - Cancelar\n> "))
            
        if tarefa == 1:
            self.TabelaDeContas()
        elif tarefa == 2:
            self.TabelaDeChavesDaOpenai()
    
    def TabelaDeContas(self):
        with open(self.nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            
            os.system("cls")
            print(f"{"Tabela de Contas":^100}"
                  f"\n{"-" * 100}")

            for linha in leitor:
                print(f"|{linha[0]:^6}|"
                      f"{linha[1]:^25}|"
                      f"{linha[2]:^15}|"
                      f"{linha[3]:^15}|"
                      f"{linha[4]:^17}|"
                      f"{linha[5]:^15}|"
                      f"\n{"-" * 100}")

    def TabelaDeChavesDaOpenai(self):
        with open('openai_keys.csv', 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            
            os.system("cls")
            print(f"{"Tabela de Chaves da Openai"}"
                  f"\n{"-" * 34}")

            for contador, linha in enumerate(leitor, 1):

                if contador == 1:
                    print(f"|{linha[0]:^6}|"
                          f"{linha[1]:^25}|")
                else:
                    print(f"{"-" * 34}\n"
                          f"|{linha[0]:^6}|"
                          f"{linha[1]:^25}|"
                          f"\n{"-" * 34}\n"
                          f" Key:   {linha[2]}\n")


    def ValoresDeLogin(self):
        with open(self.nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = list(csv.reader(arquivo))[1:]
            random.shuffle(linhas)

            return linhas[0][1], linhas[0][2]

    def ValoresDeChaves(self):
        with open('openai_keys.csv', 'r', encoding='utf-8') as arquivo:
            linhas = list(csv.reader(arquivo))[1:]
            random.shuffle(linhas)

            return linhas[0][0], linhas[0][2]
        

class ManipularNavegador():
    def __init__(self):
        self.edge_options = Options()
        self.edge_options.add_argument("--inprivate")

    def UsarNavegador(self):
        tarefa = self.DefinirTarefa()

        if self.tarefa == 1:
            self.ChatGPT()
        elif self.tarefa == 2:
            self.Gmail()
        elif self.tarefa == 4: 
            return

    def AbrirNavegador(self):
        self.navegador = webdriver.Edge()

    def DefinirTarefa(self):
        tarefa = 0
        while tarefa < 1 or tarefa > 4:
            
            os.system("cls")
            self.tarefa = int(input("Escolha uma tarefa:\n"
                           "1 - Usar o ChatGPT\n"
                           "2 - Acessar Gmail\n"
                           "3 - Excluir Conta\n"
                           "4 - Cancelar\n> "))
            
        return tarefa
            
    def FazerLogin(self):
        email, senha = arq.ValoresDeLogin()
        self.navegador.get("https://accounts.google.com/")

        WebDriverWait(self.navegador, 10).until(
            EC.presence_of_element_located((By.ID, "identifierId"))
        ).send_keys(email)

        self.navegador.find_element(By.ID, "identifierNext").click()

        WebDriverWait(self.navegador, 10).until(
            EC.presence_of_element_located((By.NAME, "Passwd"))
            ).send_keys(senha)
        
        self.navegador.find_element(By.ID, "passwordNext").click()

        input()

    def Gmail(self):
        self.navegador.get("https://mail.google.com/mail/u/0/#inbox")


arq = ManipularArquivo()
nav = ManipularNavegador()

while True:
    os.system("cls")

    input_menu = Menu(arq)

    if input_menu == 1:
       arq.ArquivosCSV()
       input("\nPressione qualquer tecla para voltar ao menu.")

    elif input_menu == 2:
        nav.UsarNavegador()

    elif input_menu == 3:
        email, senha = arq.ValoresDeLogin()
        print(email + "\n" + senha)
        break

    elif input_menu == 9:
        break
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
from selenium.webdriver.support.ui import Select


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
        
        input("\nPressione qualquer tecla para voltar ao menu.")
 
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


class ManipularNavegador():
    def __init__(self):
        pass
        self.edge_options = Options()
        self.edge_options.add_argument("--inprivate")
        self.edge_options.add_argument("--disable-blink-features=AutomationControlled")
        self.edge_options.add_argument("--start-maximized")


    def UsarNavegador(self):
        tarefa = self.DefinirTarefa()

        if tarefa == 1:
            self.CriarContaGoogle()
        elif tarefa == 2:
            self.CriarContaInstagram()
        elif tarefa == 4: 
            return

    def DefinirTarefa(self):
        tarefa = 0
        while tarefa < 1 or tarefa > 4:
            
            os.system("cls")
            tarefa = int(input("Escolha uma tarefa:\n"
                           "1 - Criar Conta Google\n"
                           "2 - Criar Conta Instagram\n"
                           "3 - Excluir Conta\n"
                           "4 - Cancelar\n> "))
            
        return tarefa
            
    def AbrirNavegador(self):
        self.navegador = webdriver.Edge()  

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

    def CriarContaGoogle(self):
        self.AbrirNavegador()
        self.navegador.get("https://accounts.google.com/signup")

        dados = {
            "nome": "felipe",
            "sobrenome": "costa",
            "dia": random.randint(1, 28),
            "mes": random.randint(1, 12),
            "ano": random.randint(1970, 2000),
            "gender": random.randint(1, 3),
            "senha": random.choice(["1234#drt", "erd34#d8", "cgd435%8", "145gty*g", "emmadr45$"]),
        }

        def Passo1(): # nome
            time.sleep(random.uniform(0, 3))
            WebDriverWait(self.navegador, 10).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )

            self.navegador.find_element(By.NAME, "firstName").send_keys(dados["nome"])
            self.navegador.find_element(By.NAME, "lastName").send_keys(dados["sobrenome"])
            self.navegador.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()

        def Passo2(): # data
            time.sleep(random.uniform(0, 3))
            WebDriverWait(self.navegador, 10).until(
                EC.presence_of_element_located((By.NAME, "day"))
            )

            self.navegador.find_element(By.NAME, "day").send_keys(dados["dia"])
            select = Select(self.navegador.find_element(By.ID, "month"))
            select.select_by_value(f"{dados['mes']}")
            self.navegador.find_element(By.NAME, "year").send_keys(dados["ano"])   

            select = Select(self.navegador.find_element(By.ID, "gender"))
            select.select_by_value(f"{dados['gender']}")

            self.navegador.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()

        def Passo3(): # e-mail
            time.sleep(random.uniform(1, 3))
            WebDriverWait(self.navegador, 10).until(
                EC.presence_of_element_located((By.NAME, "Username"))
            )

            self.navegador.find_element(By.NAME, "Username").send_keys("Teste.345trt")
            self.navegador.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()

        def Passo4(): # senha
            time.sleep(random.uniform(1, 3))
            WebDriverWait(self.navegador, 10).until(
                EC.presence_of_element_located((By.NAME, "Passwd"))
            )

            self.navegador.find_element(By.NAME, "Passwd").send_keys(dados["senha"])
            self.navegador.find_element(By.NAME, "PasswdAgain").send_keys(dados["senha"])
            self.navegador.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()

        def Passo5(): # numero
            time.sleep(random.uniform(1, 3))
            WebDriverWait(self.navegador, 10).until(
                EC.presence_of_element_located((By.ID, "phoneNumberID"))
            )

            self.navegador.find_element(By.ID, "phoneNumberID").send_keys(f"889{random.randint(90000000, 99999999)}")


        Passo1()
        Passo2()
        Passo3()
        Passo4()

    def CriarContaInstagram(self):
        self.AbrirNavegador()
        self.navegador.get("https://www.instagram.com/")


        dados = {
            "nome": "felipe",
            "sobrenome": "costa",
            "dia": random.randint(1, 28),
            "mes": random.randint(1, 12),
            "ano": random.randint(1970, 2000),
            "gender": random.randint(1, 3),
            "senha": random.choice(["1234#drt", "erd34#d8", "cgd435%8", "145gty*g", "emmadr45$"]),
        }





arq = ManipularArquivo()
nav = ManipularNavegador()

while True:
    os.system("cls")

    input_menu = Menu(arq)

    if input_menu == 1:
       arq.ArquivosCSV()

    elif input_menu == 2:
        nav.UsarNavegador()

    elif input_menu == 4:
        valor = arq.ValoresDeChaves()
        print("Chave:", valor)

    elif input_menu == 9:
        break
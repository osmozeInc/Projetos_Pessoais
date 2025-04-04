import csv

with open('contas.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
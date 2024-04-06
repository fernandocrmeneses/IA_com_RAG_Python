import pandas as pd
import csv
import json

class Arquivo:
    def __init__(self, caminho, nome_arquivo):
        self.caminho = caminho
        self.nome_arquivo = nome_arquivo
    
    def ler_arquivo_CSV(self):
        arquivo_csv = pd.read_csv(f'{self.caminho}{self.nome_arquivo}.csv')
        return arquivo_csv.iterrows()
        
        
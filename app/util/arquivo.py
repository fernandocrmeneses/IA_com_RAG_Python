import pandas as pd
import csv
import json

class Arquivo:
    def __init__(self, caminho, nome_arquivo):
        self.caminho = caminho
        self.nome_arquivo = nome_arquivo
    
    def ler_arquivo_CSV(self, retorna_head = False):
        if(retorna_head):
            arquivo_csv = pd.read_csv(f'{self.caminho}{self.nome_arquivo}.csv', sep = ',')
            return arquivo_csv.head(len(arquivo_csv))
                   
    
        arquivo_csv = pd.read_csv(f'{self.caminho}{self.nome_arquivo}.csv')
        return arquivo_csv.iterrows()        
        
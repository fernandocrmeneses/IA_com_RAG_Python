import pandas as pd
import json

class Arquivo:
    def __init__(self, caminho, nome_arquivo):
        self.caminho = caminho
        self.nome_arquivo = nome_arquivo
    
    def ler_arquivo_CSV(self):
        arquivo_csv = pd.read_csv(f'{self.caminho}{self.nome_arquivo}.csv')
        lista = []
        for indice, linha in arquivo_csv.iterrows():
            lista.append(linha)
        
        return linha
        
        
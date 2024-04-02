import pandas as pd

class LerArquivos:
    def __init__(self, caminho, nomeArquivoCSV):
        self.caminho = caminho
        self.nomeArquivoCSV = nomeArquivoCSV
    
    def ObtemDadosDoCSV(self):
        arquivo_csv = pd.read_csv(f'{self.caminho}{self.nomeArquivoCSV}.csv')
        for valor in arquivo_csv:
            print(valor)
        
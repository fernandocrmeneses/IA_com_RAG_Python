from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score #avaliação do modelo
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score #métrica de avaliação
from sklearn.preprocessing import StandardScaler, MinMaxScaler #Feature Engineer
import matplotlib.pyplot as plt #gráficos
import seaborn as sns #gráficos
import numpy as np #transformação dos dados
import warnings #remoção de avisos
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class AnaliseTratamentoDados:
    def __init__(self) -> None:
        pass
    
    def execute_plot_dashed(self):
        pass
    
    def exibe_acuracia(self, y_teste, y_predito):
        print(accuracy_score(y_teste, y_predito))
        
    def exibe_describe_linhas_colunas(self, dados):
        print(dados.describe())
        print("**shape:**")
        print(dados.shape)
    
    def exibe_dados_nulos(self, dados):
        print(dados.isnull().sum())
        
    def exibe_correlacao_dados(self, dados_coeded):
        """
            Descrição:
                Esse metodo verifica e exibe a correlação dos dados que foram aplicadas as tecnicas de 'one hot encoding'.
            Args:
                dados_coeded type(DataFrame): Um DataFrame onde já houve a aplicação das tecnicas de modelo de classificação (one hot encoding).
        """
        print("correlação")
        correlation_matrix = dados_coeded.corr().round(2)
        print("correlação 1")
        fig, ax = plt.subplots(figsize=(8,8))    
        print("correlação 3")
        sns.heatmap(data=correlation_matrix, annot=True, linewidths=.5, ax=ax)
        print("correlação 4")
        plt.show()
        print("correlação 5 fim")
        
    def exibe_outliers(self, dados, coluna, coluna_x = None, coluna_y = None):
        sns.boxplot(x = dados[coluna])
        
        if coluna_x != None:
            sns.boxplot( x = coluna_x)
        
        if coluna_y != None:
            sns.boxplot(y = coluna_y)
        
        plt.show()
        
    def exibe_historico_barras(selft, dados, coluna_x = None, coluna_y = None):
        sns.histplot(data = dados)
        
        if(coluna_x != None):
            sns.histplot(data = dados,x = coluna_x)
        
        if(coluna_y != None):
            sns.histplot(data = dados, y = coluna_y)
        
        plt.show()
        
        
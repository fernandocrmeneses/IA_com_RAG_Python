from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score #avaliação do modelo
from sklearn.metrics import accuracy_score #métrica de avaliação
import matplotlib.pyplot as plt #gráficos
import seaborn as sns #gráficos
import numpy as np #transformação dos dados
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class ModelosDeClassificacao:
       
    def __init__(self):
        self.x = None
        self.y = None
        
    def define_variavel_target(self, dados, target):
        set(dados[target])
    
    def define_variavel_target_y(self, dados, target):
         self.y = dados[target]
         
    def define_lista_variaveis_x(self,dados, colunas):
        self.x = dados[colunas]
        
    def trata_dados_ausentes(self, dados):
        if dados.isnull().sum().any():
            return dados.dropna()
        
    def trata_dado_numerico_nulo(self, dados, nome_coluna_numerica, valor_campo = 0):
            """
                Descrição:
                    Todo dado numerico, da coluna informada, que estiver nulo, será convertido para 0 por padrão. 
                    Ou convertido para o valor informado no parametro 'valor_campo'
                
                Args:
                    dados type(DataFrame): Um DataFrame que representa os dados provenientes da base de dados.
                    nome_coluna_numerica type(string): O nome da coluna que será alterado os valores nulos pelo valor do campo.
                    valor_campo type(int): O valor que será atribuido aos campos que estão com o valor nulo.
                
                Returns:
                    DataFrame: Retorna um DataFrame de dados tratados com os valores que antes eram nulos agora preenchidos.  
            """
                
            return dados[nome_coluna_numerica].fillna(value = valor_campo, inplace = True)
        
    def obtem_colunas_booleanas(self, dados):
        """
        Descrição: Obtem colunas com apenas dois valores como por exemplo: 'Sim','Não','Masculino','Feminino','Ativo','Inativo'.

        Args:
            dados (DataFrame): Um DataFrame que representa os dados provenientes da base de dados.

        Returns:
            (list of string): Retorna uma lista de strings com as colunas onde possuem apenas 2 valores.
        """
        colunas_booleanas = [coluna for coluna in dados.columns if len(dados[coluna].unique()) == 2]
        return colunas_booleanas
    
    def obtem_colunas_nao_booleanas(self, dados):
        """
        Descrição: Obtem colunas que não contém apenas dois valores.

        Args:
            dados (DataFrame): Um DataFrame que representa os dados provenientes da base de dados.

        Returns:
            (list of string): Retorna uma lista de strings com as colunas que possuem mais de 2 valores.
        """
        colunas_nao_booleanas = [coluna for coluna in dados.columns if len(dados[coluna].unique()) != 2]
        return colunas_nao_booleanas
    
    def aplica_tecnica_label_encoder(self, dados, colunas):
        """
            Descrição: 
                Geralmente a tecnica de label enconder é utilizada para colunas booleanas, 
                ou seja que possuem apenas 2 valores como por exemplo: 'Sim','Não','Masculino','Feminino','Ativo','Inativo'.
         
            Args:
                dados type(DataFrame): Um DataFrame que representa os dados provenientes da base de dados.
                colunas type(list of string): Uma lista de strings das colunas, que serão aplicadas o fit_transform/tecnica label encoder.
            
            Returns:
                DataFrame: Retorna um DataFrame de dados tratados com a aplicação da tecnica de one hot encoding.
        """
        
        label_enconder = LabelEncoder()
        for coluna in colunas:
            dados[coluna] = label_enconder.fit_transform(dados[coluna])
        return dados
        
    def aplica_one_hot_encoding(self, dados, colunas_aplicadas_one_hot, colunas_seram_apagadas = None, prefixo = "coluna_"):
        """
        Descrição: 
            O metodo/tenica one hot enconding, irá incluir o valor 1 onde obtiver um valor e nas demais colunas irá incluir 0.
        
        Args:
            dados type(DataFrame): Um DataFrame que representa os dados provenientes da base de dados.
            colunas_seram_apagadas type(list of string): Uma lista de strings das colunas que serão apagadas, devido a aplicação dos prefixos para facilitar a tecnica de one hot encoding.
            colunas_aplicadas_one_hot type(list of string): Uma lista de colunas que serão aplicados os prefixos para posteriormente aplicar a one hot encoding.
            prefixo type(string): O prefixo que será aplicado nas colunas dos dados.
        
        Returns:
            DataFrame: Retorna um DataFrame de dados tratados com a aplicação da tecnica de one hot encoding.
        """
        
        # prefixo_hsc_s = pd.get_dummies(dados['hsc_s'], prefix = str(prefixo))
        # prefixo_degree_t = pd.get_dummies(dados['degree_t'], prefix = str(prefixo))
        if colunas_seram_apagadas is None:
            colunas_seram_apagadas = []
        
        nomes_colunas_apagadas = []
        lista_concat = [dados]
        
        for col_one_hot_enconding in colunas_aplicadas_one_hot:
           lista_concat.append(pd.get_dummies(dados[col_one_hot_enconding], prefix = str(prefixo)))
            
        for coluna in colunas_seram_apagadas:
            nomes_colunas_apagadas.append(coluna)
        
        #dados_coeded = pd.concat([dados, prefixo_hsc_s, prefixo_degree_t], axis = 1)
        dados_coeded = pd.concat(lista_concat, axis = 1)
        
        if nomes_colunas_apagadas != None:
            dados_coeded.drop(nomes_colunas_apagadas, axis = 1, inplace = True)
        
        return dados_coeded
        
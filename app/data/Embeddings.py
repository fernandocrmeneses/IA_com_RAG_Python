from data.split import Split as Split
from data.vector_database import VectorDataBase as vector_database
from treinamento.analise_tratamento_dados import AnaliseTratamentoDados

class Embeddings:
    def __init__():
        pass
    
    def __init__(self, dados, chunk_size, chunk_overlap, eh_web_scrapping):
        self.dados = dados
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.eh_web_scrapping = eh_web_scrapping

    
    def dividindo(self):
        splitter = Split()
        return splitter.efetua_divisao_documento(self.dados, self.chunk_size, self.chunk_overlap, self.eh_web_scrapping)

    def vetorizador(self):
        documento_dividido = self.dividindo()
        vetor = vector_database()
        store = vetor.carrega_documentos_vectorStore(documento_dividido)
        print(store)
        
    def analise_trate_dados_ausentes(self):
        tratamento_dados = AnaliseTratamentoDados()
        tratamento_dados.exibe_discribe_linhas_colunas(self.dados)
        tratamento_dados.exibe_dados_nulos(self.dados)
        


        

     
        

        
        
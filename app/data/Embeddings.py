from data.Split import Split as Split
from data.vector_database import VectorDataBase as vector_database

class Embeddings:

    def __init__(self, documentos, chunk_size, chunk_overlap, eh_web_scrapping):
        self.documentos = documentos
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.eh_web_scrapping = eh_web_scrapping

    
    def dividindo(self):
        splitter = Split()
        return splitter.efetua_divisao_documento(self.documentos, self.chunk_size, self.chunk_overlap, self.eh_web_scrapping)

    def vetorizador(self):
        documento_dividido = self.dividindo()
        vetor = vector_database()
        store = vetor.carrega_documentos_vectorStore(documento_dividido)
        print(store)


        

     
        

        
        
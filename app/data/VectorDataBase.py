from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch

class VectorDataBase:
    def __init__(self):
        vector_store = None

    #Carrega os documentos que foram feitos o Split(divisão), no banco de dados de vetor (vectorDatabase).
    def carrega_documentos_vectorStore(self, documento_dividido):
        self.documento_dividido = documento_dividido
        vector_store = DocArrayInMemorySearch.from_documents(documento_dividido, embedding=OpenAIEmbeddings())
        return vector_store
       
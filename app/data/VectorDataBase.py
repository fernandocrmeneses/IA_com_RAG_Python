from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch

class VectorDataBase:
    def __init__(self):
        vectorStore = None

    #Carrega os documentos que foram feitos o Split(divisão), no banco de dados de vetor.
    def CarregaDocumentosVectorStore(self, documentoDividido):
        self.documentosDivididos = documentoDividido
        vectorStore = DocArrayInMemorySearch.from_documents(
            documentoDividido, embedding = OpenAIEmbeddings()
        )
        return vectorStore
       
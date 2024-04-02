from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch

class VectorDataBase:
    def __init__(self) -> None:
        pass

    def CarregaDocumentosVectorStore(self, documentoDividido):
        self.documentosDivididos = documentoDividido
        vectorStore = DocArrayInMemorySearch.from_documents(
            documentoDividido, embedding = OpenAIEmbeddings()
        )
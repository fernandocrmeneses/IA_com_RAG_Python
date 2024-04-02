from langchain.text_splitter import RecursiveCharacterTextSplitter

class Split:
    def __init__(self) -> None:
        pass

    #metodo efetua o split do documento para enviar ao vectorDB.
    def EfetuaDivisaoDocumento(self, textoDocumento):
        self.textoDocumento = textoDocumento
        recursivo = RecursiveCharacterTextSplitter(textoDocumento)
        return recursivo
    

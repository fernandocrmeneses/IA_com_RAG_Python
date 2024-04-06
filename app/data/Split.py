from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from util.Configuracoes import Configuracoes as config

class Split:
    def __init__(self):
        self.ambiente = None
        self.url = None
        self.web_scrapping = None  
    
    #metodo efetua o split do documento para enviar ao vectorDB.
    def efetua_divisao_documento(self, texto_documento, chunk_size, chunk_overlap, eh_web_scrapping = False):
        self.texto_documento = texto_documento
        print(texto_documento)
        recursivo_character = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
        if eh_web_scrapping:
            loader = WebBaseLoader(texto_documento)
            return loader.load_and_split(recursivo_character)
        else:
            return self.efetua_divisao_csv(texto_documento)
        
    def efetua_divisao_csv(self, documento_csv):
        lista_documentos = []
        for linha in documento_csv:
            idade = int(linha['idade'])
            genero = linha['gênero']
            imc = float(linha['imc'])
            filhos = int(linha['filhos'])
            fumante = linha['fumante']
            regiao = linha['região']
            encargos = float(linha['encargos'])
        
            # Criar um documento com os dados
            documento = f"Idade: {idade}, Gênero: {genero}, IMC: {imc}, Filhos: {filhos}, Fumante: {fumante}, Região: {regiao}, Encargos: {encargos}"
            lista_documentos.append(documento)
            
        return lista_documentos
            
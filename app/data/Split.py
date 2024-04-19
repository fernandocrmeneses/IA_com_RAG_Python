from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from util.configuracoes import Configuracoes as config
from langchain_core.documents import Document

class Split:
    def __init__(self):
        self.ambiente = None
        self.url = None
        self.web_scrapping = None  
    
    #metodo efetua o split do documento para enviar ao vectorDB.
    def efetua_divisao_documento(self, texto_documento, chunk_size, chunk_overlap, eh_web_scrapping = False):
        self.texto_documento = texto_documento
        recursivo_character = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
        if eh_web_scrapping:
            loader = WebBaseLoader(texto_documento)
            return loader.load_and_split(recursivo_character)
        else:
            return self.efetua_divisao_csv(texto_documento)
        
    def efetua_divisao_csv(self, documento_csv):
        lista_documentos = []
        for linha in documento_csv:
            idade = int(linha[1]['idade'])
            genero = linha[1]['gênero']
            imc = float(linha[1]['imc'])
            filhos = int(linha[1]['filhos'])
            fumante = linha[1]['fumante']
            regiao = linha[1]['região']
            encargos = float(linha[1]['encargos'])
        
            # Criar um documento com os dados
            documento = f"Idade: {idade}, Gênero: {genero}, IMC: {imc}, Filhos: {filhos}, Fumante: {fumante}, Região: {regiao}, Encargos: {encargos}"
            doc =  Document(page_content = documento)
            lista_documentos.append(doc)
        
        
        return lista_documentos
            
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from util.Configuracoes import Configuracoes as config

class Split:
    def __init__(self):
        self.ambiente = None
        self.url = None
        self.web_scrapping = None  
    
    #metodo efetua o split do documento para enviar ao vectorDB.
    def efetua_divisao_documento(self, texto_documento,chunk_size, chunk_overlap, eh_web_scrapping = False):
        self.texto_documento = texto_documento
        recursivo_character = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
        if eh_web_scrapping:
            loader = WebBaseLoader(texto_documento)
            return loader.load_and_split(recursivo_character)
        else:
            return texto_documento
    
    # def obtem_ambiente_para_split(self):
    #     configuracao = config()
    #     json_config = configuracao.obtem_json_configuracao()
    #     fontes_ativas = {}
    #     for fonte, detalhes in json_config['fontes_inputs'].items():
    #         if detalhes['status'] == 'ativo':
    #             fontes_ativas[fonte] = detalhes
                
    #     for fonte, detalhes in fontes_ativas.items():
    #         self.ambiente = fonte
    #         self.url = detalhes["URL"]
    #         self.web_scrapping = detalhes["web_scrapping"]   

import os
from util.arquivo import Arquivo as Arquivo
import json

class Configuracoes:
    
    def __init__(self):
        self.ambiente = None
        self.url = None
        self.web_scrapping = None
        self.json_config = self.obtem_json_configuracao()["configuracoes"]
        self.obtem_configuracao_openAI()
          
    
    def obtem_diretorio_configuracao(self):
        diretorio_atual = os.path.dirname(__file__)
        return f"{os.path.dirname(diretorio_atual)}\\configs\\" 
    
    def obtem_json_configuracao(self):
        with open(f"{self.obtem_diretorio_configuracao()}configuracoes.json") as arquivo_json:
            return json.load(arquivo_json)
    
    def obtem_ambiente_ativo(self):
        
        fontes_ativas = {}
        dados = []
        for fonte, detalhes in self.json_config["fontes_inputs"].items():
            if detalhes['status'] == 'ativo':
                fontes_ativas[fonte] = detalhes
                
        for fonte, detalhes in fontes_ativas.items():
            dados.append(fonte)
            dados.append(detalhes["URL"])
            dados.append(detalhes["web_scrapping"])
        return dados
    
    def obtem_chunk_size(self):
        return self.json_config["chunk_size"]
    
    def obtem_chunk_overlap(self):
        return self.json_config["overlap_chunk"]
    
    def obtem_configuracao_openAI(self):
        os.environ["OPENAI_API_KEY"] = f"{self.json_config['token_openAI']}"
        os.environ["MODEL"] = f"{self.json_config['modelo_openAI']}"
    
    
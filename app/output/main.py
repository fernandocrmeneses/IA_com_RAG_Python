
from util.arquivo import Arquivo
from data.embeddings import Embeddings
from util.configuracoes import Configuracoes
from treinamento.analise_tratamento_dados import AnaliseTratamentoDados
import os



def main():
    config = Configuracoes()
    analise = AnaliseTratamentoDados()
    dados_ambiente = config.obtem_ambiente_ativo()
    
    if dados_ambiente[0] == "excel":
        print(config.obtem_diretorio_configuracao())
        arq = Arquivo(config.obtem_diretorio_configuracao(), "dadosComplementaresFIAP")
        _dados = arq.ler_arquivo_CSV(retorna_head = True)
        embeddings = Embeddings(_dados, config.obtem_chunk_size(), config.obtem_chunk_overlap(), dados_ambiente[2])
        analise.exibe_describe_linhas_colunas(dados = _dados)
        analise.exibe_dados_nulos(dados = _dados)
        dados_sem_ausencias = analise.trata_dados_ausentes(dados = _dados)
        if dados_sem_ausencias != None :
           _dados = dados_sem_ausencias
        
        analise.obtem_colunas_booleanas(_dados) 
    
    if dados_ambiente[0] == "sites":
        embeddings = Embeddings(dados_ambiente[1], config.obtem_chunk_size(), config.obtem_chunk_overlap(), dados_ambiente[2])
        #embeddings.vetorizador()


main()
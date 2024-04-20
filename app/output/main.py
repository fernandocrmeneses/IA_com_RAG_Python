
from util.arquivo import Arquivo
from data.embeddings import Embeddings
from util.configuracoes import Configuracoes
from treinamento.analise_tratamento_dados import AnaliseTratamentoDados
from treinamento.modelos.modelos_classificacao import ModelosDeClassificacao
import os



def main():
    config = Configuracoes()
    analise = AnaliseTratamentoDados()
    modelos = ModelosDeClassificacao()
    dados_ambiente = config.obtem_ambiente_ativo()
    
    if dados_ambiente[0] == "excel":
        print(config.obtem_diretorio_configuracao())
        arq = Arquivo(config.obtem_diretorio_configuracao(), "dadosComplementaresFIAP")
        _dados = arq.ler_arquivo_CSV(retorna_head = True)
        embeddings = Embeddings(_dados, config.obtem_chunk_size(), config.obtem_chunk_overlap(), dados_ambiente[2])
        
        #analise.exibe_describe_linhas_colunas(dados = _dados)
        #analise.exibe_dados_nulos(dados = _dados)
        modelos.define_variavel_target(_dados, "encargos")
        dados_sem_ausencias = modelos.trata_dados_ausentes(dados = _dados)
        if dados_sem_ausencias != None :
           _dados = dados_sem_ausencias
        
        colunas_booleanas = modelos.obtem_colunas_booleanas(_dados)
        colunas_one_hot = modelos.obtem_colunas_nao_booleanas(_dados)
        colunas_apagar =["encargos", "região"]
        _dados = modelos.aplica_tecnica_label_encoder(_dados, colunas_booleanas)
        #analise.exibe_describe_linhas_colunas(_dados)
        _dados = modelos.aplica_one_hot_encoding(_dados, colunas_one_hot, colunas_apagar, "dummy")
        analise.exibe_describe_linhas_colunas(_dados)
        analise.exibe_correlacao_dados(_dados)
        #analise.aplica_one_hot_enconding(_dados)
         
    
    if dados_ambiente[0] == "sites":
        embeddings = Embeddings(dados_ambiente[1], config.obtem_chunk_size(), config.obtem_chunk_overlap(), dados_ambiente[2])
        #embeddings.vetorizador()


main()
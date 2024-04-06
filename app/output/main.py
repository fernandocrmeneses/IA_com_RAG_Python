
from util.arquivo import Arquivo
from data.Embeddings import Embeddings
from util.Configuracoes import Configuracoes
import os



def main():
    config = Configuracoes()
    dados_ambiente = config.obtem_ambiente_ativo()
    
    if dados_ambiente[0] == "excel":
        arq = Arquivo(config.obtem_diretorio_configuracao(), "arquivoCSV")
        dados_para_split = arq.ler_arquivo_CSV()
        embeddings = Embeddings(dados_para_split, config.obtem_chunk_size(), config.obtem_chunk_overlap(), dados_ambiente[2])
        embeddings.vetorizador()
    
    if dados_ambiente[0] == "FIAP":
        embeddings = Embeddings(dados_ambiente[1], config.obtem_chunk_size(), config.obtem_chunk_overlap(), dados_ambiente[2])
        embeddings.vetorizador()


main()